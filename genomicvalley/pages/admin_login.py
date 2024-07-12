import reflex as rx
from genomicvalley.components.login_form import login_form
from genomicvalley.state import LoginState


@rx.page(route="/admin", title="Admin Login", on_load=LoginState.redir)
def admin_login():
    return rx.center(
        rx.vstack(
            rx.cond(
                LoginState.is_hydrated,  # type: ignore
                login_form(),
            ),
            justify="center",
            align_items="center",
            height="100vh",
        ),
    )
