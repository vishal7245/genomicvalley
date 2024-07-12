from __future__ import annotations
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import feedparser
import reflex as rx
from genomicvalley.models import ContactForm
import pytz
import datetime
from sqlmodel import Column, DateTime, Field, func
from sqlmodel import select
from .models import LocalUser

LOGIN_ROUTE = "/admin"


load_dotenv()


def getdatetime():
    utc_now = datetime.datetime.now(pytz.utc)

    # Convert to IST
    ist_tz = pytz.timezone("Asia/Kolkata")
    ist_now = utc_now.astimezone(ist_tz)

    # Format the date and time
    formatted_date = ist_now.strftime("%d/%m/%y")
    formatted_time = ist_now.strftime("%I:%M:%S %p")

    return f"{formatted_time} {formatted_date}"


class ContactDatabase:
    def add_entry(self, first_name, last_name, email, phone, message):  # send mail
        with rx.session() as session:
            session.add(
                ContactForm(
                    first_name=first_name,
                    last_name=last_name,
                    phone=str(phone),
                    email=email,
                    message=message,
                    timestamp=str(getdatetime()),
                )
            )
            session.commit()
        self.send_email(first_name, last_name, email, phone, message)

    def send_email(self, first_name, last_name, email, phone, message):
        sender_email = os.getenv("SENDER_EMAIL")
        receiver_email = os.getenv("RECEIVER_EMAIL")
        subject = "Genomic Valley Contact"
        body = f""" 
                Title: Genomic Valley Contact

                Message: {message}

                Name: {first_name} {last_name}
                Phone: {phone}
                Email: {email}
                Timestamp: {getdatetime()}
                """

        smtp_server = "smtp.zoho.in"
        smtp_port = 587
        smtp_username = os.getenv("SENDER_EMAIL")
        smtp_password = os.getenv("PASSWORD")
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())


class GetRss:
    rss_urls = [
        "https://health.economictimes.indiatimes.com/rss/diagnostics",
        "https://health.economictimes.indiatimes.com/rss/medical-devices",
    ]

    @classmethod
    def getnews(cls):
        news = []
        for url in cls.rss_urls:
            entry = cls.parse_news(url)
            news = cls.merge_lists(news, entry)
        return news

    @classmethod
    def get_titles(cls):
        titles = []
        for url in cls.rss_urls:
            entries = cls.parse_news(url)
            titles.extend(entry["title"] for entry in entries)
        return titles

    @staticmethod
    def parse_news(url):
        data = feedparser.parse(url)
        entries = data.get("entries", [])
        return [
            {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "summary": entry.get("summary", ""),
            }
            for entry in entries
        ]

    @staticmethod
    def merge_lists(list1, list2):
        merged_list = []
        for item1, item2 in zip(list1, list2):
            merged_list.extend([item1, item2])
        merged_list.extend(list1[len(list2) :] + list2[len(list1) :])
        return merged_list


# Authentication Logic
#
#
#


class LocalAuthSession(
    rx.Model,
    table=True,  # type: ignore
):
    """Correlate a session_id with an arbitrary user_id."""

    user_id: int = Field(index=True, nullable=False)
    session_id: str = Field(unique=True, index=True, nullable=False)
    expiration: datetime.datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=False
        ),
    )


AUTH_TOKEN_LOCAL_STORAGE_KEY = "_auth_token"
DEFAULT_AUTH_SESSION_EXPIRATION_DELTA = datetime.timedelta(days=7)


class LocalAuthState(rx.State):
    # The auth_token is stored in local storage to persist across tab and browser sessions.
    auth_token: str = rx.LocalStorage(name=AUTH_TOKEN_LOCAL_STORAGE_KEY)

    @rx.cached_var
    def authenticated_user(self) -> LocalUser:
        """The currently authenticated user, or a dummy user if not authenticated.

        Returns:
            A LocalUser instance with id=-1 if not authenticated, or the LocalUser instance
            corresponding to the currently authenticated user.
        """
        with rx.session() as session:
            result = session.exec(
                select(LocalUser, LocalAuthSession).where(
                    LocalAuthSession.session_id == self.auth_token,
                    LocalAuthSession.expiration
                    >= datetime.datetime.now(datetime.timezone.utc),
                    LocalUser.id == LocalAuthSession.user_id,
                ),
            ).first()
            if result:
                user, session = result
                return user
        return LocalUser(id=-1)  # type: ignore

    @rx.cached_var
    def is_authenticated(self) -> bool:
        """Whether the current user is authenticated.

        Returns:
            True if the authenticated user has a positive user ID, False otherwise.
        """
        return self.authenticated_user.id >= 0

    def do_logout(self) -> None:
        """Destroy LocalAuthSessions associated with the auth_token."""
        with rx.session() as session:
            for auth_session in session.exec(
                select(LocalAuthSession).where(
                    LocalAuthSession.session_id == self.auth_token
                )
            ).all():
                session.delete(auth_session)
            session.commit()
        self.auth_token = self.auth_token

    def _login(
        self,
        user_id: int,
        expiration_delta: datetime.timedelta = DEFAULT_AUTH_SESSION_EXPIRATION_DELTA,
    ) -> None:
        """Create an LocalAuthSession for the given user_id.

        If the auth_token is already associated with an LocalAuthSession, it will be
        logged out first.

        Args:
            user_id: The user ID to associate with the LocalAuthSession.
            expiration_delta: The amount of time before the LocalAuthSession expires.
        """
        self.do_logout()
        if user_id < 0:
            return
        self.auth_token = self.auth_token or self.router.session.client_token
        with rx.session() as session:
            session.add(
                LocalAuthSession(  # type: ignore
                    user_id=user_id,
                    session_id=self.auth_token,
                    expiration=datetime.datetime.now(datetime.timezone.utc)
                    + expiration_delta,
                )
            )
            session.commit()


class RegistrationState(LocalAuthState):
    """Handle user creation and management."""

    error_message: str = ""

    @classmethod
    def create_default_user(cls):
        """Create a default user if it doesn't exist."""
        username = os.environ.get("DEFAULT_USERNAME")
        password = os.environ.get("DEFAULT_PASSWORD")

        if not username or not password:
            raise ValueError(
                "DEFAULT_USERNAME and DEFAULT_PASSWORD must be set in environment variables"
            )

        with rx.session() as session:
            existing_user = session.exec(
                select(LocalUser).where(LocalUser.username == username)
            ).one_or_none()

            if existing_user is None:
                new_user = LocalUser()
                new_user.username = username
                new_user.password_hash = LocalUser.hash_password(password)
                new_user.enabled = True
                session.add(new_user)
                session.commit()
                print(f"Default user '{username}' created successfully.")
            else:
                print(f"Default user '{username}' already exists.")


RegistrationState.create_default_user()


class LoginState(LocalAuthState):
    """Handle login form submission and redirect to proper routes after authentication."""

    error_message: str = ""
    redirect_to: str = ""

    def on_submit(self, form_data) -> rx.event.EventSpec:
        """Handle login form on_submit.
        Args:
            form_data: A dict of form fields and values.
        """
        self.error_message = ""
        username = form_data["username"]
        password = form_data["password"]

        with rx.session() as session:
            user = session.exec(
                select(LocalUser).where(LocalUser.username == username)
            ).one_or_none()

        if user is not None and not user.enabled:
            self.error_message = "This account is disabled."
            return rx.set_value("password", "")

        if (
            user is not None
            and user.id is not None
            and user.enabled
            and password
            and user.verify(password)
        ):
            # mark the user as logged in
            self._login(user.id)
        else:
            self.error_message = "There was a problem logging in, please try again."
            return rx.set_value("password", "")

        self.error_message = ""
        return self.redir()  # type: ignore

    def redir(self) -> rx.event.EventSpec | None:
        """Redirect to the home page if logged in, or to the login page if not."""
        if not self.is_hydrated:
            # wait until after hydration to ensure auth_token is known
            return LoginState.redir

        page = self.router.page.path

        if not self.is_authenticated and page != LOGIN_ROUTE:
            return rx.redirect(LOGIN_ROUTE)
        elif self.is_authenticated and page == LOGIN_ROUTE:
            return rx.redirect("/dashboard")
        else:
            return None


def require_login(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:
    """Decorator to require authentication before rendering a page.

    If the user is not authenticated, then redirect to the login page.

    Args:
        page: The page to wrap.

    Returns:
        The wrapped page component.
    """
    print("Decorator Called")

    def protected_page():
        return rx.fragment(
            rx.cond(
                LoginState.is_hydrated & LoginState.is_authenticated,  # type: ignore
                page(),
                rx.center(
                    # When this text mounts, it will redirect to the login page
                    rx.text("Loading...", on_mount=LoginState.redir),
                ),
            )
        )

    protected_page.__name__ = page.__name__
    return protected_page
