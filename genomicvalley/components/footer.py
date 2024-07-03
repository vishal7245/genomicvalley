import reflex as rx


    


def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3", color="black"), href=href)


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "Quick Links", size="4", weight="bold", as_="h3", color="black"
        ),
        footer_item("About us", "/about"),
        footer_item("Our Vision", "/about"),
        footer_item("Our Team", "/about"),
        footer_item("Contact", "/contact"),
        footer_item("FAQs", "/faq"),
        spacing="4",
        text_align="center",
        align_items="center",
        flex_direction="column",
    )

def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            "Services", size="4", weight="bold", as_="h3", color="black"
        ),
        footer_item("Personalized Healthcare", "/diagnostic-services"),
        footer_item("Genetic Disease Predisposition", "/diagnostic-services"),
        footer_item("Community Health Support", "/diagnostic-services"),
        footer_item("AI-Based Genome Healthcare", "/research-services"),
        footer_item("Metagenomics and Healthcare", "/research-services"),
        footer_item("Extramural Research Project", "/research-services"),
        spacing="4",
        text_align="center",
        align_items="center",
        flex_direction="column",
    )


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon, color="black"), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify="end",
        width="100%",
    )
               
footer_style = {
    "background_color": "rgba(39,162,85,0.5);",
    "width": "100%",
    "padding": "3em",
    "border_top": "1px solid black",
}
divier_style = {
    "background_color": "black",
    "height": "1px",
    "width": "100%",
}


def footer() -> rx.Component:
    return rx.section(
        rx.desktop_only(
                        rx.el.footer(
                rx.vstack(
                    rx.flex(
                        rx.vstack(
                            rx.hstack(
                                rx.heading(
                                    "Genomic Valley Biotech Ltd.",
                                    size="7",
                                    weight="bold",
                                    color="black",
                                ),
                                align_items="center",
                            ),
                            rx.box(
                                rx.text(
                                    "4 KM Stone, Berri Chhara Road, P.O. Tanda Heri, Tehsil Bahadurgarh, District Jhajjar, HARYANA, INDIA - 124 507",
                                    size="3",
                                    weight="medium",
                                    color="black",
                                ),
                                width="450px"
                            ),
                            spacing="4",
                            align_items=[
                                "center",
                                "center",
                                "start",
                            ],
                            width="50%"
                        ),
                        footer_items_1(),
                        footer_items_2(),
                        justify="between",
                        spacing="6",
                        flex_direction=["column", "column", "row"],
                        width="100%",
                    ),
                    rx.divider(border_color="black", opacity=0.4, border_width="1px"),
                    spacing="5",
                    width="100%",
                ),
                style=footer_style,
            )
        ),
        rx.mobile_and_tablet(
            rx.el.footer(
                rx.vstack(
                    rx.vstack(
                        rx.heading(
                            "Genomic Valley Biotech Ltd.",
                            size="6",
                            weight="bold",
                            color="black",
                            text_align="center",
                        ),
                        rx.text(
                            "4 KM Stone, Berri Chhara Road, P.O. Tanda Heri, Tehsil Bahadurgarh, District Jhajjar, HARYANA, INDIA - 124 507",
                            size="2",
                            weight="medium",
                            color="black",
                            text_align="center",
                        ),
                        spacing="3",
                        align_items="center",
                        width="100%",
                    ),
                    footer_items_1(),
                    footer_items_2(),
                    rx.divider(border_color="black", opacity=0.4, border_width="1px"),
                    spacing="6",
                    width="100%",
                    align_items="center",
                ),
                style=footer_style,
            )
        ),
        width="100%",
        padding="0px",
    )