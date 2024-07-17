import reflex as rx


def dashboard_navbar() -> rx.Component:
    return rx.box(
        rx.text("Dashboard", font_size="xl", font_weight="bold"),
        position="fixed",
        top="0",
        left="0",
        right="0",
        height="60px",
        background_color="gray",
        color="white",
        display="flex",
        align_items="center",
        justify_content="center",
        z_index="10",
    )
