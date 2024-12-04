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

mobile_paragraph_style = {
    "font-size": "1rem",
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

button_style = {
    "background_color": "teal",
    "color": "white",
    "font_size": "1.4rem",
    "padding": "0.75rem 1.5rem",
    "border_radius": "0.5rem",
    "cursor": "pointer",
    "width": "fit-content",
    "margin": "2rem auto",  # Centers the button horizontally
}


@rx.page(route="/rna-fusion", title="RNA Fusion")
def rna_fusion():
    return rx.section(
        rx.html(
        """
                <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-7C0KZ36E1J"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-7C0KZ36E1J');
        </script>
        """    
        ),
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("RNA Fusion"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "RNA fusion events, where two separate genes combine to form a hybrid gene, are significant markers in various cancers and other diseases. Detecting these fusion events is crucial for accurate diagnosis, prognosis, and the development of targeted therapies. Our RNA Fusion services offer specialized solutions to identify, analyze, and interpret these critical genetic alterations.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Fusion Only",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "The Fusion Only service is designed to detect gene fusions exclusively. This focused approach allows for the identification of fusion events that may be driving disease processes, particularly in cancers such as leukemia and solid tumors. By pinpointing these fusions, this service provides valuable insights for targeted therapeutic interventions.",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Applications:",
                                font_weight="bold",
                                margin_top="1rem",
                                margin_bottom="0.5rem",
                                style=paragraph_style
                            ),
                            rx.unordered_list(
                                rx.list_item("Cancer Diagnosis: Identifying specific gene fusions associated with different cancer types."),
                                rx.list_item("Therapeutic Targeting: Informing treatment plans based on fusion-driven disease mechanisms."),
                                rx.list_item("Prognosis: Assessing the impact of gene fusions on disease outcomes."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Fusion, Expression, and SNV",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "The Fusion, Expression, and SNV service expands upon the detection of gene fusions by also analyzing gene expression levels and identifying single nucleotide variants (SNVs). This comprehensive approach provides a broader view of the genetic landscape, offering deeper insights into the molecular underpinnings of diseases.",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Applications:",
                                font_weight="bold",
                                margin_top="1rem",
                                margin_bottom="0.5rem",
                                style=paragraph_style
                            ),
                            rx.unordered_list(
                                rx.list_item("Integrated Analysis: Combining fusion detection with expression profiling and SNV identification for a more complete genetic analysis."),
                                rx.list_item("Personalized Medicine: Informing precision treatment strategies by considering multiple genetic factors."),
                                rx.list_item("Research Applications: Supporting complex research studies by providing multi-dimensional genetic data."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Harness the power of advanced RNA fusion analysis to unlock new possibilities in disease diagnosis and treatment. Whether you need focused fusion detection or a comprehensive genetic analysis, our RNA Fusion services are here to support your research and clinical efforts. Contact Us Today to explore how our RNA Fusion services can enhance your genomic studies and improve patient outcomes.",
                                style=paragraph_style,
                                margin_top="2rem",
                                font_weight="bold",
                            ),
                            rx.button(
                                "Contact Us Today",
                                on_click=rx.redirect("/contact"),
                                style=button_style,
                            )
                        ),
                        width="70vw",
                        p="4",
                        padding="4rem",
                    ),
                    width="100%",
                    justify_content="center",
                    align_items="center"    
                ),
                footer()
            ),
            width="100%",
            padding="0px",
        ),
        rx.mobile_and_tablet(  # Mobile layout
            rx.vstack(
                navbar(),
                banner("RNA Fusion"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "RNA fusion events, where two separate genes combine to form a hybrid gene, are significant markers in various cancers and other diseases. Detecting these fusion events is crucial for accurate diagnosis, prognosis, and the development of targeted therapies. Our RNA Fusion services offer specialized solutions to identify, analyze, and interpret these critical genetic alterations.",
                            style=mobile_paragraph_style,
                        ),
                        # Fusion Only - Mobile
                        rx.heading(
                            "Fusion Only",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "The Fusion Only service is designed to detect gene fusions exclusively. This focused approach allows for the identification of fusion events that may be driving disease processes, particularly in cancers such as leukemia and solid tumors. By pinpointing these fusions, this service provides valuable insights for targeted therapeutic interventions.",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Applications:",
                            font_weight="bold",
                            margin_top="1rem",
                            margin_bottom="0.5rem",
                            style=mobile_paragraph_style
                        ),
                        rx.unordered_list(
                            rx.list_item("Cancer Diagnosis: Identifying specific gene fusions associated with different cancer types."),
                            rx.list_item("Therapeutic Targeting: Informing treatment plans based on fusion-driven disease mechanisms."),
                            rx.list_item("Prognosis: Assessing the impact of gene fusions on disease outcomes."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Fusion, Expression, and SNV - Mobile
                        rx.heading(
                            "Fusion, Expression, and SNV",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "The Fusion, Expression, and SNV service expands upon the detection of gene fusions by also analyzing gene expression levels and identifying single nucleotide variants (SNVs). This comprehensive approach provides a broader view of the genetic landscape, offering deeper insights into the molecular underpinnings of diseases.",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Applications:",
                            font_weight="bold",
                            margin_top="1rem",
                            margin_bottom="0.5rem",
                            style=mobile_paragraph_style
                        ),
                        rx.unordered_list(
                            rx.list_item("Integrated Analysis: Combining fusion detection with expression profiling and SNV identification for a more complete genetic analysis."),
                            rx.list_item("Personalized Medicine: Informing precision treatment strategies by considering multiple genetic factors."),
                            rx.list_item("Research Applications: Supporting complex research studies by providing multi-dimensional genetic data."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Harness the power of advanced RNA fusion analysis to unlock new possibilities in disease diagnosis and treatment. Whether you need focused fusion detection or a comprehensive genetic analysis, our RNA Fusion services are here to support your research and clinical efforts. Contact Us Today to explore how our RNA Fusion services can enhance your genomic studies and improve patient outcomes.",
                            style=mobile_paragraph_style,
                            margin_top="2rem",
                            font_weight="bold",
                        ),
                        rx.button(
                                "Contact Us Today",
                                on_click=rx.redirect("/contact"),
                                style=button_style,
                            )
                    ),
                    width="100%",
                    p="2",
                    padding="2rem",
                ),
                footer(),
                width="100%",
                spacing="2"
            ),
            width="100%",
        ),
        margin="0",
        padding="0",
    )