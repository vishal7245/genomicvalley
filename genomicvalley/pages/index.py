import reflex as rx

# from genomicvalley.components.hero import hero
from genomicvalley.components.faq import faq_section
from genomicvalley.components.footer import footer
from genomicvalley.components.navbar import navbar
from genomicvalley.components.contact import contact_section
from genomicvalley.components.services import services_section
from genomicvalley.components.testimonials import testimonials_section
from genomicvalley.components.image_gallery import image_gallery
from genomicvalley.components.about_section import about_section
from genomicvalley.components.hero import hero_section
from genomicvalley.components.news_scroller import news_scroller


@rx.page(title="Genomic Valley")
def index():
    return rx.vstack(
        navbar(),
        hero_section(),
        about_section(),
        services_section(),
        faq_section(),
        image_gallery(),
        contact_section(),
        footer(),
        spacing="0",
    )





    