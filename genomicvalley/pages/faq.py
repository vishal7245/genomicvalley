import reflex as rx


from genomicvalley.components.footer import footer
from genomicvalley.components.navbar_2 import navbar_white as navbar
from genomicvalley.components.faq import faq_section
from genomicvalley.components.banner import banner


@rx.page(route="/faq", title="Frequently Asked Questions")
def faq_page():
    return rx.vstack(
        navbar(),
        banner("FAQs"),
        faq_section(),
        footer(),
    )
