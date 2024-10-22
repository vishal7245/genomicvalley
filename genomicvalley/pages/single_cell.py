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


@rx.page(route="/single-cell-sequencing", title="Single-Cell Sequencing")
def single_cell_sequencing():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Single-Cell Sequencing"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Single-Cell Sequencing service provides an advanced approach to analyzing gene expression and genetic variations at the single-cell level. This cutting-edge technology enables researchers to explore cellular heterogeneity and understand the molecular mechanisms underlying individual cell behavior, offering unparalleled insights into complex biological systems and disease processes.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Single-Cell Sequencing?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Cellular Resolution: Investigate gene expression and genetic variations in individual cells, allowing for the identification of rare cell types, subpopulations, and cellular states that may be obscured in bulk analyses."),
                                rx.list_item("High Sensitivity: Achieve high sensitivity in detecting low-abundance transcripts and genetic variants, providing detailed insights into the functional diversity and dynamics of single cells."),
                                rx.list_item("Comprehensive Profiling: Analyze various aspects of cellular biology, including transcriptomics, epigenomics, and genomic variations, to gain a holistic understanding of cellular functions and interactions."),
                                rx.list_item("Uncover Cellular Heterogeneity: Discover and characterize cellular heterogeneity within complex tissues or populations, advancing research in areas such as cancer, immunology, and developmental biology."),
                                rx.list_item("Facilitate Discovery: Identify novel biomarkers, regulatory mechanisms, and cellular interactions, contributing to breakthroughs in understanding disease mechanisms and developing targeted therapies."),
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
                                rx.list_item("Researchers: Gain detailed insights into single-cell gene expression, genetic variations, and cellular heterogeneity, enhancing research in fields such as cell biology, developmental biology, and cancer research."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Utilize single-cell data to explore drug effects on individual cells, identify novel therapeutic targets, and understand the molecular basis of drug responses and resistance."),
                                rx.list_item("Clinical Labs: Apply single-cell sequencing for diagnostic and prognostic purposes, including the identification of rare cell populations and disease-specific biomarkers, supporting personalized medicine approaches."),
                                rx.list_item("Academic Institutions: Enhance research capabilities with single-cell data, contributing to academic research, publications, and advancements in single-cell genomics."),
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
                                rx.list_item("Sample Collection: Follow detailed guidelines for sample submission to ensure high-quality cell isolation, including requirements for sample type, cell viability, and processing conditions."),
                                rx.list_item("Single-Cell Isolation: Employ advanced techniques for isolating individual cells from complex samples, including microfluidics and droplet-based methods, to prepare cells for sequencing."),
                                rx.list_item("Library Preparation: Convert RNA or DNA from individual cells into sequencing libraries using sophisticated methods, including cell barcoding and amplification, to enable high-throughput analysis."),
                                rx.list_item("Sequencing: Perform single-cell sequencing using state-of-the-art platforms to generate high-resolution data on gene expression or genetic variations for each cell."),
                                rx.list_item("Data Analysis: Apply advanced bioinformatics tools and algorithms to analyze single-cell data, including clustering, dimensionality reduction, and differential expression analysis, to uncover insights into cellular diversity and function."),
                                rx.list_item("Quality Control: Implement rigorous quality control measures to ensure the accuracy, completeness, and reliability of single-cell sequencing data, meeting high standards of precision."),
                                rx.list_item("Reporting: Generate detailed reports that summarize findings, highlight significant cellular variations, and provide interpretation of results in the context of research or clinical objectives."),
                                rx.list_item("Consultation & Support: Offer expert support throughout the single-cell sequencing process, addressing questions, providing insights, and assisting with the integration of findings into research or clinical practice."),
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
                                "We are dedicated to providing high-quality Single-Cell Sequencing services that deliver precise and actionable insights into individual cells. By employing advanced technologies and expert analysis, our Single-Cell Sequencing service supports meaningful research discoveries and clinical applications, contributing to a deeper understanding of cellular heterogeneity and its implications for health and disease.",
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
                banner("Single-Cell Sequencing"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Single-Cell Sequencing service provides an advanced approach to analyzing gene expression and genetic variations at the single-cell level. This cutting-edge technology enables researchers to explore cellular heterogeneity and understand the molecular mechanisms underlying individual cell behavior, offering unparalleled insights into complex biological systems and disease processes.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Single-Cell Sequencing? - Mobile
                        rx.heading(
                            "Why Choose Single-Cell Sequencing?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Cellular Resolution: Investigate gene expression and genetic variations in individual cells, allowing for the identification of rare cell types, subpopulations, and cellular states that may be obscured in bulk analyses."),
                            rx.list_item("High Sensitivity: Achieve high sensitivity in detecting low-abundance transcripts and genetic variants, providing detailed insights into the functional diversity and dynamics of single cells."),
                            rx.list_item("Comprehensive Profiling: Analyze various aspects of cellular biology, including transcriptomics, epigenomics, and genomic variations, to gain a holistic understanding of cellular functions and interactions."),
                            rx.list_item("Uncover Cellular Heterogeneity: Discover and characterize cellular heterogeneity within complex tissues or populations, advancing research in areas such as cancer, immunology, and developmental biology."),
                            rx.list_item("Facilitate Discovery: Identify novel biomarkers, regulatory mechanisms, and cellular interactions, contributing to breakthroughs in understanding disease mechanisms and developing targeted therapies."),
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
                            rx.list_item("Researchers: Gain detailed insights into single-cell gene expression, genetic variations, and cellular heterogeneity, enhancing research in fields such as cell biology, developmental biology, and cancer research."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Utilize single-cell data to explore drug effects on individual cells, identify novel therapeutic targets, and understand the molecular basis of drug responses and resistance."),
                            rx.list_item("Clinical Labs: Apply single-cell sequencing for diagnostic and prognostic purposes, including the identification of rare cell populations and disease-specific biomarkers, supporting personalized medicine approaches."),
                            rx.list_item("Academic Institutions: Enhance research capabilities with single-cell data, contributing to academic research, publications, and advancements in single-cell genomics."),
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
                            rx.list_item("Sample Collection: Follow detailed guidelines for sample submission to ensure high-quality cell isolation, including requirements for sample type, cell viability, and processing conditions."),
                            rx.list_item("Single-Cell Isolation: Employ advanced techniques for isolating individual cells from complex samples, including microfluidics and droplet-based methods, to prepare cells for sequencing."),
                            rx.list_item("Library Preparation: Convert RNA or DNA from individual cells into sequencing libraries using sophisticated methods, including cell barcoding and amplification, to enable high-throughput analysis."),
                            rx.list_item("Sequencing: Perform single-cell sequencing using state-of-the-art platforms to generate high-resolution data on gene expression or genetic variations for each cell."),
                            rx.list_item("Data Analysis: Apply advanced bioinformatics tools and algorithms to analyze single-cell data, including clustering, dimensionality reduction, and differential expression analysis, to uncover insights into cellular diversity and function."),
                            rx.list_item("Quality Control: Implement rigorous quality control measures to ensure the accuracy, completeness, and reliability of single-cell sequencing data, meeting high standards of precision."),
                            rx.list_item("Reporting: Generate detailed reports that summarize findings, highlight significant cellular variations, and provide interpretation of results in the context of research or clinical objectives."),
                            rx.list_item("Consultation & Support: Offer expert support throughout the single-cell sequencing process, addressing questions, providing insights, and assisting with the integration of findings into research or clinical practice."),
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
                            "We are dedicated to providing high-quality Single-Cell Sequencing services that deliver precise and actionable insights into individual cells. By employing advanced technologies and expert analysis, our Single-Cell Sequencing service supports meaningful research discoveries and clinical applications, contributing to a deeper understanding of cellular heterogeneity and its implications for health and disease.",
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