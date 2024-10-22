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


@rx.page(route="/whole-genome-sequencing", title="Whole Genome Sequencing (WGS)")
def whole_genome_sequencing():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Whole Genome Sequencing (WGS)"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Whole Genome Sequencing (WGS) service offers comprehensive and high-resolution analysis of an entire genome, providing detailed insights into genetic variations across the whole DNA sequence. By leveraging state-of-the-art sequencing technologies, we deliver precise and actionable data that supports a wide range of research applications, from basic genetic studies to complex disease investigations.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Whole Genome Sequencing (WGS)?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Comprehensive Coverage: Analyze the complete genome, capturing all genetic variations, including single nucleotide polymorphisms (SNPs), insertions, deletions, and structural variants, to provide a thorough understanding of genetic diversity."),
                                rx.list_item("High Resolution: Utilize advanced sequencing technologies to achieve high-resolution data with accurate detection of genetic variants, ensuring reliable results for complex genetic studies."),
                                rx.list_item("In-Depth Analysis: Gain insights into both coding and non-coding regions of the genome, facilitating the study of gene function, regulatory elements, and potential disease mechanisms."),
                                rx.list_item("Unbiased Data: Avoid biases associated with targeted sequencing approaches by analyzing the entire genome, allowing for the discovery of novel variants and associations that may be missed with other methods."),
                                rx.list_item("Enhanced Research Applications: Support a wide range of research applications, including population genetics, evolutionary studies, cancer genomics, and rare disease research, by providing comprehensive genomic information."),
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
                                rx.list_item("Researchers: Obtain in-depth genomic data for a variety of research purposes, including the study of genetic variations, gene function, and disease mechanisms, enhancing understanding of complex biological systems."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Leverage WGS data to support drug discovery, identify new therapeutic targets, and understand genetic factors influencing drug responses and efficacy."),
                                rx.list_item("Clinical Labs: Utilize WGS for diagnostic and prognostic applications, including the identification of genetic mutations associated with rare and complex diseases, enabling personalized medicine approaches."),
                                rx.list_item("Academic Institutions: Enhance research capabilities with comprehensive genomic data, contributing to academic publications and advancing scientific knowledge in genomics and related fields."),
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
                                rx.list_item("Library Preparation: Convert genomic DNA into sequencing libraries using advanced techniques, including fragmentation, adapter ligation, and amplification, to prepare samples for sequencing."),
                                rx.list_item("Sequencing: Perform whole genome sequencing using state-of-the-art platforms to generate high-resolution data, capturing all genetic variations across the entire genome."),
                                rx.list_item("Data Analysis: Apply comprehensive bioinformatics tools and algorithms to analyze sequencing data, including variant calling, annotation, and interpretation, to provide actionable insights."),
                                rx.list_item("Quality Control: Implement rigorous quality control measures to assess data accuracy, completeness, and reliability, ensuring that results meet high standards of precision."),
                                rx.list_item("Reporting: Generate detailed reports that summarize findings, highlight key genetic variants, and provide interpretation of results in the context of research or clinical objectives."),
                                rx.list_item("Consultation & Support: Offer expert support and consultation throughout the WGS process, addressing questions, providing insights, and assisting with the integration of findings into research or clinical practice."),
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
                                "We are committed to delivering high-quality Whole Genome Sequencing (WGS) services that provide comprehensive and accurate genomic data for a wide range of applications. By employing advanced technologies and expert analysis, our WGS service supports meaningful research discoveries and advances in genomics, contributing to a deeper understanding of genetic variation and its impact on health and disease.",
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
                banner("Whole Genome Sequencing (WGS)"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Whole Genome Sequencing (WGS) service offers comprehensive and high-resolution analysis of an entire genome, providing detailed insights into genetic variations across the whole DNA sequence. By leveraging state-of-the-art sequencing technologies, we deliver precise and actionable data that supports a wide range of research applications, from basic genetic studies to complex disease investigations.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Whole Genome Sequencing (WGS)? - Mobile
                        rx.heading(
                            "Why Choose Whole Genome Sequencing (WGS)?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Comprehensive Coverage: Analyze the complete genome, capturing all genetic variations, including single nucleotide polymorphisms (SNPs), insertions, deletions, and structural variants, to provide a thorough understanding of genetic diversity."),
                            rx.list_item("High Resolution: Utilize advanced sequencing technologies to achieve high-resolution data with accurate detection of genetic variants, ensuring reliable results for complex genetic studies."),
                            rx.list_item("In-Depth Analysis: Gain insights into both coding and non-coding regions of the genome, facilitating the study of gene function, regulatory elements, and potential disease mechanisms."),
                            rx.list_item("Unbiased Data: Avoid biases associated with targeted sequencing approaches by analyzing the entire genome, allowing for the discovery of novel variants and associations that may be missed with other methods."),
                            rx.list_item("Enhanced Research Applications: Support a wide range of research applications, including population genetics, evolutionary studies, cancer genomics, and rare disease research, by providing comprehensive genomic information."),
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
                            rx.list_item("Researchers: Obtain in-depth genomic data for a variety of research purposes, including the study of genetic variations, gene function, and disease mechanisms, enhancing understanding of complex biological systems."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Leverage WGS data to support drug discovery, identify new therapeutic targets, and understand genetic factors influencing drug responses and efficacy."),
                            rx.list_item("Clinical Labs: Utilize WGS for diagnostic and prognostic applications, including the identification of genetic mutations associated with rare and complex diseases, enabling personalized medicine approaches."),
                            rx.list_item("Academic Institutions: Enhance research capabilities with comprehensive genomic data, contributing to academic publications and advancing scientific knowledge in genomics and related fields."),
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
                            rx.list_item("Library Preparation: Convert genomic DNA into sequencing libraries using advanced techniques, including fragmentation, adapter ligation, and amplification, to prepare samples for sequencing."),
                            rx.list_item("Sequencing: Perform whole genome sequencing using state-of-the-art platforms to generate high-resolution data, capturing all genetic variations across the entire genome."),
                            rx.list_item("Data Analysis: Apply comprehensive bioinformatics tools and algorithms to analyze sequencing data, including variant calling, annotation, and interpretation, to provide actionable insights."),
                            rx.list_item("Quality Control: Implement rigorous quality control measures to assess data accuracy, completeness, and reliability, ensuring that results meet high standards of precision."),
                            rx.list_item("Reporting: Generate detailed reports that summarize findings, highlight key genetic variants, and provide interpretation of results in the context of research or clinical objectives."),
                            rx.list_item("Consultation & Support: Offer expert support and consultation throughout the WGS process, addressing questions, providing insights, and assisting with the integration of findings into research or clinical practice."),
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
                            "We are committed to delivering high-quality Whole Genome Sequencing (WGS) services that provide comprehensive and accurate genomic data for a wide range of applications. By employing advanced technologies and expert analysis, our WGS service supports meaningful research discoveries and advances in genomics, contributing to a deeper understanding of genetic variation and its impact on health and disease.",
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