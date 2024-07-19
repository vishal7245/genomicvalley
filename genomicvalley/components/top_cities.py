import reflex as rx
from genomicvalley.state import VisitorStats, CityStats


def stats(city_obj: CityStats) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="building-2", size=34),
                    color_scheme="green",
                    radius="full",
                    padding="0.7rem",
                ),
                rx.vstack(
                    rx.heading(city_obj.count, size="6", weight="bold", color="black"),
                    rx.text(city_obj.city, size="4", weight="medium", color="gray"),
                    spacing="1",
                    height="100%",
                    align_items="start",
                    width="100%",
                ),
                height="100%",
                spacing="4",
                align="center",
                width="100%",
            ),
        ),
        size="3",
        width="100%",
        max_width="21rem",
    )


def top_cities() -> rx.Component:
    return rx.section(
        rx.vstack(
            rx.heading(
                "TOP CITIES",
                size="5",
                weight="bold",
                color="green",
            ),
            rx.section(
                rx.grid(
                    rx.foreach(VisitorStats.city_wise, stats),
                    columns="6",
                    spacing="1",
                    padding_left="1em",
                    padding_right="1em",
                    width="100%",
                ),
                width="100%",
            ),
            justify_content="center",
            align_items="center",
            width="100%",
            spacing="0",
        ),
        width="100%",
    )
