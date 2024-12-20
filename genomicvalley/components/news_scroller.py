import reflex as rx
from genomicvalley.state import GetRss

class NewsTitleState():
    news_list: list = []
    news_list_string: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.news_list = GetRss.get_titles()
        self.news_list_string = " | ".join(self.news_list)
        
news = NewsTitleState()

def news_scroller() -> rx.Component:
    return rx.link(
        rx.section(
            rx.html(
                f"""
                <div style="display: flex;">
                <marquee behavior="scroll" scrollamount="8" direction="left" style="font-size: 25px; color: #FDFFBA;">{news.news_list_string}</marquee>
                </div>
                """
            ),
            width="100%",
            padding_top="10px",
            padding_bottom="10px",
            margin="0",
        ),
        href="/news"
    )