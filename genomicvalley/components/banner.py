import reflex as rx

banner_style = {
    "width": "100%",
    "height": "60vh",
    "background-color": "hsla(231,0%,100%,1)",
    "background-image": "url('/banner-bg.jpg')",
    "background-size": "cover",
    "background-position": "center",
    "display": "flex",  # Added display flex
    "justify-content": "center",  # Center horizontally
    "align-items": "center",  # Center vertically
    "border_bottom": "1px solid black",

}

banner_card_style = {
    "padding": "2em",
    "border_radius": "1em",
    "backdrop-filter": "blur(60px)",
    "display": "inline-block",
    "max-width": "80%",
}


font_size = {
    "font_size": "4em",
    "color": "black",
    "padding": "30px",
}

mobile_font_size = {
    "font_size": "1em",
    "color": "black",
    "padding": "10px",
}

def banner(heading: str) -> rx.Component:
    return rx.section(
        rx.desktop_only(
            rx.section(
                rx.box(
                    rx.heading(heading, style=font_size),
                    style=banner_card_style
                ),
                style=banner_style, 
            )
        ),
        rx.mobile_and_tablet(
            rx.section(
                rx.box(
                    rx.heading(heading, style=mobile_font_size),
                    style=banner_card_style
                ),
                style=banner_style, 
            )
        ),
        width="100%",
    )
