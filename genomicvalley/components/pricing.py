import reflex as rx


icon_box_style = {
    "background_color": "#f9fafb",
}

def feature_item(feature: str, color: str) -> rx.Component:
    return rx.hstack(
        rx.icon(
            "check", color=rx.color("blue", 9), size=21
        ),
        rx.text(feature, size="4", weight="regular", color=color),
    )


def standard_features() -> rx.Component:
    return rx.vstack(
        feature_item("40 credits for image generation", "black"),
        feature_item("Credits never expire" , "black"),
        feature_item("High quality images" , "black"),
        feature_item("Commercial license" , "black"),
        spacing="3",
        width="100%",
        align_items="start",
    )


def popular_features() -> rx.Component:
    return rx.vstack(
        feature_item("250 credits for image generation", "white"),
        feature_item("+30% Extra free credits", "white"),
        feature_item("Credits never expire" , "white"),
        feature_item("High quality images" , "white"),
        feature_item("Commercial license" , "white"),
        spacing="3",
        width="100%",
        align_items="start",
    )
    
standard_card_style = {
    "background_color": "rgba(128,212,148,0.2);",
}

button_style = {
    "background_color": "rgba(8, 132, 132, 0.2);",
    "color": "black",
    "border": "1px solid black",
}


def pricing_card_standard() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "Rs.999",
                    trim="both",
                    size="6",
                    weight="regular",
                    color = "black"
                ),
                width="100%",
                spacing="2",
                align_items="end",
            ),
            height="35px",
            align_items="center",
            justify="between",
            width="100%",
        ),
        rx.text(
            "40 Image Credits",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
            color = "black"
        ),
        standard_features(),
        rx.spacer(),
        rx.button(
            "Purchase",
            size="3",
            variant="outline",
            width="100%",
            style = button_style    
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('green', 5)}",
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
        style = standard_card_style,
    )

popular_card_style = {
    "background_color": "rgba(39,162,85,0.5)",
}

def pricing_card_popular() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "Rs.2999",
                    trim="both",
                    size="6",
                    weight="regular",
                ),
                width="100%",
                spacing="2",
                align_items="end",
            ),
            rx.badge(
                "POPULAR",
                size="2",
                radius="full",
                variant="solid",
                color_scheme="green",
            ),
            align_items="center",
            justify="between",
            height="35px",
            width="100%",
        ),
        rx.text(
            "250 Image Credits",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
        ),
        popular_features(),
        rx.spacer(),
        rx.button(
            "Purchase",
            size="3",
            width="100%",
            color_scheme="green",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('blue', 6)}",
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
        style=popular_card_style,
    )


def pricing_cards() -> rx.Component:
    return rx.flex(
        pricing_card_standard(),
        pricing_card_popular(),
        pricing_card_standard(),
        spacing="4",
        flex_direction=["column", "column", "row"],
        width="100%",
        align_items="center",
        justify_content="center",
    )


def pricing_section() -> rx.Component:
    return rx.section(
        rx.vstack(
            rx.heading("PRICING", size="5", weight="bold", margin_bottom="1em", color="green"),
            rx.heading("Simple pricing", size="8", weight="medium", color="black", margin_bottom="10px"),
            rx.text(
                "Pricing that fits your needs and helps you scale.",
                size="5", align="center", margin_bottom="1em", color="gray"
            ),
            rx.grid(
   
                columns = "3",
                spacing = "5",
                
                ),
            pricing_cards(),
            justift_content="center",
            align_items="center",
            width="100%",
        ),
        width="100%",
    )