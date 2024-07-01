import reflex as rx
import json,ast

hero_style = {
    "width": "100%",
    "height": "90vh",
    "background-color":"hsla(231,0%,100%,1);",
    "background-image":
""" linear-gradient(
  35deg,
  hsl(149deg 87% 94%) 0%,
  hsl(152deg 75% 90%) 28%,
  hsl(153deg 70% 85%) 44%,
  hsl(155deg 67% 81%) 57%,
  hsl(156deg 65% 77%) 73%,
  hsl(157deg 64% 72%) 100%
);""",
"box-shadow": "0 10px 20px rgba(0, 0, 0, 0.3), 0 6px 6px rgba(0, 0, 0, 0.23);",
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
    "background_image": "url('bg-hero.jpeg')",
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
    "font_size": "7em",
    "margin_bottom": "0.5em",
}

def hero():
    return rx.box(
        rx.hstack(
            # Left side: Main text and button
            rx.vstack(
                rx.heading("Genomic Valley", color="black", style=heading_font),
                type_animation(
                    sequence=[
                        'Where Health Meets Technology',
                        1000, 
                        'Where Health Meets Breakthroughs',
                        1000,
                        'Where Health Meets Precision',
                        1000,
                        'Where Health Meets Innovation',
                        1000,
                    ],
                    size = "9",
                    style = {
                        "color": "gray",
                        "fontSize": "3em",
                    },
                ),
                rx.hstack(
                    rx.button("Get Started", size="4"),
                    rx.button("Contact Us", size="4", variant="outline"),
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
        background="gray.100",
        height="90vh",
        padding="4em",
        style=hero_style,
    )