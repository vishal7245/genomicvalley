import reflex as rx


from genomicvalley.components.footer import footer
from genomicvalley.components.navbar_2 import navbar_white as navbar
from genomicvalley.components.banner import banner
from genomicvalley.state import LocalAuthState


@rx.page(route="/logout", title="logout", on_load=LocalAuthState.do_logout)
def logout():
    return rx.vstack(
        navbar(),
        banner("Logged Out"),
        footer(),
    )
