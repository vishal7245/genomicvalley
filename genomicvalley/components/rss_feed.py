import reflex as rx
from genomicvalley.state import GetRss
from typing import Any


class NewsState(rx.State):
    news_list: list[dict[str, Any]] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.news_list = GetRss.getnews()


def news_card(heading: str, summary: str, read_more_url: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(heading, size="3", color="black"),
            rx.text(summary, color="gray", style={"text_align": "justify"}),
            rx.button(
                "Read More",
                on_click=lambda: rx.redirect(
                    read_more_url,
                    external=True,
                ),
                color_scheme="green",
                size="2",
                align_self="flex-start",
                margin_top="1em",
            ),
            spacing="2",
            align_items="flex-start",
        ),
        width="97%",
        padding="1em",
        margin="1em",
    )


def mobile_news_card(heading: str, summary: str, read_more_url: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(heading, size="3", color="black"),
            rx.text(summary, color="gray", style={"text_align": "justify"}),
            rx.button(
                "Read More",
                on_click=lambda: rx.redirect(
                    read_more_url,
                    external=True,
                ),
                color_scheme="green",
                size="2",
                align_self="flex-start",
                margin_top="1em",
            ),
            spacing="2",
            align_items="flex-start",
        ),
        width="100%",
        padding="1em",
        margin_bottom="1em",
    )


def news_section() -> rx.Component:
    return rx.section(
        rx.desktop_only(
            rx.section(
                rx.vstack(
                    rx.box(
                        rx.heading(
                            "NEWS AND UPDATES",
                            size="5",
                            weight="bold",
                            margin_bottom="1em",
                            color="green",
                            align="center",
                        ),
                        width="100%",
                    ),
                    rx.heading(
                        "Stay updated with the latest healthcare news",
                        size="8",
                        weight="medium",
                        color="black",
                        margin_bottom="30px",
                        align="center",
                    ),
                    rx.center(  # Added a center component
                        rx.vstack(
                            rx.scroll_area(
                                rx.foreach(
                                    NewsState.news_list,
                                    lambda news: news_card(
                                        news["title"], news["summary"], news["link"]
                                    ),
                                ),
                                type="always",
                                scrollbars="vertical",
                                style={
                                    "height": "620px",
                                    "width": "100%",
                                    "max_width": "70%",
                                },  # Added max-width
                            ),
                            width="100%",
                            align_items="center",
                        ),
                        width="100%",
                    ),
                    width="100%",
                    align_items="center",
                ),
                justify_content="center",
                align_items="center",
                width="100%",
            )
        ),
        rx.mobile_and_tablet(
            rx.mobile_and_tablet(
                rx.vstack(
                    rx.box(
                        rx.heading(
                            "NEWS AND UPDATES",
                            size="5",
                            weight="bold",
                            margin_bottom="1em",
                            color="green",
                            align="center",
                        ),
                        width="100%",
                    ),
                    rx.heading(
                        "Stay updated with the latest healthcare news",
                        size="6",
                        weight="medium",
                        color="black",
                        margin_bottom="10px",
                        align="center",
                    ),
                    rx.vstack(
                        rx.vstack(
                            rx.scroll_area(
                                rx.foreach(
                                    NewsState.news_list,
                                    lambda news: mobile_news_card(
                                        news["title"], news["summary"], news["link"]
                                    ),
                                ),
                                type="always",
                                scrollbars="vertical",
                                style={
                                    "height": "620px",
                                    "width": "100%",
                                },  # Added max-width
                            ),
                            width="100%",
                            align_items="center",
                        ),
                    ),
                    justify_content="center",
                    align_items="center",
                    width="100%",
                    padding="1em",
                )
            )
        ),
        width="100%",
    )
