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
from genomicvalley.components.rss_feed import news_section

@rx.page()
def index(title="Genomic Valley"):
    return rx.vstack(
        navbar(),
        hero_section(),
        about_section(),
        image_gallery(),
        services_section(),
        faq_section(),
        news_section(),
        contact_section(),
        footer(),
        spacing="0",
    )





    