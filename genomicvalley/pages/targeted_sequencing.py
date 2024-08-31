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

@rx.page(route="/targeted-sequencing", title="Targeted Sequencing")
def targeted_sequencing():
    return rx.section(
        rx.vstack(
            navbar(),
            banner("Targeted Sequencing"),
            rx.flex(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Targeted Sequencing service offers a focused approach to genomic analysis by specifically sequencing selected regions of interest within the genome. This method is designed to provide in-depth and high-resolution insights into particular genes, pathways, or genomic regions that are relevant to your research objectives, enabling detailed investigation of specific genetic elements.",
                            style=paragraph_style,
                        ),
                        rx.heading(
                            "Why Choose Targeted Sequencing?",
                            size="9",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Focused Analysis: Concentrate on specific regions of the genome, such as genes or pathways of interest, to obtain detailed and accurate data relevant to your research or clinical goals."),
                            rx.list_item("Enhanced Sensitivity: Increase the sensitivity of variant detection in targeted regions by using enriched sequencing techniques, which improves the ability to identify rare or low-frequency mutations."),
                            rx.list_item("Cost-Effective: Achieve high-resolution results at a lower cost compared to whole genome or whole exome sequencing, making it an efficient choice for focused genetic investigations."),
                            rx.list_item("Customizable Panels: Utilize customizable panels that can be tailored to your specific research needs, including panels for cancer genes, inherited disorders, pharmacogenomics, or other areas of interest."),
                            rx.list_item("Efficient Data Analysis: Generate high-quality data with reduced complexity, facilitating easier and faster data analysis and interpretation compared to broader sequencing approaches."),
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
                            rx.list_item("Researchers: Obtain targeted genetic data for studying specific genes, pathways, or mutations relevant to your research, advancing studies in fields such as cancer genomics, rare diseases, and gene function."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Use targeted sequencing to identify genetic variations associated with drug responses, optimize therapeutic targets, and understand disease mechanisms in a focused manner."),
                            rx.list_item("Clinical Labs: Apply targeted sequencing for diagnostic and prognostic purposes, including the identification of genetic mutations associated with specific diseases or conditions, supporting personalized medicine approaches."),
                            rx.list_item("Academic Institutions: Enhance research capabilities with focused sequencing data, contributing to academic research, publications, and advancements in specific areas of genomics."),
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
                            rx.list_item("Panel Design: Collaborate with our team to design a customized sequencing panel targeting specific genes, regions, or pathways relevant to your research or clinical objectives."),
                            rx.list_item("Sample Collection: Follow detailed guidelines for sample submission to ensure high-quality DNA extraction, including requirements for sample type and storage conditions."),
                            rx.list_item("Library Preparation: Prepare sequencing libraries with a focus on targeted regions, using advanced techniques such as hybridization capture or amplicon-based enrichment to isolate the regions of interest."),
                            rx.list_item("Sequencing: Perform targeted sequencing using state-of-the-art platforms to generate high-resolution data specifically from the selected regions of the genome."),
                            rx.list_item("Data Analysis: Apply comprehensive bioinformatics tools to analyze sequencing data, including variant calling, annotation, and interpretation, with a focus on the targeted regions."),
                            rx.list_item("Quality Control: Implement rigorous quality control measures to ensure the accuracy, completeness, and reliability of the targeted sequencing data, meeting high standards of precision."),
                            rx.list_item("Reporting: Generate detailed reports that summarize findings, highlight significant genetic variants, and provide interpretation of results in the context of your research or clinical objectives."),
                            rx.list_item("Consultation & Support: Offer expert support throughout the targeted sequencing process, addressing questions, providing insights, and assisting with the integration of findings into research or clinical practice."),
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
                            "We are dedicated to providing high-quality Targeted Sequencing services that deliver precise and actionable insights into selected regions of the genome. By employing advanced technologies and expert analysis, our Targeted Sequencing service supports meaningful research discoveries and clinical applications, contributing to a deeper understanding of genetic variation and its implications for health and disease.",
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
    )
