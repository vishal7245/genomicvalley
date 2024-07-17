import reflex as rx
from genomicvalley.state import LoginState

style_login_form = {
    "background_color": "rgba(128,212,148,0.2)",
}


def login_error() -> rx.Component:
    """Render the login error message."""
    return rx.cond(
        LoginState.error_message != "",
        rx.callout(
            LoginState.error_message,
            icon="triangle_alert",
            color_scheme="red",
            role="alert",
            width="100%",
        ),
    )


def login_form() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.heading(
                    "Admin Login",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                    color="black",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            login_error(),
            rx.form(
                rx.vstack(
                    rx.vstack(
                        rx.text(
                            "Username",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                            color="black",
                        ),
                        rx.input(
                            placeholder="username",
                            size="3",
                            width="100%",
                            id="username",
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "Password", size="3", weight="medium", color="black"
                            ),
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Enter your password",
                            type="password",
                            size="3",
                            width="100%",
                            id="password",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.button("Sign in", size="3", width="100%", type="submit"),
                    spacing="6",
                    width="100%",
                ),
                on_submit=LoginState.on_submit,
            ),
        ),
        size="4",
        max_width="28em",
        width="100%",
        style=style_login_form,
    )
