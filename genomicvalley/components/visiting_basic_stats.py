import reflex as rx
from genomicvalley.state import VisitorStats


from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)


def stats(
    stat_name: str = "Users",
    value: int = 4200,
    icon: str = "users",
    badge_color: LiteralAccentColor = "green",
) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.badge(
                    rx.icon(tag=icon, size=34),
                    color_scheme=badge_color,
                    radius="full",
                    padding="0.7rem",
                ),
                rx.vstack(
                    rx.heading(f"{value:,}", size="6", weight="bold", color="black"),
                    rx.text(stat_name, size="4", weight="medium", color="gray"),
                    spacing="1",
                    height="100%",
                    align_items="start",
                    width="100%",
                    black="black",
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


def visiting_basic_stats() -> rx.Component:
    return rx.section(
        rx.grid(
            stats(stat_name="Total Visitors", value=VisitorStats.total_visitors),
            stats(stat_name="Unique Visitos", value=VisitorStats.unique_visitors),
            stats(stat_name="Monthly Visitos", value=VisitorStats.monthly_visitors),
            stats(
                stat_name="Monthly Unique Visitors",
                value=VisitorStats.unique_monthly_visitors,
            ),
            stats(stat_name="Daily Visitors", value=VisitorStats.daily_visitors),
            stats(
                stat_name="Daily Unique Visitors",
                value=VisitorStats.unique_daily_visitors,
            ),
            columns="6",
            spacing="4",
            width="100%",
            padding="1em",
        ),
        width="100%",
        padding_top="3em",
    )
