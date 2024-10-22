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


@rx.page(route="/rare-disease-genomics", title="Rare Disease Genomics")
def rare_disease_genomics():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Rare Disease Genomics"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Rare Disease Genomics service specializes in the comprehensive analysis of genetic variations associated with rare and complex diseases. By leveraging advanced genomic technologies, we provide critical insights into the genetic underpinnings of rare conditions, facilitating accurate diagnosis, personalized treatment, and groundbreaking research. This service is designed to address the unique challenges of rare diseases, where traditional diagnostic methods often fall short.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Rare Disease Genomics?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("In-Depth Genetic Analysis: We utilize next-generation sequencing (NGS) and other cutting-edge technologies to analyze the entire genome or targeted regions, identifying rare genetic variants that are often missed by conventional methods."),
                                rx.list_item("Comprehensive Variant Detection: Our service includes the detection of a wide range of genetic variations, including single nucleotide changes, insertions, deletions, and structural variants, providing a thorough understanding of the genetic factors involved in rare diseases."),
                                rx.list_item("Accurate Diagnosis: Rare Disease Genomics helps in pinpointing the exact genetic cause of rare conditions, which can be critical for providing accurate diagnoses where traditional methods may not be sufficient."),
                                rx.list_item("Personalized Treatment: By identifying the specific genetic mutations associated with a rare disease, we enable the development of personalized treatment plans tailored to the individual’s genetic profile, potentially improving treatment outcomes and quality of life."),
                                rx.list_item("Research and Discovery: Our genomic analysis supports research into the etiology of rare diseases, helping to uncover novel disease mechanisms, identify new biomarkers, and develop targeted therapies."),
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
                                rx.list_item("Clinicians & Geneticists: Obtain precise genetic information to diagnose rare diseases, guide treatment decisions, and provide genetic counseling to patients and families."),
                                rx.list_item("Patients & Families: Gain access to advanced genetic testing to identify rare conditions, leading to accurate diagnoses and tailored treatment options."),
                                rx.list_item("Researchers: Leverage our genomic data to explore the genetic basis of rare diseases, contribute to research initiatives, and advance the understanding of these complex conditions."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Utilize our data to drive the development of new therapies and drugs for rare diseases, supported by detailed genetic insights and potential therapeutic targets."),
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
                                rx.list_item("Sample Collection & Preparation: We provide clear instructions for collecting and preparing samples to ensure high-quality genomic analysis."),
                                rx.list_item("Genomic Sequencing: Employing advanced NGS technology, we sequence the genome or specific regions of interest, capturing detailed genetic information."),
                                rx.list_item("Bioinformatics Analysis: Our sophisticated bioinformatics tools analyze the sequencing data to identify rare genetic variants, their potential impact, and their relevance to the patient’s condition."),
                                rx.list_item("Comprehensive Reporting: We deliver detailed reports that include the identified genetic variants, their potential clinical significance, and recommendations for further action or research."),
                                rx.list_item("Consultation & Support: Our team of genetic experts is available to discuss results, provide insights into the implications for diagnosis and treatment, and offer guidance on the next steps."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Commitment to Quality",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "We are dedicated to providing the highest quality results through rigorous quality control and the use of the latest genomic technologies. Our Rare Disease Genomics service ensures accurate, reliable, and actionable insights, supporting clinicians, researchers, and patients in their quest for understanding and managing rare diseases.",
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
                banner("Rare Disease Genomics"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Rare Disease Genomics service specializes in the comprehensive analysis of genetic variations associated with rare and complex diseases. By leveraging advanced genomic technologies, we provide critical insights into the genetic underpinnings of rare conditions, facilitating accurate diagnosis, personalized treatment, and groundbreaking research. This service is designed to address the unique challenges of rare diseases, where traditional diagnostic methods often fall short.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Rare Disease Genomics? - Mobile
                        rx.heading(
                            "Why Choose Rare Disease Genomics?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("In-Depth Genetic Analysis: We utilize next-generation sequencing (NGS) and other cutting-edge technologies to analyze the entire genome or targeted regions, identifying rare genetic variants that are often missed by conventional methods."),
                            rx.list_item("Comprehensive Variant Detection: Our service includes the detection of a wide range of genetic variations, including single nucleotide changes, insertions, deletions, and structural variants, providing a thorough understanding of the genetic factors involved in rare diseases."),
                            rx.list_item("Accurate Diagnosis: Rare Disease Genomics helps in pinpointing the exact genetic cause of rare conditions, which can be critical for providing accurate diagnoses where traditional methods may not be sufficient."),
                            rx.list_item("Personalized Treatment: By identifying the specific genetic mutations associated with a rare disease, we enable the development of personalized treatment plans tailored to the individual’s genetic profile, potentially improving treatment outcomes and quality of life."),
                            rx.list_item("Research and Discovery: Our genomic analysis supports research into the etiology of rare diseases, helping to uncover novel disease mechanisms, identify new biomarkers, and develop targeted therapies."),
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
                            rx.list_item("Clinicians & Geneticists: Obtain precise genetic information to diagnose rare diseases, guide treatment decisions, and provide genetic counseling to patients and families."),
                            rx.list_item("Patients & Families: Gain access to advanced genetic testing to identify rare conditions, leading to accurate diagnoses and tailored treatment options."),
                            rx.list_item("Researchers: Leverage our genomic data to explore the genetic basis of rare diseases, contribute to research initiatives, and advance the understanding of these complex conditions."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Utilize our data to drive the development of new therapies and drugs for rare diseases, supported by detailed genetic insights and potential therapeutic targets."),
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
                            rx.list_item("Sample Collection & Preparation: We provide clear instructions for collecting and preparing samples to ensure high-quality genomic analysis."),
                            rx.list_item("Genomic Sequencing: Employing advanced NGS technology, we sequence the genome or specific regions of interest, capturing detailed genetic information."),
                            rx.list_item("Bioinformatics Analysis: Our sophisticated bioinformatics tools analyze the sequencing data to identify rare genetic variants, their potential impact, and their relevance to the patient’s condition."),
                            rx.list_item("Comprehensive Reporting: We deliver detailed reports that include the identified genetic variants, their potential clinical significance, and recommendations for further action or research."),
                            rx.list_item("Consultation & Support: Our team of genetic experts is available to discuss results, provide insights into the implications for diagnosis and treatment, and offer guidance on the next steps."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Commitment to Quality - Mobile
                        rx.heading(
                            "Commitment to Quality",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "We are dedicated to providing the highest quality results through rigorous quality control and the use of the latest genomic technologies. Our Rare Disease Genomics service ensures accurate, reliable, and actionable insights, supporting clinicians, researchers, and patients in their quest for understanding and managing rare diseases.",
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