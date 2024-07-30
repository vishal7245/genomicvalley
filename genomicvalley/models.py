from __future__ import annotations
import bcrypt
import reflex as rx
from sqlmodel import Field


class AnnouncementModel(rx.Model, table=True):
    title: str
    body: str
    date: str
    author: str
    month: int
    year: int


class ContactForm(rx.Model, table=True):
    first_name: str
    last_name: str
    phone: str
    email: str
    message: str
    date: str
    seen: bool
    month: int
    year: int


class VisitorModel(rx.Model, table=True):
    ip_address: str
    lat: float
    long: float
    country: str
    city: str
    date: str
    month: int
    year: int


class LocalUser(
    rx.Model,
    table=True,  # type: ignore
):
    """A local User model with bcrypt password hashing."""

    username: str = Field(unique=True, nullable=False, index=True)
    password_hash: bytes = Field(nullable=False)
    enabled: bool = False

    @staticmethod
    def hash_password(secret: str) -> str:
        """Hash the secret using bcrypt.

        Args:
            secret: The password to hash.

        Returns:
            The hashed password.
        """
        return bcrypt.hashpw(
            password=secret.encode("utf-8"),
            salt=bcrypt.gensalt(),
        )

    def verify(self, secret: str) -> bool:
        """Validate the user's password.

        Args:
            secret: The password to check.

        Returns:
            True if the hashed secret matches this user's password_hash.
        """
        return bcrypt.checkpw(
            password=secret.encode("utf-8"),
            hashed_password=self.password_hash,
        )

    def dict(self, *args, **kwargs) -> dict:
        """Return a dictionary representation of the user."""
        d = super().dict(*args, **kwargs)
        # Never return the hash when serializing to the frontend.
        d.pop("password_hash", None)
        return d
