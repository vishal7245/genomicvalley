import reflex as rx

from genomicvalley.components.footer import footer
from genomicvalley.components.navbar_2 import navbar_white as navbar
from genomicvalley.components.banner import banner
from genomicvalley.components.career_form import career_form


@rx.page(route="/career", title="Career")
def career_page():
    return rx.vstack(
        navbar(),
        banner("Career"),
        career_form(),
        footer(),
    )
