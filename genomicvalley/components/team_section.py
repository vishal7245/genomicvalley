import reflex as rx
from genomicvalley.components.profiles import yogesh_agrawal_profile
from genomicvalley.components.profiles import romasha_gupta_profile
from genomicvalley.components.profiles import sanjoy_gupta_profile
from genomicvalley.components.profiles import vipul_garg_profile

standard_card_style = {
    "background_color": "rgba(128,212,148,0.2)",
    "border_radius": "10px",
    "border": "1px solid #E2E8F0",
    "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
}

image_style = {
    "width": "250px",
    "height": "250px",
    "border_radius": "50%",  # This makes the image circular
    "object_fit": "cover",
}

dialog_style = {
    "width": "900px",  # Increased from 700px to 900px
    "max-width": "90vw",  # Added to ensure it doesn't exceed viewport width on smaller screens
    "height": "80vh",  # Added to make it taller, using 80% of the viewport height
    "max-height": "800px",  # Added a maximum height
}

def profile_card(image_url: str, name: str, designation: str, dialog_content: rx.Component = None):
    return rx.box(
        rx.vstack(
            rx.image(
                src=image_url,
                style= image_style
            ),
            rx.text(name, font_size="1.5em", font_weight="bold", color="black"),
            rx.text(designation, color="gray"),
            rx.dialog.root(
                rx.dialog.trigger(rx.button("Profile", color_scheme="teal", size="3"),),
                rx.dialog.content(
                    rx.dialog.description(
                        dialog_content,
                    ),
                    rx.dialog.close(
                        rx.button("Close", size="3"), margin_top="2rem"
                    ),
                    style=dialog_style,
                ),
            ),
            spacing="4",
            align_items="center",
            padding="3em",
            border="1px solid #E2E8F0",
        ),
            style=standard_card_style
    )
    


def open_profile() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Open Dialog")),
        rx.dialog.content(
            rx.dialog.title("Mr. Yogesh Agrawal"),
            rx.dialog.description(
                yogesh_agrawal_profile(),
            ),
            rx.dialog.close(
                rx.button("Close", size="3"), margin_top="2rem"
            ),
            style=dialog_style,
        ),
    )
    
def team_section() -> rx.Component:
    return rx.section(
        rx.desktop_only(
            rx.section(
                rx.vstack(
                    rx.heading("OUR TEAM", size="5", weight="bold", margin_bottom="1em", color="green"),
                    rx.heading("Taking care of your tomorrow", size="8", weight="medium", color="black", margin_bottom="10px"),
                    rx.text(
                        "Here's what our clients around the internet are saying about us.",
                        size="5", align="center", margin_bottom="1em", color="gray"
                    ),
                    rx.grid(
                        profile_card("/ya.jpeg", "Mr. Yogesh Agrawal", "Chairman", yogesh_agrawal_profile()),
                        profile_card("/vg.jpg", "Mr. Vipul Garg", "Executive Assistant to MD", vipul_garg_profile()),
                        profile_card("/sg.jpg", "Mr. Sanjoy Gupta", "General Manager", sanjoy_gupta_profile()),
                        profile_card("/rg.jpeg", "Ms. Romasha Gupta", "Project Manager", romasha_gupta_profile()),
                        columns = "4",
                        spacing = "3",
                        
                        ),
                    justift_content="center",
                    align_items="center",
                    width="100%",
                ),
                width="100%",
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.heading("OUR TEAM", size="4", weight="bold", margin_bottom="1em", color="green", id="our-team"),
                rx.heading("Taking care of your tomorrow", size="6", weight="medium", color="black", margin_bottom="10px"),
                rx.text(
                    "Here's what our clients around the internet are saying about us.",
                    size="4", align="center", margin_bottom="1em", color="gray"
                ),
                rx.vstack(
                    profile_card("/ya.jpeg", "Mr. Yogesh Agrawal", "Chairman", yogesh_agrawal_profile()),
                    profile_card("/vg.jpg", "Mr. Vipul Garg", "Executive Assistant to MD", vipul_garg_profile()),
                    profile_card("/sg.jpg", "Mr. Sanjoy Gupta", "General Manager", sanjoy_gupta_profile()),
                    profile_card("/rg.jpeg", "Ms. Romasha Gupta", "Project Manager", romasha_gupta_profile()),
                    spacing="4",
                    width="100%",
                ),
                justify_content="center",
                align_items="center",
                width="100%",
                padding="1em",
            ),
            width="100%",
            margin_bottom="3em",
        ),
        width="100%",
    )
    
