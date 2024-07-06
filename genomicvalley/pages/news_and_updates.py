import reflex as rx


from genomicvalley.components.footer import footer
from genomicvalley.components.navbar_2 import navbar_white as navbar
from genomicvalley.components.banner import banner
from genomicvalley.components.rss_feed import news_section


@rx.page(route="/news", title="News and Updates")
def news_and_updates():
    return rx.vstack(
        navbar(),
        banner("News and Updates"),
        news_section(),
        footer(),
    )





    