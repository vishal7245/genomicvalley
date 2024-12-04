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


@rx.page(route="/pan-cancer-studies", title="Pan-Cancer Studies")
def pan_cancer_studies():
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
                banner("Pan-Cancer Studies"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Pan-Cancer Studies service offers a comprehensive and integrated approach to understanding cancer through the analysis of diverse cancer types simultaneously. By employing advanced genomic, transcriptomic, and bioinformatics techniques, we provide valuable insights into the common and unique molecular features of various cancers, helping to drive breakthroughs in diagnosis, treatment, and prevention.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Pan-Cancer Studies?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Integrated Cancer Insights: Our pan-cancer studies analyze multiple cancer types in a unified framework, revealing shared and distinct molecular pathways, genetic alterations, and biomarkers across different cancers."),
                                rx.list_item("Identification of Common Biomarkers: By examining a broad spectrum of cancers, we identify common biomarkers and genetic signatures that can be used for early detection, diagnosis, and monitoring of cancer progression."),
                                rx.list_item("Cross-Cancer Comparisons: Gain insights into how different cancers compare at the molecular level, including similarities in mutation patterns, gene expression profiles, and response to therapies. This comparative analysis can reveal new targets for treatment and improve understanding of cancer biology."),
                                rx.list_item("Support for Personalized Medicine: Our studies help identify genetic and molecular profiles that influence individual responses to treatment, supporting the development of personalized therapeutic strategies and improving patient outcomes."),
                                rx.list_item("Advancement of Research: Contribute to the development of new cancer therapies and diagnostic tools by leveraging comprehensive data across multiple cancer types, facilitating novel research discoveries and innovations."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Who Can Benefit?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Researchers: Utilize our pan-cancer data to explore cancer biology, identify new therapeutic targets, and contribute to the development of innovative cancer treatments."),
                                rx.list_item("Oncologists & Healthcare Providers: Access integrated cancer insights to enhance diagnostic accuracy, tailor treatment plans, and improve patient care based on a broader understanding of cancer mechanisms."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Leverage our comprehensive cancer data to support drug discovery, clinical trials, and the development of targeted therapies that address multiple cancer types."),
                                rx.list_item("Public Health Authorities: Use the insights from our pan-cancer studies to inform cancer prevention strategies, monitor trends, and allocate resources for cancer research and treatment."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Our Process",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Sample Collection & Preparation: We provide guidelines for collecting and preparing cancer samples to ensure high-quality data for pan-cancer analysis."),
                                rx.list_item("Omics Analysis: Employing cutting-edge techniques such as next-generation sequencing (NGS), transcriptomics, and proteomics, we analyze genetic, transcriptomic, and protein-level data across various cancer types."),
                                rx.list_item("Bioinformatics & Data Integration: Our expert bioinformatics team integrates and analyzes multi-dimensional data to identify key molecular features, commonalities, and differences among cancer types."),
                                rx.list_item("Detailed Reporting: Receive comprehensive reports that include insights into common and unique molecular features, potential biomarkers, and recommendations for further research or clinical application."),
                                rx.list_item("Consultation & Support: Our team of experts is available to discuss findings, interpret results, and provide guidance on the implications for research, treatment, and patient care."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Commitment to Excellence",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "We are dedicated to delivering high-quality, actionable insights through rigorous analysis and advanced technologies. Our Pan-Cancer Studies service provides a holistic view of cancer, driving forward research and improving patient outcomes through integrated molecular understanding.",
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
                banner("Pan-Cancer Studies"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Pan-Cancer Studies service offers a comprehensive and integrated approach to understanding cancer through the analysis of diverse cancer types simultaneously. By employing advanced genomic, transcriptomic, and bioinformatics techniques, we provide valuable insights into the common and unique molecular features of various cancers, helping to drive breakthroughs in diagnosis, treatment, and prevention.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Pan-Cancer Studies? - Mobile
                        rx.heading(
                            "Why Choose Pan-Cancer Studies?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Integrated Cancer Insights: Our pan-cancer studies analyze multiple cancer types in a unified framework, revealing shared and distinct molecular pathways, genetic alterations, and biomarkers across different cancers."),
                            rx.list_item("Identification of Common Biomarkers: By examining a broad spectrum of cancers, we identify common biomarkers and genetic signatures that can be used for early detection, diagnosis, and monitoring of cancer progression."),
                            rx.list_item("Cross-Cancer Comparisons: Gain insights into how different cancers compare at the molecular level, including similarities in mutation patterns, gene expression profiles, and response to therapies. This comparative analysis can reveal new targets for treatment and improve understanding of cancer biology."),
                            rx.list_item("Support for Personalized Medicine: Our studies help identify genetic and molecular profiles that influence individual responses to treatment, supporting the development of personalized therapeutic strategies and improving patient outcomes."),
                            rx.list_item("Advancement of Research: Contribute to the development of new cancer therapies and diagnostic tools by leveraging comprehensive data across multiple cancer types, facilitating novel research discoveries and innovations."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Who Can Benefit? - Mobile
                        rx.heading(
                            "Who Can Benefit?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Researchers: Utilize our pan-cancer data to explore cancer biology, identify new therapeutic targets, and contribute to the development of innovative cancer treatments."),
                            rx.list_item("Oncologists & Healthcare Providers: Access integrated cancer insights to enhance diagnostic accuracy, tailor treatment plans, and improve patient care based on a broader understanding of cancer mechanisms."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Leverage our comprehensive cancer data to support drug discovery, clinical trials, and the development of targeted therapies that address multiple cancer types."),
                            rx.list_item("Public Health Authorities: Use the insights from our pan-cancer studies to inform cancer prevention strategies, monitor trends, and allocate resources for cancer research and treatment."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Our Process - Mobile
                        rx.heading(
                            "Our Process",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Sample Collection & Preparation: We provide guidelines for collecting and preparing cancer samples to ensure high-quality data for pan-cancer analysis."),
                            rx.list_item("Omics Analysis: Employing cutting-edge techniques such as next-generation sequencing (NGS), transcriptomics, and proteomics, we analyze genetic, transcriptomic, and protein-level data across various cancer types."),
                            rx.list_item("Bioinformatics & Data Integration: Our expert bioinformatics team integrates and analyzes multi-dimensional data to identify key molecular features, commonalities, and differences among cancer types."),
                            rx.list_item("Detailed Reporting: Receive comprehensive reports that include insights into common and unique molecular features, potential biomarkers, and recommendations for further research or clinical application."),
                            rx.list_item("Consultation & Support: Our team of experts is available to discuss findings, interpret results, and provide guidance on the implications for research, treatment, and patient care."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Commitment to Excellence - Mobile
                        rx.heading(
                            "Commitment to Excellence",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "We are dedicated to delivering high-quality, actionable insights through rigorous analysis and advanced technologies. Our Pan-Cancer Studies service provides a holistic view of cancer, driving forward research and improving patient outcomes through integrated molecular understanding.",
                            style=mobile_paragraph_style,
                            margin_top="1rem",
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