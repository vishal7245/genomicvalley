import reflex as rx

bg_card_style = {
    "background_color": "rgba(39,162,85,0.5);",
}

quote_style = {
    "font_size": "2em",
    "color": "white",
    "font_weight": "bold",
}

def about_section() -> rx.Component:
    return rx.section(
        rx.desktop_only(
            rx.section(
                rx.vstack(
                    rx.heading("ABOUT US", size="5", weight="bold", margin_bottom="1em", color="green", text_align="center"),
                    rx.heading("Who we are", size="8", weight="medium", color="black", margin_bottom="10px", text_align="center"),
                    rx.box(
                        rx.text.quote(
                            "Taking Care of Your Tomorrow", style=quote_style
                        ),
                        text_align="center"
                    ),
                    rx.hstack(
                        rx.text(
                            "Welcome to Genomic Valley Biotech Limited, where innovation meets expertise to revolutionize healthcare. With a dedicated team boasting over 10 years of experience in Next-Generation Sequencing (NGS), oncology, and Artificial Intelligence (AI), we are at the forefront of integrating advanced technologies into biotechnology and healthcare solutions. Our team comprises highly skilled professionals passionate about utilizing their extensive knowledge to drive forward the fields of oncology research and diagnostics. We are committed to implementing both novel and validated methods, ensuring the delivery of accurate and confident results in our pursuit of better healthcare outcomes.",
                            color="black",
                            padding="1em",
                            size="5",
                            text_align="justify",
                        ),
                        rx.image(
                            src="/about-img.jpg",
                            alt="Genomic Valley Biotech Limited",
                            width="50vw",
                            margin_top="2em",
                            padding="1em",
                        ),
                        margin_top="2em",
                        align_items="center",
                        margin_bottom="2em",
                        spacing="4",
                    ),
                    justify_content="center",
                    align_items="center",
                    width=["100%", "80%"],
                ),
                width="100%",
                display="flex",
                justify_content="center",
                padding="1em"
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.heading("ABOUT US", size="4", weight="bold", margin_bottom="1em", color="green", text_align="center"),
                rx.heading("Who we are", size="6", weight="medium", color="black", margin_bottom="10px", text_align="center"),
                rx.box(
                    rx.text.quote(
                        "Taking Care of Your Tomorrow", style=quote_style
                    ),
                    text_align="center"
                ),
                rx.image(
                    src="/about-img.jpg",
                    alt="Genomic Valley Biotech Limited",
                    width="100%",
                    margin_top="1em",
                    padding="0.5em",
                ),
                rx.text(
                    "Welcome to Genomic Valley Biotech Limited, where innovation meets expertise to revolutionize healthcare. With a dedicated team boasting over 10 years of experience in Next-Generation Sequencing (NGS), oncology, and Artificial Intelligence (AI), we are at the forefront of integrating advanced technologies into biotechnology and healthcare solutions. Our team comprises highly skilled professionals passionate about utilizing their extensive knowledge to drive forward the fields of oncology research and diagnostics. We are committed to implementing both novel and validated methods, ensuring the delivery of accurate and confident results in our pursuit of better healthcare outcomes.",
                    color="black",
                    padding="1em",
                    size="4",
                    text_align="justify",
                ),
                width="100%",
                spacing="4",
                padding="1em",
                align_items="center",
            )
        ),
        style=bg_card_style,
    )