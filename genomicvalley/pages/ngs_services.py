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


@rx.page(route="/ngs-services", title="NGS Services")
def ngs_services():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("NGS Services"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Next-Generation Sequencing (NGS) revolutionizes genomic research by providing high-throughput, detailed insights into genetic information. Our NGS services cover every stage of the sequencing process, from library preparation to data interpretation, ensuring that you receive comprehensive and actionable results. Whether you are conducting research, developing new therapies, or exploring genetic variants, our NGS services are designed to meet the highest standards of accuracy and efficiency.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Library Preparation",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Library Preparation is a critical step in NGS that involves preparing DNA or RNA samples for sequencing. This process includes fragmenting the genetic material, adding adapters, and amplifying the library to create a sequencing-ready sample. Our advanced library preparation techniques ensure high-quality, reproducible results, providing the foundation for successful sequencing and accurate data analysis.",
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
                                rx.list_item("Sample Preparation: Preparing diverse sample types, including genomic DNA, cDNA, and RNA."),
                                rx.list_item("Quality Control: Ensuring high-quality libraries with optimal fragment size and adapter ligation."),
                                rx.list_item("Customized Solutions: Tailoring library preparation protocols to meet specific research needs or sequencing platforms."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Sequencing Platforms",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Our NGS services utilize state-of-the-art sequencing platforms to deliver high-resolution genomic data. We offer sequencing on leading technologies including Illumina, PacBio, and Oxford Nanopore. Each platform provides unique advantages, such as high throughput, long-read capabilities, or real-time sequencing, allowing us to select the best technology for your specific research requirements.",
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
                                rx.list_item("Illumina Sequencing: Known for its high accuracy and throughput, ideal for large-scale genomics projects and short-read sequencing."),
                                rx.list_item("PacBio Sequencing: Provides long-read sequencing capabilities, useful for de novo assembly and detecting structural variations."),
                                rx.list_item("Oxford Nanopore Sequencing: Offers real-time sequencing with ultra-long reads, enabling comprehensive genomic analysis and dynamic data acquisition."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Bioinformatics Analysis",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Bioinformatics Analysis involves processing and interpreting the vast amounts of data generated by NGS. Our services include data alignment, variant calling, annotation, and integration with other omics data. Utilizing advanced algorithms and software, we provide comprehensive analysis tailored to your research goals, ensuring that you extract meaningful insights from your sequencing data.",
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
                                rx.list_item("Data Processing: Aligning sequencing reads to reference genomes and calling genetic variants."),
                                rx.list_item("Annotation: Identifying and annotating genetic variants, including SNPs, indels, and structural variants."),
                                rx.list_item("Integration: Combining NGS data with other omics data for a holistic view of genetic information."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Data Interpretation",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Data Interpretation is the final step in the NGS workflow, where the analyzed data is translated into actionable biological insights. Our experts provide detailed reports on genetic variants, expression profiles, and other key findings, offering guidance on their implications for your research or clinical applications. We work closely with you to ensure that the results are relevant and informative for your specific needs.",
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
                                rx.list_item("Clinical Insights: Interpreting data for clinical research and personalized medicine applications."),
                                rx.list_item("Research Findings: Providing insights into genetic variations, gene expression patterns, and disease mechanisms."),
                                rx.list_item("Consultative Support: Offering expert advice on the implications of your data and next steps for further investigation or application."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Unlock the full potential of your genomic research with our comprehensive NGS services. From meticulous library preparation to advanced data interpretation, we provide end-to-end solutions that ensure accurate, actionable insights.",
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
                banner("NGS Services"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Next-Generation Sequencing (NGS) revolutionizes genomic research by providing high-throughput, detailed insights into genetic information. Our NGS services cover every stage of the sequencing process, from library preparation to data interpretation, ensuring that you receive comprehensive and actionable results. Whether you are conducting research, developing new therapies, or exploring genetic variants, our NGS services are designed to meet the highest standards of accuracy and efficiency.",
                            style=mobile_paragraph_style,
                        ),
                        # Library Preparation - Mobile
                        rx.heading(
                            "Library Preparation",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Library Preparation is a critical step in NGS that involves preparing DNA or RNA samples for sequencing. This process includes fragmenting the genetic material, adding adapters, and amplifying the library to create a sequencing-ready sample. Our advanced library preparation techniques ensure high-quality, reproducible results, providing the foundation for successful sequencing and accurate data analysis.",
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
                            rx.list_item("Sample Preparation: Preparing diverse sample types, including genomic DNA, cDNA, and RNA."),
                            rx.list_item("Quality Control: Ensuring high-quality libraries with optimal fragment size and adapter ligation."),
                            rx.list_item("Customized Solutions: Tailoring library preparation protocols to meet specific research needs or sequencing platforms."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Sequencing Platforms - Mobile
                        rx.heading(
                            "Sequencing Platforms",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Our NGS services utilize state-of-the-art sequencing platforms to deliver high-resolution genomic data. We offer sequencing on leading technologies including Illumina, PacBio, and Oxford Nanopore. Each platform provides unique advantages, such as high throughput, long-read capabilities, or real-time sequencing, allowing us to select the best technology for your specific research requirements.",
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
                            rx.list_item("Illumina Sequencing: Known for its high accuracy and throughput, ideal for large-scale genomics projects and short-read sequencing."),
                            rx.list_item("PacBio Sequencing: Provides long-read sequencing capabilities, useful for de novo assembly and detecting structural variations."),
                            rx.list_item("Oxford Nanopore Sequencing: Offers real-time sequencing with ultra-long reads, enabling comprehensive genomic analysis and dynamic data acquisition."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Bioinformatics Analysis - Mobile
                        rx.heading(
                            "Bioinformatics Analysis",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Bioinformatics Analysis involves processing and interpreting the vast amounts of data generated by NGS. Our services include data alignment, variant calling, annotation, and integration with other omics data. Utilizing advanced algorithms and software, we provide comprehensive analysis tailored to your research goals, ensuring that you extract meaningful insights from your sequencing data.",
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
                            rx.list_item("Data Processing: Aligning sequencing reads to reference genomes and calling genetic variants."),
                            rx.list_item("Annotation: Identifying and annotating genetic variants, including SNPs, indels, and structural variants."),
                            rx.list_item("Integration: Combining NGS data with other omics data for a holistic view of genetic information."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Data Interpretation - Mobile
                        rx.heading(
                            "Data Interpretation",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Data Interpretation is the final step in the NGS workflow, where the analyzed data is translated into actionable biological insights. Our experts provide detailed reports on genetic variants, expression profiles, and other key findings, offering guidance on their implications for your research or clinical applications. We work closely with you to ensure that the results are relevant and informative for your specific needs.",
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
                            rx.list_item("Clinical Insights: Interpreting data for clinical research and personalized medicine applications."),
                            rx.list_item("Research Findings: Providing insights into genetic variations, gene expression patterns, and disease mechanisms."),
                            rx.list_item("Consultative Support: Offering expert advice on the implications of your data and next steps for further investigation or application."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Unlock the full potential of your genomic research with our comprehensive NGS services. From meticulous library preparation to advanced data interpretation, we provide end-to-end solutions that ensure accurate, actionable insights.",
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