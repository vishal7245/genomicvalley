import reflex as rx
from genomicvalley.components.news_scroller import news_scroller


class TypeAnimation(rx.Component):
    """ReflexTypeAnimation component."""

    tag = "TypeAnimation"
    library = "react-type-animation"
    sequence: rx.Var[list]
    speed: rx.Var[int]
    repeat: rx.Var[str] = "infinite"
    wrapper: rx.Var[str] = "span"
    cursor: rx.Var[bool] = True
    pre_render_first_string: rx.Var[bool] = False
    deletion_speed: rx.Var[int] = 40
    omit_deletion_animation: rx.Var[bool] = False
    style: dict = {"fontSize": "2em", "color": "black"}


type_animation = TypeAnimation.create

heading_font = {
    "font_size": ["1em", "1em", "2em", "3em", "4em"],
    "line_height": ["1.2", "1.1", "1", "0.9", "0.8"],
    "margin_bottom": "5px",
}

hero_card_style = {
    "padding": "2em",
    "border_radius": "1em",
    "backdrop_filter": "blur(60px)",
    "background_color": "rgba(255, 255, 255, 0.1)",  # Added for better visibility
    "max_width": "950px",  # Limit the maximum width
    "width": "90%",  # Take up 90% of the container width, but not more than max-width
    "margin_left": "3%",  # Add some left margin
    "margin_top": "20%",
}

news_scroller_style = {
    "backdrop_filter": "blur(60px)",
    "background_color": "rgba(255, 255, 255, 0.1)",
}


def hero_section():
    return rx.section(
        rx.desktop_only(
            rx.box(
                rx.vstack(
                    rx.vstack(
                        rx.heading("Genomic Valley", color="white", style=heading_font),
                        type_animation(
                            sequence=[
                                "Where Health Meets Technology.",
                                1000,
                                "Where Health Meets Breakthroughs.",
                                1000,
                                "Where Health Meets Precision.",
                                1000,
                                "A dynamic startup reshaping healthcare with advanced solutions.",
                                1000,
                            ],
                            style={
                                "color": "#d5d2cb",
                                "fontSize": "30px",
                            },
                        ),
                        rx.hstack(
                            rx.button(
                                "Brochure",
                                size="3",
                                color_scheme="teal",
                                on_click=rx.download(
                                    url="/GV_Biotech.pdf",
                                ),
                            ),
                            rx.link(
                                rx.button(
                                    "Contact Us",
                                    size="3",
                                    variant="solid",
                                    color_scheme="teal",
                                ),
                                href="/contact",
                            ),
                            spacing="4",  # Add spacing between buttons
                        ),
                        spacing="4",
                        align_items="flex_start",  # Align items to the start (left) within the vstack
                        style=hero_card_style,
                    ),
                    justify_content="center",  # Center the card vertically
                    height="100%",  # Take full height of the parent
                    width="100%",  # Take full width of the parent
                ),
                rx.box(
                    news_scroller(),
                    position="absolute",
                    bottom="0",
                    left="0",
                    right="0",
                    style=news_scroller_style,
                ),
                background_image="url('hero-bg.jpg')",
                background_size="cover",
                background_position="center",
                width="100%",
                height="100vh",  # Full viewport height
                margin="0",
                padding="0",
                position="relative",
            )
        ),
        rx.mobile_and_tablet(
            rx.box(
                rx.vstack(
                    rx.vstack(
                        rx.heading(
                            "Genomic Valley",
                            color="white",
                            style={
                                "fontSize": "30px",
                                "lineHeight": "clamp(1.2, 4vw, 2em)",
                            },
                        ),
                        type_animation(
                            sequence=[
                                "Where Health Meets Technology.",
                                1000,
                                "Where Health Meets Breakthroughs.",
                                1000,
                                "Where Health Meets Precision.",
                                1000,
                                "Where Health Meets Innovation.",
                                1000,
                            ],
                            style={
                                "color": "#d5d2cb",
                                "fontSize": "15px",  # Responsive font size
                                "textAlign": "center",  # Center text
                            },
                        ),
                        rx.hstack(  # Changed from hstack to vstack for better mobile layout
                            rx.button(
                                "Brochure",
                                size="3",
                                color_scheme="teal",
                                on_click=rx.download(
                                    url="/Genomic Valley-Brochure.pdf"
                                ),
                            ),
                            rx.link(
                                rx.button(
                                    "Contact Us",
                                    size="3",
                                    variant="solid",
                                    color_scheme="teal",
                                ),
                                href="/contact",
                            ),
                            spacing="4",  # Add spacing between buttons
                        ),
                        spacing="4",
                        align_items="center",  # Center items horizontally
                        style=hero_card_style,
                    ),
                    justify_content="center",  # Center the card vertically
                    align_items="center",  # Center the card horizontally
                    height="100%",
                    width="100%",
                    max_width="600px",  # Limit maximum width for larger screens
                    padding="1rem",  # Add some padding around the content
                ),
                rx.box(
                    news_scroller(),
                    position="absolute",
                    bottom="0",
                    left="0",
                    right="0",
                    style=news_scroller_style,
                ),
                position="relative",
                background_image="url('hero-bg.jpg')",
                background_size="cover",
                background_position="center",
                width="100%",
                height="90vh",  # Full viewport height
                margin="0",
                padding="0",  # Remove padding from the main box
                display="flex",
                justify_content="center",  # Center the content horizontally
                align_items="center",  # Center the content vertically
            )
        ),
        width="100%",
        padding="0",
    )
