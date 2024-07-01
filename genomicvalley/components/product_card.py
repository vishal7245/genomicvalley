import reflex as rx

product_card_style = {

    "background-color": "rgba(17, 41, 70, 0.5)",
    "border-radius": "1em",
    "backdrop-filter": "blur(60px)",
}

product_section_bg = {
    "width": "100%",
    "height": "90vh",
    "background-image": "url('/1.jpg')",
    "background-size": "cover",
    "background-position": "center",
}

def product_section():
    return rx.section(
        rx.vstack(
            rx.heading("Product Highlight", size="8", text_align="center"),
            rx.divider(border_color="black", opacity=0.4, border_width="1px", width="50vh"),
            rx.hstack(
                rx.image(src="/12.jpeg", alt="Product Image", width="50%", max_width="50%", max_height="50%"),
                rx.box(
                    rx.vstack(
                        rx.text("This is a brief description of the product. It highlights key features and benefits that will appeal to potential customers."),
                        rx.button("Learn More", bg="blue.500", color="white"),
                        spacing="4",
                        align_items="start",
                    ),
                    bg="gray.100",
                    p="6",
                    border_radius="md",
                    box_shadow="md",
                    width="50%",
                ),
                spacing="8",
                align_items="center",
                margin_top="2em",
                padding="2em",
            ),
            max_width="1200px",
            padding="1em",
            margin="0 auto",
            align_items="center",
            justify_content="center",
            style=product_card_style,
        ),  
        style=product_section_bg     
),