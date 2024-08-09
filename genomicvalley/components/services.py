import reflex as rx


icon_box_style = {
    "background_color": "#f9fafb",
}


def card(icon_img: str, title:str, description:str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(icon_img,color="green", size=70, margin="5px"),
                border_radius="10px",
                border="1px solid #e0e0e0",
                style=icon_box_style,
                ),
            rx.heading(title, size="5", margin_bottom="10px", color="black"),
            rx.text(description, color="gray"),
            spacing="4",
            align_items="start",
        ),
        width="350px",
        padding="20px",
        border="1px solid #e0e0e0",
        border_radius="8px",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
        _hover = {
            "background": "#A8F7D4",
        }
    )
    
def mobile_card(icon_img: str, title:str, description:str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.icon(icon_img,color="green", size=70, margin="5px"),
                border_radius="10px",
                border="1px solid #e0e0e0",
                style=icon_box_style,
                ),
            rx.heading(title, size="5", margin_bottom="10px", color="black"),
            rx.text(description, color="gray"),
            spacing="4",
            align_items="start",
        ),
        width="90vw",
        padding="20px",
        border="1px solid #e0e0e0",
        border_radius="8px",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
        _hover = {
            "background": "#A8F7D4",
        }
    )

def services_section() -> rx.Component:
    return rx.section(
        rx.desktop_only(
            rx.section(
        rx.vstack(
            rx.box(
                rx.heading("SERVICES", size="5", weight="bold", margin_bottom="1em", color="green", align="center"),
                width="100%",
            ),
            rx.heading("Empowering healthcare with NGS and AI", size="8", weight="medium", color="black", margin_bottom="10px",),
            rx.box(rx.text(
                "We offer advanced Diagnostic Services using Next-Generation Sequencing (NGS) and AI for precise genetic analysis and personalized oncology treatments. Our Research Services drive innovation in oncology through NGS and AI, enhancing diagnostic tools and therapeutic strategies.",
                size="5", align="center", margin_bottom="1em", color="gray"
            ),width="60%"),
            rx.grid(
                card("heart-pulse", "Personalized Healthcare", "Personalized healthcare at Genomic Valley Bharat Pvt. Ltd. is centered on tailoring medical treatment to individual patients based on their unique genetic profiles."),
                card("dna", "Genetic Disease Predisposition", "Our genetic disease predisposition services focus on identifying individuals' susceptibility to various hereditary conditions."),
                card("hospital", "Community Health Support", "Community health support at Genomic Valley Bharat Pvt. Ltd. aims to improve public health outcomes through comprehensive genomic screening programs."),
                card("brain", "AI-Based Genome Healthcare", "At Genomic Valley Bharat Pvt. Ltd. , we are pioneering AI-based genome healthcare research to revolutionize the way genetic data is analyzed and interpreted."),
                card("circle-fading-plus", "Metagenomics and Healthcare", "Our metagenomics research focuses on studying the collective genomes of microbial communities within the human body and their impact on health and disease."),
                card("microscope", "Extramural Research Project", "Our extramural research projects involve collaborating with external academic institutions, research organizations, and industry partners to advance genomic science."),
                columns = "3",
                spacing = "5",
                
                ),
            justift_content="center",
            align_items="center",
            width="100%",
        ),
        width="100%",
    )
            ),
        rx.mobile_and_tablet(
            rx.mobile_and_tablet(
            rx.vstack(
                rx.box(
                    rx.heading("SERVICES", size="5", weight="bold", margin_bottom="1em", color="green", align="center"),
                    width="100%",
                ),
                rx.heading("Empowering healthcare with NGS and AI", size="6", weight="medium", color="black", margin_bottom="10px", align="center"),
                rx.box(
                    rx.text(
                        "We offer advanced Diagnostic Services using Next-Generation Sequencing (NGS) and AI for precise genetic analysis and personalized oncology treatments. Our Research Services drive innovation in oncology through NGS and AI, enhancing diagnostic tools and therapeutic strategies.",
                        size="4",
                        align="center",
                        margin_bottom="1em",
                        color="gray"
                    ),
                    width="90%"
                ),
                rx.vstack(
                    mobile_card("heart-pulse", "Personalized Healthcare", "Personalized healthcare at Genomic Valley Bharat Pvt. Ltd. is centered on tailoring medical treatment to individual patients based on their unique genetic profiles."),
                    mobile_card("dna", "Genetic Disease Predisposition", "Our genetic disease predisposition services focus on identifying individuals' susceptibility to various hereditary conditions."),
                    mobile_card("hospital", "Community Health Support", "Community health support at Genomic Valley Bharat Pvt. Ltd. aims to improve public health outcomes through comprehensive genomic screening programs."),
                    mobile_card("brain", "AI-Based Genome Healthcare", "At Genomic Valley Bharat Pvt. Ltd. , we are pioneering AI-based genome healthcare research to revolutionize the way genetic data is analyzed and interpreted."),
                    mobile_card("circle-fading-plus", "Metagenomics and Healthcare", "Our metagenomics research focuses on studying the collective genomes of microbial communities within the human body and their impact on health and disease."),
                    mobile_card("microscope", "Extramural Research Project", "Our extramural research projects involve collaborating with external academic institutions, research organizations, and industry partners to advance genomic science."),
                    spacing="4",
                    width="100%",
                ),
                justify_content="center",
                align_items="center",
                width="100%",
                padding="1em",
            )
        )
        )
    )