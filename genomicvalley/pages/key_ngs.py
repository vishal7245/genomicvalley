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


@rx.page(route="/key-areas-ngs-services", title="Key Areas of NGS Services")
def key_areas_ngs_services():
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
                banner("Key Areas of NGS Services"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Next-Generation Sequencing (NGS) offers a range of specialized services that cater to diverse research needs and objectives. Our key NGS services are designed to provide deep insights into genetic and transcriptomic data, enabling advanced discovery and understanding in genomics. Whether you need comprehensive genome analysis or specific targeted insights, our services cover all critical aspects of NGS to support your research goals.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Whole Genome Sequencing (WGS)",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Whole Genome Sequencing (WGS) provides a comprehensive view of an organism’s entire genome, capturing all genetic variations, including single nucleotide polymorphisms (SNPs), insertions, deletions, and structural variants. This high-resolution approach enables in-depth analysis of genetic diseases, evolutionary studies, and genomic architecture.",
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
                                rx.list_item("Disease Research: Identifying genetic variants associated with complex diseases and disorders."),
                                rx.list_item("Genomic Mapping: Exploring structural variations and their implications in health and disease."),
                                rx.list_item("Evolutionary Studies: Understanding genetic diversity and evolutionary relationships among species."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Whole Exome Sequencing (WES)",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Whole Exome Sequencing (WES) focuses on sequencing the coding regions of the genome, known as exomes. By targeting only the protein-coding genes, WES provides a cost-effective and high-resolution approach to identify variants that are often associated with genetic disorders and functional studies.",
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
                                rx.list_item("Genetic Disorder Diagnosis: Identifying mutations in coding regions linked to inherited diseases."),
                                rx.list_item("Functional Genomics: Analysing gene function and gene-disease associations."),
                                rx.list_item("Variant Prioritization: Narrowing down potential pathogenic variants from a vast genome."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Targeted Sequencing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Targeted Sequencing focuses on specific regions of interest within the genome, such as known disease-associated genes or pathways. This approach allows for high-depth sequencing of selected regions, providing detailed insights into genetic variations and their potential effects.",
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
                                rx.list_item("Disease Gene Panels: Sequencing genes known to be associated with specific diseases or conditions."),
                                rx.list_item("Mutation Analysis: Detecting mutations in targeted regions with high accuracy."),
                                rx.list_item("Personalized Medicine: Customizing sequencing panels based on individual patient needs."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "RNA Sequencing (RNA-Seq)",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "RNA Sequencing (RNA-Seq) provides a comprehensive analysis of the transcriptome, enabling the study of gene expression, alternative splicing, and non-coding RNA. This technique reveals dynamic changes in gene expression and functional annotations of transcripts.",
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
                                rx.list_item("Gene Expression Profiling: Quantifying gene expression levels across different conditions."),
                                rx.list_item("Alternative Splicing Analysis: Identifying splicing events and their impact on gene function."),
                                rx.list_item("Transcriptome Mapping: Discovering new transcripts and understanding their roles in cellular processes."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Single-cell Sequencing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Single-cell Sequencing enables the analysis of gene expression at the individual cell level, providing insights into cellular heterogeneity and rare cell populations. This technology is crucial for understanding complex tissues and uncovering cellular mechanisms in health and disease.",
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
                                rx.list_item("Cellular Heterogeneity: Exploring variations in gene expression between individual cells."),
                                rx.list_item("Developmental Biology: Studying cellular differentiation and development at the single-cell level."),
                                rx.list_item("Disease Mechanisms: Identifying rare cell types and understanding their roles in disease progression."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Metagenomics Testing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Metagenomics Testing involves analyzing the genetic material from environmental samples to study microbial communities and their functions. This approach provides insights into the diversity, composition, and functional potential of microbial populations in various environments.",
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
                                rx.list_item("Microbial Diversity: Assessing the diversity and abundance of microorganisms in environmental or clinical samples."),
                                rx.list_item("Pathogen Detection: Identifying and characterizing pathogens present in a sample."),
                                rx.list_item("Functional Profiling: Understanding the functional roles of microbial communities and their interactions."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Unlock the power of Next-Generation Sequencing with our comprehensive suite of services. From whole genome and exome sequencing to targeted and single-cell analyses, we provide cutting-edge solutions to advance your research and discovery.",
                                style=paragraph_style,
                                margin_top="2rem",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Contact Us Today to explore how our NGS services can enhance your projects and provide the insights you need. Let’s work together to drive innovation and achieve breakthroughs in genomics.",
                                style=paragraph_style,
                                margin_top="1rem",
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
                banner("Key Areas of NGS Services"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Next-Generation Sequencing (NGS) offers a range of specialized services that cater to diverse research needs and objectives. Our key NGS services are designed to provide deep insights into genetic and transcriptomic data, enabling advanced discovery and understanding in genomics. Whether you need comprehensive genome analysis or specific targeted insights, our services cover all critical aspects of NGS to support your research goals.",
                            style=mobile_paragraph_style,
                        ),
                        # Whole Genome Sequencing (WGS) - Mobile
                        rx.heading(
                            "Whole Genome Sequencing (WGS)",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Whole Genome Sequencing (WGS) provides a comprehensive view of an organism’s entire genome, capturing all genetic variations. This high-resolution approach enables in-depth analysis of genetic diseases, evolutionary studies, and genomic architecture.",
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
                            rx.list_item("Disease Research: Identifying genetic variants associated with complex diseases and disorders."),
                            rx.list_item("Genomic Mapping: Exploring structural variations and their implications in health and disease."),
                            rx.list_item("Evolutionary Studies: Understanding genetic diversity and evolutionary relationships among species."),
                            margin_left="1rem",  # Smaller margin
                            style=mobile_paragraph_style
                        ),

                        # Whole Exome Sequencing (WES) - Mobile
                        rx.heading(
                            "Whole Exome Sequencing (WES)",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Whole Exome Sequencing (WES) focuses on sequencing the coding regions of the genome, known as exomes. By targeting only the protein-coding genes, WES provides a cost-effective and high-resolution approach to identify variants that are often associated with genetic disorders and functional studies.",
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
                            rx.list_item("Genetic Disorder Diagnosis: Identifying mutations in coding regions linked to inherited diseases."),
                            rx.list_item("Functional Genomics: Analysing gene function and gene-disease associations."),
                            rx.list_item("Variant Prioritization: Narrowing down potential pathogenic variants from a vast genome."),
                            margin_left="1rem",  # Smaller margin
                            style=mobile_paragraph_style
                        ),

                        # Targeted Sequencing - Mobile
                        rx.heading(
                            "Targeted Sequencing",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Targeted Sequencing focuses on specific regions of interest within the genome, such as known disease-associated genes or pathways. This approach allows for high-depth sequencing of selected regions, providing detailed insights into genetic variations and their potential effects.",
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
                            rx.list_item("Disease Gene Panels: Sequencing genes known to be associated with specific diseases or conditions."),
                            rx.list_item("Mutation Analysis: Detecting mutations in targeted regions with high accuracy."),
                            rx.list_item("Personalized Medicine: Customizing sequencing panels based on individual patient needs."),
                            margin_left="1rem",  # Smaller margin
                            style=mobile_paragraph_style
                        ),

                        # RNA Sequencing (RNA-Seq) - Mobile
                        rx.heading(
                            "RNA Sequencing (RNA-Seq)",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "RNA Sequencing (RNA-Seq) provides a comprehensive analysis of the transcriptome, enabling the study of gene expression, alternative splicing, and non-coding RNA. This technique reveals dynamic changes in gene expression and functional annotations of transcripts.",
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
                            rx.list_item("Gene Expression Profiling: Quantifying gene expression levels across different conditions."),
                            rx.list_item("Alternative Splicing Analysis: Identifying splicing events and their impact on gene function."),
                            rx.list_item("Transcriptome Mapping: Discovering new transcripts and understanding their roles in cellular processes."),
                            margin_left="1rem",  # Smaller margin
                            style=mobile_paragraph_style
                        ),

                        # Single-cell Sequencing - Mobile
                        rx.heading(
                            "Single-cell Sequencing",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Single-cell Sequencing enables the analysis of gene expression at the individual cell level, providing insights into cellular heterogeneity and rare cell populations. This technology is crucial for understanding complex tissues and uncovering cellular mechanisms in health and disease.",
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
                            rx.list_item("Cellular Heterogeneity: Exploring variations in gene expression between individual cells."),
                            rx.list_item("Developmental Biology: Studying cellular differentiation and development at the single-cell level."),
                            rx.list_item("Disease Mechanisms: Identifying rare cell types and understanding their roles in disease progression."),
                            margin_left="1rem",  # Smaller margin
                            style=mobile_paragraph_style
                        ),

                        # Metagenomics Testing - Mobile
                        rx.heading(
                            "Metagenomics Testing",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Metagenomics Testing involves analyzing the genetic material from environmental samples to study microbial communities and their functions. This approach provides insights into the diversity, composition, and functional potential of microbial populations in various environments.",
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
                            rx.list_item("Microbial Diversity: Assessing the diversity and abundance of microorganisms in environmental or clinical samples."),
                            rx.list_item("Pathogen Detection: Identifying and characterizing pathogens present in a sample."),
                            rx.list_item("Functional Profiling: Understanding the functional roles of microbial communities and their interactions."),
                            margin_left="1rem",  # Smaller margin
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Unlock the power of Next-Generation Sequencing with our comprehensive suite of services. From whole genome and exome sequencing to targeted and single-cell analyses, we provide cutting-edge solutions to advance your research and discovery.",
                            style=mobile_paragraph_style,
                            margin_top="2rem",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Contact Us Today to explore how our NGS services can enhance your projects and provide the insights you need. Let’s work together to drive innovation and achieve breakthroughs in genomics.",
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
                    p="2",  # Smaller padding
                    padding="2rem",
                ),
                footer(),
                width="100%",
                spacing="2"  # Smaller spacing
            ),
            width="100%",
        ),
        margin="0",
        padding="0",
    )