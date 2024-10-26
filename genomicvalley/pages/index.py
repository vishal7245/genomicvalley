import reflex as rx

# from genomicvalley.components.hero import hero
from genomicvalley.components.faq import faq_section
from genomicvalley.components.footer import footer
from genomicvalley.components.navbar import navbar
from genomicvalley.components.contact import contact_section
from genomicvalley.components.services import services_section
from genomicvalley.components.image_gallery import image_gallery
from genomicvalley.components.about_section import about_section
from genomicvalley.components.hero import hero_section
from genomicvalley.state import VisitorStats
from genomicvalley.components.our_vision import vision_section
from genomicvalley.components.career_form import career_form
from genomicvalley.components.create_announcement import create_announcement
from genomicvalley.components.testimonials import testimonials_section
from genomicvalley.components.video_section import video_section


@rx.page(title="Genomic Valley", on_load=VisitorStats.log_visitor)
def index():
    return rx.vstack(
        navbar(),
        hero_section(),
        about_section(),
        services_section(),
        video_section(),
        faq_section(),
        testimonials_section(),
        image_gallery(),
        contact_section(),
        footer(),
        spacing="0",
    )
