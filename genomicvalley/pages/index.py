import reflex as rx

from genomicvalley.components.hero import hero
from genomicvalley.components.faq import faq_section
from genomicvalley.components.footer import footer
from genomicvalley.components.navbar import navbar
from genomicvalley.components.contact import contact_section
from genomicvalley.components.services import services_section
from genomicvalley.components.testimonials import testimonials_section
from genomicvalley.components.image_gallery import image_gallery
from genomicvalley.components.about_section import about_section


@rx.page()
def index(title="Genomic Valley"):
    return rx.vstack(
        navbar(),
        hero(),
        about_section(),
        image_gallery(),
        services_section(),
        testimonials_section(),
        faq_section(),
        contact_section(),
        footer(),
    )





    