import reflex as rx


from genomicvalley.components.footer import footer
from genomicvalley.components.navbar_2 import navbar_white as navbar
from genomicvalley.components.banner import banner


paragraph_style = {
    "font-size": "1.2rem",
    "color": "gray",
    "margin-bottom": "1rem",
    "text-align": "justify",
}


image_style = {
    "width": "75%",
    "height": "auto",
    "object-fit": "cover",
    "margin-bottom": "1rem",
}

mobile_paragraph_style = {
    "font-size": "1rem",
    "color": "gray",
    "margin-bottom": "1rem",
    "text-align": "justify",
}

image_urls = [
    "/Personalized Healthcare.jpg",
    "/Genetic Disease Predisposition.jpg",
    "/Community Health Support.jpg",
]


@rx.page(route="/diagnostic-services", title="Diagnostic Services")
def diagnostic_services():
    return rx.section(
        rx.desktop_only(
            rx.vstack(
                navbar(),
                banner("Diagnostic Services"),
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.vstack(
                                rx.text(
                                    "At Genomic Valley Biotech Limited, our diagnostic services harness the power of Next-Generation Sequencing (NGS) to deliver unparalleled precision in identifying genetic mutations and abnormalities. By integrating advanced AI technologies, we provide rapid and accurate molecular diagnostics, enabling early detection and personalized treatment plans for oncology patients. Our commitment to leveraging cutting-edge NGS ensures that healthcare providers have access to comprehensive and reliable data, empowering them to make informed decisions and improve patient outcomes.",
                                    style=paragraph_style,
                                ),
                                rx.heading(
                                    "Personalized Healthcare",
                                    size="9",
                                    margin_top="2rem",
                                    margin_bottom="1rem",
                                    color="teal",
                                    font_weight="bold",
                                ),
                                rx.text(
                                    "Personalized healthcare at Genomic Valley Biotech Limited is centered on tailoring medical treatment to individual patients based on their unique genetic profiles. Utilizing Next-Generation Sequencing (NGS) and advanced AI technologies, we provide precise diagnostics that enable healthcare providers to design customized treatment plans. This approach enhances the effectiveness of therapies, minimizes adverse effects, and ensures that each patient receives the most suitable care for their specific genetic makeup.",
                                    style=paragraph_style,
                                ),
                                rx.heading(
                                    "Genetic Disease Predisposition",
                                    size="9",
                                    margin_top="2rem",
                                    margin_bottom="1rem",
                                    color="teal",
                                    font_weight="bold",
                                ),
                                rx.text(
                                    "Our genetic disease predisposition services focus on identifying individuals' susceptibility to various hereditary conditions. By analyzing genetic markers through NGS, we can predict the likelihood of developing certain diseases, allowing for early interventions and proactive healthcare measures. This service empowers patients and healthcare professionals to make informed decisions about lifestyle changes, monitoring, and preventive strategies to mitigate the risk of genetic diseases.",
                                    style=paragraph_style,
                                ),
                                rx.heading(
                                    "Community Health Support",
                                    size="9",
                                    margin_top="2rem",
                                    margin_bottom="1rem",
                                    color="teal",
                                    font_weight="bold",
                                ),
                                rx.text(
                                    "Community health support at Genomic Valley Biotech Limited aims to improve public health outcomes through comprehensive genomic screening programs. By integrating NGS and AI, we offer population-wide genetic testing to identify prevalent health risks and tailor community health initiatives accordingly. This service supports public health agencies and organizations in designing effective health programs, improving disease prevention, and enhancing the overall well-being of the community.",
                                    style=paragraph_style,
                                ),
                            ),
                            width="60vw",
                            p="4",
                            padding="4rem",
                        ),
                        rx.box(
                            rx.vstack(
                                *[
                                    rx.image(src=url, style=image_style)
                                    for url in image_urls
                                ],
                            ),
                            width="40vw",
                            p="4",
                            padding="4rem",
                        ),
                        width="100vw",
                        spacing="0",
                        left="0",
                    ),
                    width="100%",
                    overflow="hidden",
                ),
                footer(),
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                navbar(),
                banner("Diagnostic Services"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "At Genomic Valley Biotech Limited, our diagnostic services harness the power of Next-Generation Sequencing (NGS) to deliver unparalleled precision in identifying genetic mutations and abnormalities. By integrating advanced AI technologies, we provide rapid and accurate molecular diagnostics, enabling early detection and personalized treatment plans for oncology patients. Our commitment to leveraging cutting-edge NGS ensures that healthcare providers have access to comprehensive and reliable data, empowering them to make informed decisions and improve patient outcomes.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Personalized Healthcare",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                            id="personalized-healthcare",
                        ),
                        rx.text(
                            "Personalized healthcare at Genomic Valley Biotech Limited is centered on tailoring medical treatment to individual patients based on their unique genetic profiles. Utilizing Next-Generation Sequencing (NGS) and advanced AI technologies, we provide precise diagnostics that enable healthcare providers to design customized treatment plans. This approach enhances the effectiveness of therapies, minimizes adverse effects, and ensures that each patient receives the most suitable care for their specific genetic makeup.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Genetic Disease Predisposition",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                            id="genetic-disease-predisposition",
                        ),
                        rx.text(
                            "Our genetic disease predisposition services focus on identifying individuals' susceptibility to various hereditary conditions. By analyzing genetic markers through NGS, we can predict the likelihood of developing certain diseases, allowing for early interventions and proactive healthcare measures. This service empowers patients and healthcare professionals to make informed decisions about lifestyle changes, monitoring, and preventive strategies to mitigate the risk of genetic diseases.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Community Health Support",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                            id="community-health-support",
                        ),
                        rx.text(
                            "Community health support at Genomic Valley Biotech Limited aims to improve public health outcomes through comprehensive genomic screening programs. By integrating NGS and AI, we offer population-wide genetic testing to identify prevalent health risks and tailor community health initiatives accordingly. This service supports public health agencies and organizations in designing effective health programs, improving disease prevention, and enhancing the overall well-being of the community.",
                            style=mobile_paragraph_style,
                        ),
                        rx.vstack(
                            *[
                                rx.image(src=url, style=image_style)
                                for url in image_urls
                            ],
                            width="100%",
                            spacing="4",
                            padding="1rem",
                        ),
                    ),
                    width="100%",
                    p="4",
                    padding="2rem",
                ),
                footer(),
                width="100%",
                spacing="4",
            ),
            width="100%",
        ),
        width="100%",
        margin="0",
        padding="0",
    )
