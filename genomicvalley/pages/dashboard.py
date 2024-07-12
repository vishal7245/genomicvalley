import reflex as rx


from genomicvalley.components.footer import footer
from genomicvalley.components.navbar_2 import navbar_white as navbar
from genomicvalley.components.banner import banner
from genomicvalley.state import require_login, LocalAuthState


@rx.page(route="/dashboard", title="Dashboard")
@require_login
def dashboard():
    return rx.vstack(
        navbar(),
        banner("Dashboard"),
        rx.text(f"{LocalAuthState.authenticated_user.username}", color="black"),
        footer(),
    )
