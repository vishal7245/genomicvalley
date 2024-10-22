import reflex as rx


icon_box_style = {
    "background_color": "#f9fafb",
}


def card(
    name: str,
    id: str,
    testimonial: str,
) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.avatar(fallback=name.upper()[0:2], color_scheme="green", size="5"),
                rx.vstack(
                    rx.heading(
                        name,
                        size="5",
                        color="black",
                    ),
                    rx.text(
                        id,
                        color="gray",
                    ),
                    margin_left="10px",
                ),
            ),
            rx.text.quote(testimonial, color="gray"),
            spacing="4",
            align_items="start",
        ),
        width="350px",
        padding="20px",
        border="1px solid #e0e0e0",
        border_radius="8px",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
        _hover={
            "background": "#E5E4E2",
        },
    )


def mobile_card(
    name: str,
    id: str,
    testimonial: str,
) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.avatar(fallback=name.upper()[0:2], color_scheme="green", size="5"),
                rx.vstack(
                    rx.heading(
                        name,
                        size="5",
                        color="black",
                    ),
                    rx.text(
                        id,
                        color="gray",
                    ),
                    margin_left="10px",
                ),
            ),
            rx.text.quote(testimonial, color="gray"),
            spacing="4",
            align_items="start",
        ),
        width="100%",
        padding="20px",
        border="1px solid #e0e0e0",
        border_radius="8px",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
        _hover={
            "background": "#E5E4E2",
        },
    )


def testimonials_section() -> rx.Component:
    return rx.section(
        rx.desktop_only(
            rx.section(
                rx.vstack(
                    rx.heading(
                        "TESTIMONIALS",
                        size="5",
                        weight="bold",
                        margin_bottom="1em",
                        color="green",
                    ),
                    rx.heading(
                        "What our users say",
                        size="8",
                        weight="medium",
                        color="black",
                        margin_bottom="10px",
                    ),
                    rx.text(
                        "Here's what our clients around the internet are saying about us.",
                        size="5",
                        align="center",
                        margin_bottom="1em",
                        color="gray",
                    ),
                    rx.grid(
                        card(
                            "Amit",
                            "@DrAmit",
                            "Genomic Valley Bharat will be a trailblazer in integrating Next-Generation Sequencing and AI into healthcare. Their expertise and commitment to innovation will be evident in the precision and reliability of their diagnostic services. As a healthcare provider, I will trust their data and solutions to enhance patient outcomes and support informed decision-making.",
                        ),
                        card(
                            "Mohit",
                            "@DrMohit",
                            "Genomic Valley Bharat will be transformative. Their advanced AI-based genome healthcare research will provide us with invaluable insights into genetic patterns, driving innovation in our personalized medicine approaches. Their dedication to excellence and cutting-edge technology will be truly commendable.",
                        ),
                        card(
                            "Shikha",
                            "@DrShikha",
                            "The personalized healthcare services at Genomic Valley Bharat will revolutionize our approach to patient care. By tailoring treatments based on unique genetic profiles, they will ensure our patients receive the most effective therapies with minimal adverse effects. Their expertise in NGS and AI will be unmatched, making them an invaluable partner in our healthcare journey.",
                        ),
                        columns="3",
                        spacing="5",
                    ),
                    justify_content="center",
                    align_items="center",
                    width="100%",
                ),
                width="100%",
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.box(
                    rx.heading(
                        "TESTIMONIALS",
                        size="5",
                        weight="bold",
                        margin_bottom="1em",
                        color="green",
                        align="center",
                    ),
                    width="100%",
                ),
                rx.heading(
                    "What our users say",
                    size="6",
                    weight="medium",
                    color="black",
                    margin_bottom="10px",
                    align="center",
                ),
                rx.box(
                    rx.text(
                        "Here's what our clients around the internet are saying about us.",
                        size="4",
                        align="center",
                        margin_bottom="1em",
                        color="gray",
                    ),
                    width="90%",
                ),
                rx.vstack(
                    mobile_card(
                        "Amit",
                        "@DrAmit",
                        "Genomic Valley Bharat will be a trailblazer in integrating Next-Generation Sequencing and AI into healthcare. Their expertise and commitment to innovation will be evident in the precision and reliability of their diagnostic services. As a healthcare provider, I will trust their data and solutions to enhance patient outcomes and support informed decision-making.",
                    ),
                    mobile_card(
                        "Mohit",
                        "@DrMohit",
                        "Genomic Valley Bharat will be transformative. Their advanced AI-based genome healthcare research will provide us with invaluable insights into genetic patterns, driving innovation in our personalized medicine approaches. Their dedication to excellence and cutting-edge technology will be truly commendable.",
                    ),
                    mobile_card(
                        "Shikha",
                        "@DrShikha",
                        "The personalized healthcare services at Genomic Valley Bharat will revolutionize our approach to patient care. By tailoring treatments based on unique genetic profiles, they will ensure our patients receive the most effective therapies with minimal adverse effects. Their expertise in NGS and AI will be unmatched, making them an invaluable partner in our healthcare journey.",
                    ),
                    spacing="4",
                    width="100%",
                ),
                justify_content="center",
                align_items="center",
                width="100%",
                padding="1em",
            )
        ),
        width="100%",
    )
