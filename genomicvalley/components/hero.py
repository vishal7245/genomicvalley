import reflex as rx
import json,ast

hero_style = {
    "width": "100%",
    "height": "90vh",
    "background-color":"hsla(231,0%,100%,1);",
    "background-image":
"""radial-gradient(at 58% 53%, hsla(147,100%,50%,0.71) 0px, transparent 50%),
radial-gradient(at 85% 43%, hsla(137,78%,61%,1) 0px, transparent 50%);""",
    "background-size": "cover",
    "background-position": "center",
}


# hero_card_style = {
#     "padding": "2em",
#     "border_radius": "1em",
#     "width": "50%",
#     "height": "50%",
#     "backdrop-filter": "blur(60px)",
#     "margin_top": "10em",
#     "margin_left": "5em",
# }

hero_font_style = {
    "background_image": "url('/bg-hero.jpeg')",
    "text_fill_color": "transparent",
    "background_clip": "text",
    "-webkit-background-clip": "text",
}


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
    style: dict = {'fontSize': '2em', 'color': "black"}



type_animation = TypeAnimation.create


heading_font = {
    "font_size": ["1em", "2em", "3em", "4em", "5em"],
    "line_height": ["1.2", "1.1", "1", "0.9", "0.8"],
    "margin_bottom": "0.5em",
}

def hero():
    return rx.section(
        rx.desktop_only(
            rx.box(
                rx.hstack(
                    # Left side: Main text and button
                    rx.vstack(
                        rx.heading("Genomic Valley", color="black", style=heading_font),
                        type_animation(
                            sequence=[
                                'Where Health Meets Technology.',
                                1000,
                                'Where Health Meets Breakthroughs.',
                                1000,
                                'Where Health Meets Precision.',
                                1000,
                                'Where Health Meets Innovation.',
                                1000,
                            ],
                            style={
                                "color": "gray",
                                "fontSize": "2em",
                            },
                        ),
                        rx.hstack(
                            rx.button("Brochure", size="4"),
                            rx.link(rx.button("Contact Us", size="4", variant="outline"), href="/contact")
                        ),
                        spacing="4",
                        align_items="flex-start",
                        width="50%",
                    ),
                    # Right side: Image
                    rx.image(
                        src="hero.png",
                        alt="Hero image",
                        width="40%",
                    ),
                    spacing="8",
                    align_items="center",
                    padding="4em",
                ),
                width="100%",
                height="90vh",
                padding="4em",
                style=hero_style,
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.heading("Genomic Valley", color="black", size="6"),
                type_animation(
                    sequence=[
                        'Where Health Meets Technology.',
                        1000,
                        'Where Health Meets Breakthroughs.',
                        1000,
                        'Where Health Meets Precision.',
                        1000,
                        'Where Health Meets Innovation.',
                        1000,
                    ],
                    size="6",
                    style={
                        "color": "gray",
                        "fontSize": "1em",
                    },
                ),
                rx.image(
                    src="hero.png",
                    alt="Hero image",
                    width="100%",
                ),
                rx.hstack(
                    rx.button("Brochure", size="3"),
                    rx.link(rx.button("Contact Us", size="3", variant="outline"), href="/contact")
                ),
                spacing="6",
                align_items="center",
                padding="2em",
                text_align="center",
            )
        )
    )