import reflex as rx


from genomicvalley.components.footer import footer
from genomicvalley.components.navbar import navbar
from genomicvalley.components.contact import contact_section
from genomicvalley.components.banner import banner




@rx.page(route="/contact", title="Contact Us")
def contact_page():
    return rx.vstack(
        navbar(),
        banner("Contact Us"),
        contact_section(),
        footer(),
    )
    