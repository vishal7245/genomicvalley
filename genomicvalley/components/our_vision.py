import reflex as rx

bg_card_style = {
    "background_color": "white",
}

quote_style = {
    "font_size": "2em",
    "color": "white",
    "font_weight": "bold",
}


def vision_section() -> rx.Component:
    return rx.section(
        rx.desktop_only(
            rx.section(
                rx.vstack(
                    rx.heading(
                        "OUR VISION",
                        size="5",
                        weight="bold",
                        margin_bottom="1em",
                        color="green",
                        text_align="center",
                    ),
                    rx.heading(
                        "See where we are going",
                        size="8",
                        weight="medium",
                        color="black",
                        margin_bottom="10px",
                        text_align="center",
                    ),
                    rx.box(
                        rx.text.quote(
                            "Taking Care of Your Tomorrow", style=quote_style
                        ),
                        text_align="center",
                    ),
                    rx.hstack(
                        rx.image(
                            src="/c4.png",
                            alt="Genomic Valley",
                            width="40vw",
                            margin_top="2em",
                            padding="1em",
                        ),
                        rx.vstack(
                            rx.text(
                                "At Genomic Valley, our vision is to propel molecular diagnostics into a new era of precision and efficiency through the integration of novel AI-based approaches. We are dedicated to advancing modern healthcare by offering more accurate diagnostics, backed by comprehensive metadata, delivered in significantly less time. Our goal is to provide personalized therapy options, empowering doctors with robust support for decision-making and enabling the identification of effective treatment options. By harnessing the power of AI and IT, we aim to transform oncology research and diagnostics, ensuring that patients receive the most precise and timely care possible.",
                                color="black",
                                padding="1em",
                                size="5",
                                text_align="justify",
                            ),
                            rx.text(
                                "We envision a future where cutting-edge technology and human expertise converge to revolutionize the landscape of molecular diagnostics. Our commitment to innovation and excellence drives us to continuously explore and implement advanced methods, ultimately improving patient outcomes and contributing to the advancement of global healthcare. We are committed to providing comprehensive Research Process Outsourcing (RPO) services tailored to global researchers. With a dedicated team of experts and access to professional software tools, we ensure refined data analysis and deliver optimal solutions. Our services aim to empower researchers worldwide by enhancing their projects with advanced analytical capabilities and meticulous attention to detail.",
                                color="black",
                                padding="1em",
                                size="5",
                                text_align="justify",
                            ),
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
                padding="1em",
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.heading(
                    "ABOUT US",
                    size="4",
                    weight="bold",
                    margin_bottom="1em",
                    color="green",
                    text_align="center",
                ),
                rx.heading(
                    "Who we are",
                    size="6",
                    weight="medium",
                    color="black",
                    margin_bottom="10px",
                    text_align="center",
                ),
                rx.box(
                    rx.text.quote("Taking Care of Your Tomorrow", style=quote_style),
                    text_align="center",
                ),
                rx.image(
                    src="/about-img.jpg",
                    alt="Genomic Valley",
                    width="100%",
                    margin_top="1em",
                    padding="0.5em",
                ),
                rx.text(
                    "Welcome to Genomic Valley, where innovation meets expertise to revolutionize healthcare. With a dedicated team boasting over 10 years of experience in Next-Generation Sequencing (NGS), oncology, and Artificial Intelligence (AI), we are at the forefront of integrating advanced technologies into biotechnology and healthcare solutions. Our team comprises highly skilled professionals passionate about utilizing their extensive knowledge to drive forward the fields of oncology research and diagnostics. We are committed to implementing both novel and validated methods, ensuring the delivery of accurate and confident results in our pursuit of better healthcare outcomes.",
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
