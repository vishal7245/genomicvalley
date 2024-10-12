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


@rx.page(route="/whole-exome-sequencing", title="Whole Exome Sequencing (WES)")
def whole_exome_sequencing():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Whole Exome Sequencing (WES)"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Whole Exome Sequencing (WES) service offers focused and high-resolution analysis of the coding regions of the genome, known as exomes. By capturing the protein-coding portions of the genome, WES provides detailed insights into genetic variations that are often associated with disease, gene function, and molecular mechanisms.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Whole Exome Sequencing (WES)?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Targeted Focus: Analyze the exonic regions of the genome, which represent approximately 1-2% of the entire genome but contain the majority of known disease-related variants. This targeted approach is highly effective for identifying mutations linked to genetic disorders."),
                                rx.list_item("High Sensitivity: Detect rare and novel genetic variants with high sensitivity, improving the chances of identifying pathogenic mutations associated with inherited diseases and complex conditions."),
                                rx.list_item("Efficient and Cost-Effective: Compared to Whole Genome Sequencing, WES provides a cost-effective and efficient solution for studying the coding regions of the genome, making it an ideal choice for focused genetic investigations."),
                                rx.list_item("Enhanced Variant Discovery: Uncover a wide range of genetic variants, including single nucleotide variants (SNVs), insertions, deletions, and small structural variants, within the coding regions of the genome."),
                                rx.list_item("Applicability Across Research Areas: Support diverse research applications, including rare disease research, cancer genomics, gene function studies, and personalized medicine, by providing detailed information on protein-coding genes."),
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
                                rx.list_item("Researchers: Obtain targeted genetic data for studying the role of coding regions in disease and gene function, advancing research in fields such as human genetics, molecular biology, and evolutionary biology."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Utilize WES data to identify genetic targets for drug development, understand disease mechanisms, and explore potential therapeutic interventions."),
                                rx.list_item("Clinical Labs: Employ WES for diagnostic and prognostic purposes, including the identification of genetic mutations associated with rare and complex diseases, supporting personalized treatment strategies."),
                                rx.list_item("Academic Institutions: Enhance research capabilities with focused exome data, contributing to academic research, publications, and advancements in genetic and genomic studies."),
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
                                rx.list_item("Sample Collection: Follow detailed guidelines for sample submission to ensure high-quality DNA extraction, including requirements for sample type and storage conditions."),
                                rx.list_item("Library Preparation: Convert genomic DNA into sequencing libraries with a focus on coding regions, using advanced techniques such as exome capture, fragmentation, adapter ligation, and amplification."),
                                rx.list_item("Sequencing: Perform whole exome sequencing using state-of-the-art platforms to generate high-resolution data specifically from the exonic regions of the genome."),
                                rx.list_item("Data Analysis: Apply comprehensive bioinformatics tools to analyze sequencing data, including variant calling, annotation, and interpretation, focusing on coding region variations."),
                                rx.list_item("Quality Control: Implement rigorous quality control measures to ensure the accuracy, completeness, and reliability of the exome sequencing data, meeting high standards of precision."),
                                rx.list_item("Reporting: Generate detailed reports that summarize findings, highlight significant genetic variants, and provide interpretation of results in the context of research or clinical objectives."),
                                rx.list_item("Consultation & Support: Offer expert support throughout the WES process, addressing questions, providing insights, and assisting with the integration of findings into research or clinical practice."),
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
                                "We are dedicated to providing high-quality Whole Exome Sequencing (WES) services that deliver precise and actionable insights into the coding regions of the genome. By employing advanced technologies and expert analysis, our WES service supports meaningful research discoveries and advances in genetic studies, contributing to a better understanding of genetic variation and its implications for health and disease.",
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
                banner("Whole Exome Sequencing (WES)"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Whole Exome Sequencing (WES) service offers focused and high-resolution analysis of the coding regions of the genome, known as exomes. By capturing the protein-coding portions of the genome, WES provides detailed insights into genetic variations that are often associated with disease, gene function, and molecular mechanisms.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Whole Exome Sequencing (WES)? - Mobile
                        rx.heading(
                            "Why Choose Whole Exome Sequencing (WES)?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Targeted Focus: Analyze the exonic regions of the genome, which represent approximately 1-2% of the entire genome but contain the majority of known disease-related variants. This targeted approach is highly effective for identifying mutations linked to genetic disorders."),
                            rx.list_item("High Sensitivity: Detect rare and novel genetic variants with high sensitivity, improving the chances of identifying pathogenic mutations associated with inherited diseases and complex conditions."),
                            rx.list_item("Efficient and Cost-Effective: Compared to Whole Genome Sequencing, WES provides a cost-effective and efficient solution for studying the coding regions of the genome, making it an ideal choice for focused genetic investigations."),
                            rx.list_item("Enhanced Variant Discovery: Uncover a wide range of genetic variants, including single nucleotide variants (SNVs), insertions, deletions, and small structural variants, within the coding regions of the genome."),
                            rx.list_item("Applicability Across Research Areas: Support diverse research applications, including rare disease research, cancer genomics, gene function studies, and personalized medicine, by providing detailed information on protein-coding genes."),
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
                            rx.list_item("Researchers: Obtain targeted genetic data for studying the role of coding regions in disease and gene function, advancing research in fields such as human genetics, molecular biology, and evolutionary biology."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Utilize WES data to identify genetic targets for drug development, understand disease mechanisms, and explore potential therapeutic interventions."),
                            rx.list_item("Clinical Labs: Employ WES for diagnostic and prognostic purposes, including the identification of genetic mutations associated with rare and complex diseases, supporting personalized treatment strategies."),
                            rx.list_item("Academic Institutions: Enhance research capabilities with focused exome data, contributing to academic research, publications, and advancements in genetic and genomic studies."),
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
                            rx.list_item("Sample Collection: Follow detailed guidelines for sample submission to ensure high-quality DNA extraction, including requirements for sample type and storage conditions."),
                            rx.list_item("Library Preparation: Convert genomic DNA into sequencing libraries with a focus on coding regions, using advanced techniques such as exome capture, fragmentation, adapter ligation, and amplification."),
                            rx.list_item("Sequencing: Perform whole exome sequencing using state-of-the-art platforms to generate high-resolution data specifically from the exonic regions of the genome."),
                            rx.list_item("Data Analysis: Apply comprehensive bioinformatics tools to analyze sequencing data, including variant calling, annotation, and interpretation, focusing on coding region variations."),
                            rx.list_item("Quality Control: Implement rigorous quality control measures to ensure the accuracy, completeness, and reliability of the exome sequencing data, meeting high standards of precision."),
                            rx.list_item("Reporting: Generate detailed reports that summarize findings, highlight significant genetic variants, and provide interpretation of results in the context of research or clinical objectives."),
                            rx.list_item("Consultation & Support: Offer expert support throughout the WES process, addressing questions, providing insights, and assisting with the integration of findings into research or clinical practice."),
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
                            "We are dedicated to providing high-quality Whole Exome Sequencing (WES) services that deliver precise and actionable insights into the coding regions of the genome. By employing advanced technologies and expert analysis, our WES service supports meaningful research discoveries and advances in genetic studies, contributing to a better understanding of genetic variation and its implications for health and disease.",
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