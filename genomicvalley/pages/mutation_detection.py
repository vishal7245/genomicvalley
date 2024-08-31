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

@rx.page(route="/mutation-detection", title="Mutation Detection")
def mutation_detection():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Mutation Detection"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Mutation Detection service provides precise and comprehensive analysis to identify genetic mutations associated with various diseases, including cancer, genetic disorders, and other conditions. By leveraging state-of-the-art genomic technologies and bioinformatics tools, we deliver critical insights into genetic variations that can inform diagnosis, treatment, and research.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Mutation Detection?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Accurate Mutation Identification: Our service uses advanced sequencing technologies, such as next-generation sequencing (NGS), to accurately detect a wide range of genetic mutations, including single nucleotide variants (SNVs), insertions, deletions, and copy number variations (CNVs)."),
                                rx.list_item("Comprehensive Genetic Analysis: We offer extensive analysis of both coding and non-coding regions of the genome, providing a complete picture of genetic alterations and their potential impact on gene function and disease."),
                                rx.list_item("Personalized Medicine: Identify mutations that can influence an individual’s response to treatment, enabling personalized therapeutic strategies tailored to each patient’s unique genetic profile."),
                                rx.list_item("Early Diagnosis and Risk Assessment: Detect genetic mutations associated with hereditary diseases and cancer predisposition, allowing for early diagnosis, risk assessment, and timely intervention."),
                                rx.list_item("Support for Research and Development: Provide valuable data for understanding the genetic basis of diseases, supporting drug discovery, and advancing research into novel therapeutic approaches."),
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
                                rx.list_item("Clinicians & Oncologists: Utilize mutation detection data to enhance diagnostic accuracy, guide treatment decisions, and develop personalized care plans based on genetic insights."),
                                rx.list_item("Researchers: Access detailed genetic data to explore disease mechanisms, study mutation impacts, and identify new biomarkers for disease and treatment research."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Leverage mutation detection data to support drug development, design clinical trials, and evaluate the efficacy of new therapies based on genetic profiles."),
                                rx.list_item("Genetic Counselors: Use mutation detection results to provide comprehensive genetic counseling, helping patients understand their genetic risks and make informed decisions about their health."),
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
                                rx.list_item("Sample Collection & Preparation: We provide detailed guidelines for collecting and preparing biological samples, ensuring high-quality DNA for accurate mutation analysis."),
                                rx.list_item("Genomic Sequencing: Employ advanced sequencing technologies, including whole-exome sequencing (WES), whole-genome sequencing (WGS), and targeted gene panels, to detect and analyze genetic mutations."),
                                rx.list_item("Bioinformatics Analysis: Our bioinformatics team processes and interprets sequencing data, identifying significant mutations and assessing their clinical relevance and potential impact on disease."),
                                rx.list_item("Detailed Reporting: Receive comprehensive reports that include identified mutations, their implications for disease or treatment, and recommendations for further action or research."),
                                rx.list_item("Consultation & Support: Our team of experts is available to discuss results, provide interpretation, and offer guidance on the implications for patient care, research, and therapeutic development."),
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
                                "We are dedicated to delivering high-quality, actionable insights through advanced technologies and rigorous analysis. Our Mutation Detection service provides essential information for diagnosing and managing genetic conditions, advancing research, and supporting personalized medicine.",
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
                banner("Mutation Detection"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Mutation Detection service provides precise and comprehensive analysis to identify genetic mutations associated with various diseases, including cancer, genetic disorders, and other conditions. By leveraging state-of-the-art genomic technologies and bioinformatics tools, we deliver critical insights into genetic variations that can inform diagnosis, treatment, and research.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Mutation Detection? - Mobile
                        rx.heading(
                            "Why Choose Mutation Detection?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Accurate Mutation Identification: Our service uses advanced sequencing technologies, such as next-generation sequencing (NGS), to accurately detect a wide range of genetic mutations, including single nucleotide variants (SNVs), insertions, deletions, and copy number variations (CNVs)."),
                            rx.list_item("Comprehensive Genetic Analysis: We offer extensive analysis of both coding and non-coding regions of the genome, providing a complete picture of genetic alterations and their potential impact on gene function and disease."),
                            rx.list_item("Personalized Medicine: Identify mutations that can influence an individual’s response to treatment, enabling personalized therapeutic strategies tailored to each patient’s unique genetic profile."),
                            rx.list_item("Early Diagnosis and Risk Assessment: Detect genetic mutations associated with hereditary diseases and cancer predisposition, allowing for early diagnosis, risk assessment, and timely intervention."),
                            rx.list_item("Support for Research and Development: Provide valuable data for understanding the genetic basis of diseases, supporting drug discovery, and advancing research into novel therapeutic approaches."),
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
                            rx.list_item("Clinicians & Oncologists: Utilize mutation detection data to enhance diagnostic accuracy, guide treatment decisions, and develop personalized care plans based on genetic insights."),
                            rx.list_item("Researchers: Access detailed genetic data to explore disease mechanisms, study mutation impacts, and identify new biomarkers for disease and treatment research."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Leverage mutation detection data to support drug development, design clinical trials, and evaluate the efficacy of new therapies based on genetic profiles."),
                            rx.list_item("Genetic Counselors: Use mutation detection results to provide comprehensive genetic counseling, helping patients understand their genetic risks and make informed decisions about their health."),
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
                            rx.list_item("Sample Collection & Preparation: We provide detailed guidelines for collecting and preparing biological samples, ensuring high-quality DNA for accurate mutation analysis."),
                            rx.list_item("Genomic Sequencing: Employ advanced sequencing technologies, including whole-exome sequencing (WES), whole-genome sequencing (WGS), and targeted gene panels, to detect and analyze genetic mutations."),
                            rx.list_item("Bioinformatics Analysis: Our bioinformatics team processes and interprets sequencing data, identifying significant mutations and assessing their clinical relevance and potential impact on disease."),
                            rx.list_item("Detailed Reporting: Receive comprehensive reports that include identified mutations, their implications for disease or treatment, and recommendations for further action or research."),
                            rx.list_item("Consultation & Support: Our team of experts is available to discuss results, provide interpretation, and offer guidance on the implications for patient care, research, and therapeutic development."),
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
                            "We are dedicated to delivering high-quality, actionable insights through advanced technologies and rigorous analysis. Our Mutation Detection service provides essential information for diagnosing and managing genetic conditions, advancing research, and supporting personalized medicine.",
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