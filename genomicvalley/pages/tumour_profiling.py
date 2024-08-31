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

@rx.page(route="/tumor-profiling", title="Tumor Profiling")
def tumor_profiling():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Tumor Profiling"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Tumor Profiling service offers comprehensive genomic and molecular analysis of tumors to provide a detailed understanding of their unique biological characteristics. By utilizing cutting-edge technologies and analytical approaches, we deliver actionable insights into the genetic, epigenetic, and molecular features of tumors, supporting personalized treatment strategies and advancing cancer research.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Tumor Profiling?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Detailed Molecular Insights: Tumor profiling provides in-depth analysis of genetic mutations, gene expression, and molecular pathways within tumors, offering a detailed view of the tumor’s unique biological landscape."),
                                rx.list_item("Identification of Therapeutic Targets: By analyzing tumor-specific alterations, we identify potential therapeutic targets, including actionable mutations and dysregulated pathways, facilitating the development of targeted therapies and personalized treatment plans."),
                                rx.list_item("Assessment of Treatment Response: Profiling helps predict how tumors will respond to specific treatments, including chemotherapy, targeted therapy, and immunotherapy, enabling more effective and personalized treatment strategies."),
                                rx.list_item("Detection of Minimal Residual Disease: Identify residual cancer cells that may be present after treatment, aiding in the monitoring of disease progression and the effectiveness of therapy."),
                                rx.list_item("Support for Clinical Trials: Tumor profiling provides critical data for designing and conducting clinical trials, including identifying patient populations with specific molecular profiles that may benefit from novel therapies."),
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
                                rx.list_item("Oncologists & Healthcare Providers: Access detailed molecular data to enhance diagnostic accuracy, tailor treatment plans, and improve patient management based on the tumor’s specific profile."),
                                rx.list_item("Researchers: Utilize tumor profiling data to study cancer biology, uncover new mechanisms of tumor progression, and identify novel therapeutic targets."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Leverage tumor profiling to support drug discovery, develop targeted therapies, and optimize clinical trial designs based on molecular characteristics of tumors."),
                                rx.list_item("Clinical Trial Teams: Use profiling data to select appropriate patient cohorts, monitor treatment responses, and evaluate the efficacy of new therapies."),
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
                                rx.list_item("Sample Collection & Preparation: We provide guidelines for the collection and preparation of tumor samples to ensure high-quality analysis and accurate profiling results."),
                                rx.list_item("Genomic & Molecular Analysis: Employ advanced techniques such as next-generation sequencing (NGS), gene expression profiling, and proteomics to analyze the genetic and molecular features of tumors."),
                                rx.list_item("Bioinformatics & Data Integration: Our bioinformatics team integrates and analyzes multi-dimensional data to identify key genetic mutations, molecular pathways, and potential therapeutic targets."),
                                rx.list_item("Detailed Reporting: Receive comprehensive reports that include insights into tumor-specific alterations, potential therapeutic targets, and recommendations for treatment or further research."),
                                rx.list_item("Consultation & Support: Our team of experts is available to discuss findings, provide interpretation, and offer guidance on the implications for clinical practice, research, and therapeutic development."),
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
                                "We are dedicated to delivering high-quality, actionable insights through rigorous analysis and the latest technologies. Our Tumor Profiling service provides a detailed view of the tumor’s molecular landscape, driving forward research and improving patient outcomes through personalized and targeted treatment approaches.",
                                style=paragraph_style,
                                margin_top="2rem",
                                font_weight="bold",
                            ),
                        ),
                        width="60vw",
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
                banner("Tumor Profiling"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Tumor Profiling service offers comprehensive genomic and molecular analysis of tumors to provide a detailed understanding of their unique biological characteristics. By utilizing cutting-edge technologies and analytical approaches, we deliver actionable insights into the genetic, epigenetic, and molecular features of tumors, supporting personalized treatment strategies and advancing cancer research.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Tumor Profiling? - Mobile
                        rx.heading(
                            "Why Choose Tumor Profiling?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Detailed Molecular Insights: Tumor profiling provides in-depth analysis of genetic mutations, gene expression, and molecular pathways within tumors, offering a detailed view of the tumor’s unique biological landscape."),
                            rx.list_item("Identification of Therapeutic Targets: By analyzing tumor-specific alterations, we identify potential therapeutic targets, including actionable mutations and dysregulated pathways, facilitating the development of targeted therapies and personalized treatment plans."),
                            rx.list_item("Assessment of Treatment Response: Profiling helps predict how tumors will respond to specific treatments, including chemotherapy, targeted therapy, and immunotherapy, enabling more effective and personalized treatment strategies."),
                            rx.list_item("Detection of Minimal Residual Disease: Identify residual cancer cells that may be present after treatment, aiding in the monitoring of disease progression and the effectiveness of therapy."),
                            rx.list_item("Support for Clinical Trials: Tumor profiling provides critical data for designing and conducting clinical trials, including identifying patient populations with specific molecular profiles that may benefit from novel therapies."),
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
                            rx.list_item("Oncologists & Healthcare Providers: Access detailed molecular data to enhance diagnostic accuracy, tailor treatment plans, and improve patient management based on the tumor’s specific profile."),
                            rx.list_item("Researchers: Utilize tumor profiling data to study cancer biology, uncover new mechanisms of tumor progression, and identify novel therapeutic targets."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Leverage tumor profiling to support drug discovery, develop targeted therapies, and optimize clinical trial designs based on molecular characteristics of tumors."),
                            rx.list_item("Clinical Trial Teams: Use profiling data to select appropriate patient cohorts, monitor treatment responses, and evaluate the efficacy of new therapies."),
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
                            rx.list_item("Sample Collection & Preparation: We provide guidelines for the collection and preparation of tumor samples to ensure high-quality analysis and accurate profiling results."),
                            rx.list_item("Genomic & Molecular Analysis: Employ advanced techniques such as next-generation sequencing (NGS), gene expression profiling, and proteomics to analyze the genetic and molecular features of tumors."),
                            rx.list_item("Bioinformatics & Data Integration: Our bioinformatics team integrates and analyzes multi-dimensional data to identify key genetic mutations, molecular pathways, and potential therapeutic targets."),
                            rx.list_item("Detailed Reporting: Receive comprehensive reports that include insights into tumor-specific alterations, potential therapeutic targets, and recommendations for treatment or further research."),
                            rx.list_item("Consultation & Support: Our team of experts is available to discuss findings, provide interpretation, and offer guidance on the implications for clinical practice, research, and therapeutic development."),
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
                            "We are dedicated to delivering high-quality, actionable insights through rigorous analysis and the latest technologies. Our Tumor Profiling service provides a detailed view of the tumor’s molecular landscape, driving forward research and improving patient outcomes through personalized and targeted treatment approaches.",
                            style=mobile_paragraph_style,
                            margin_top="1rem",
                            font_weight="bold",
                        ),
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
        )
    )