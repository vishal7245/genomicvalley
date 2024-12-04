import reflex as rx


from genomicvalley.components.footer import footer
from genomicvalley.components.navbar_2 import navbar_white as navbar
from genomicvalley.components.faq import faq_section
from genomicvalley.components.banner import banner


@rx.page(route="/faq", title="Frequently Asked Questions")
def faq_page():
    return rx.vstack(
        rx.html(
        """
                <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-7C0KZ36E1J"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-7C0KZ36E1J');
        </script>
        """    
        ),
        navbar(),
        banner("FAQs"),
        faq_section(),
        footer(),
    )
