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

@rx.page(route="/sequencing-platforms", title="Sequencing Platforms")
def sequencing_platforms():
    return rx.section(
        rx.vstack(
            navbar(),
            banner("Sequencing Platforms"),
            rx.flex(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Sequencing Platforms service offers access to a range of advanced sequencing technologies designed to meet diverse research needs, from whole-genome analysis to targeted sequencing and transcriptomics. By providing cutting-edge platforms and expert support, we enable researchers to obtain high-quality, comprehensive genomic and transcriptomic data to drive scientific discovery and innovation.",
                            style=paragraph_style,
                        ),
                        rx.heading(
                            "Why Choose Our Sequencing Platforms?",
                            size="9",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Diverse Technology Options: Access a variety of sequencing platforms, including Next-Generation Sequencing (NGS), Single-Cell Sequencing, and Long-Read Sequencing, to suit different research requirements and applications."),
                            rx.list_item("High-Throughput Capability: Utilize platforms with high-throughput capabilities to generate large-scale sequencing data efficiently, accommodating projects of varying sizes and complexities."),
                            rx.list_item("Exceptional Data Quality: Benefit from state-of-the-art technologies that deliver high accuracy and resolution in genomic and transcriptomic analysis, ensuring reliable and reproducible results."),
                            rx.list_item("Customizable Solutions: Tailor sequencing approaches to meet specific research goals, including whole-genome sequencing (WGS), whole-exome sequencing (WES), RNA sequencing (RNA-seq), epigenomics, and more."),
                            rx.list_item("Expert Guidance: Receive support from our experienced team to select the most appropriate sequencing platform for your project, optimize experimental design, and ensure successful data generation."),
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
                            rx.list_item("Researchers: Obtain high-quality sequencing data for a wide range of applications, including genomic, transcriptomic, and epigenomic studies, to advance research in various fields such as cancer genomics, rare diseases, and evolutionary biology."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Leverage sequencing platforms to support drug discovery, development, and personalized medicine initiatives, gaining insights into genetic variations and molecular mechanisms."),
                            rx.list_item("Clinical Labs: Utilize sequencing technologies for diagnostic and prognostic applications, including genetic testing, cancer profiling, and personalized treatment strategies."),
                            rx.list_item("Academic Institutions: Enhance research capabilities with access to cutting-edge sequencing technologies, supporting a wide range of scientific investigations and contributing to academic advancements."),
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
                            rx.list_item("Platform Selection: Collaborate with our team to choose the most suitable sequencing platform for your research objectives, based on your specific needs and project goals."),
                            rx.list_item("Experimental Design: Receive guidance on designing experiments, including sample preparation, library construction, and sequencing parameters, to ensure optimal results."),
                            rx.list_item("Data Generation: Utilize our advanced sequencing platforms to generate high-quality data, including genomic, transcriptomic, or epigenomic sequences, depending on your research requirements."),
                            rx.list_item("Quality Control: Implement rigorous quality control measures to assess the accuracy, completeness, and reliability of the sequencing data, ensuring it meets your research standards."),
                            rx.list_item("Data Analysis & Interpretation: Optionally, benefit from data analysis services to process and interpret sequencing results, providing insights into genetic variations, gene expression, and other key findings."),
                            rx.list_item("Consultation & Support: Access expert support throughout the sequencing process, from platform selection to data analysis, to ensure successful outcomes and address any questions or challenges."),
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
                            "We are dedicated to providing top-tier sequencing platforms and expert support to enable high-impact research and discovery. By leveraging cutting-edge technologies and a deep understanding of sequencing applications, our Sequencing Platforms service delivers reliable, high-quality data that advances scientific knowledge and drives innovation.",
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
