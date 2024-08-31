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

image_urls = [
    "/Personalized Healthcare.jpg",
    "/Genetic Disease Predisposition.jpg",
    "/Community Health Support.jpg",
]

@rx.page(route="/rna-sequencing", title="RNA Sequencing")
def rna_sequencing():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("RNA Sequencing"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "RNA sequencing (RNA-Seq) is a cutting-edge technology that revolutionizes our understanding of the transcriptome—the complete set of RNA molecules expressed by a cell, tissue, or organism at any given moment. This powerful technique decodes the intricate language of RNA, enabling researchers to uncover the full spectrum of gene expression, dissect complex regulatory networks, and explore the dynamic world of non-coding RNAs. By capturing and quantifying RNA molecules with unprecedented precision, RNA-Seq provides deep insights into gene activity, alternative splicing patterns, and the vast array of non-coding RNA species, driving breakthroughs in biology and medicine.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "mRNA Sequencing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "mRNA Sequencing, often referred to as mRNA-Seq, focuses on the subset of the transcriptome that encodes proteins. This technique specifically sequences messenger RNA (mRNA) molecules, which are transcribed from DNA and translated into proteins. By targeting the mRNA, mRNA-Seq provides a detailed snapshot of gene expression, enabling researchers to identify and quantify the genes that are actively being transcribed in a sample.",
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
                                rx.list_item("Gene Expression Profiling: Understanding which genes are upregulated or downregulated under specific conditions, such as disease states, drug treatments, or environmental factors."),
                                rx.list_item("Alternative Splicing Analysis: Detecting different splicing events that lead to multiple protein isoforms from a single gene."),
                                rx.list_item("Biomarker Discovery: Identifying potential biomarkers for diseases or therapeutic responses."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Total RNA Sequencing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Total RNA Sequencing (Total RNA-Seq) is a comprehensive approach that captures all RNA species present in a sample, including mRNA, ribosomal RNA (rRNA), transfer RNA (tRNA), long non-coding RNA (lncRNA), and other small RNAs. This technique provides a complete overview of the transcriptome, allowing for the study of both coding and non-coding regions of RNA.",
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
                                rx.list_item("Transcriptome Profiling: Comprehensive analysis of all RNA molecules to understand the full complexity of gene expression."),
                                rx.list_item("Non-coding RNA Analysis: Investigating the roles of lncRNAs, small RNAs, and other non-coding RNAs in regulating gene expression and cellular processes."),
                                rx.list_item("Comparative Transcriptomics: Comparing the transcriptome between different conditions, species, or tissues to identify conserved or unique RNA species."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "miRNA Sequencing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "miRNA Sequencing (miRNA-Seq) is a specialized RNA-Seq technique that targets microRNAs (miRNAs), a class of small non-coding RNAs that play critical roles in gene regulation. miRNAs typically bind to the 3' untranslated regions (3' UTRs) of target mRNAs, leading to their degradation or inhibition of translation. miRNA-Seq provides insights into the miRNA landscape of a sample, enabling the study of their regulatory networks and their roles in health and disease.",
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
                                rx.list_item("Regulatory Network Analysis: Understanding how miRNAs regulate gene expression and their impact on cellular pathways."),
                                rx.list_item("Disease Research: Identifying miRNA signatures associated with various diseases, including cancer, cardiovascular diseases, and neurological disorders."),
                                rx.list_item("Therapeutic Targeting: Exploring miRNAs as potential therapeutic targets or biomarkers for diagnosis and prognosis."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Explore our RNA sequencing services to unlock the secrets of your transcriptome. Whether you're interested in mRNA profiling, comprehensive RNA analysis, or the intricate regulatory roles of miRNAs, our cutting-edge sequencing solutions provide the insights you need for your research. Contact us today to learn more about how our services can empower your discoveries.",
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
                banner("RNA Sequencing"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "RNA sequencing (RNA-Seq) is a cutting-edge technology that revolutionizes our understanding of the transcriptome—the complete set of RNA molecules expressed by a cell, tissue, or organism at any given moment. This powerful technique decodes the intricate language of RNA, enabling researchers to uncover the full spectrum of gene expression, dissect complex regulatory networks, and explore the dynamic world of non-coding RNAs. By capturing and quantifying RNA molecules with unprecedented precision, RNA-Seq provides deep insights into gene activity, alternative splicing patterns, and the vast array of non-coding RNA species, driving breakthroughs in biology and medicine.",
                            style=mobile_paragraph_style,
                        ),
                        # mRNA Sequencing - Mobile
                        rx.heading(
                            "mRNA Sequencing",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "mRNA Sequencing, often referred to as mRNA-Seq, focuses on the subset of the transcriptome that encodes proteins. This technique specifically sequences messenger RNA (mRNA) molecules, which are transcribed from DNA and translated into proteins. By targeting the mRNA, mRNA-Seq provides a detailed snapshot of gene expression, enabling researchers to identify and quantify the genes that are actively being transcribed in a sample.",
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
                            rx.list_item("Gene Expression Profiling: Understanding which genes are upregulated or downregulated under specific conditions, such as disease states, drug treatments, or environmental factors."),
                            rx.list_item("Alternative Splicing Analysis: Detecting different splicing events that lead to multiple protein isoforms from a single gene."),
                            rx.list_item("Biomarker Discovery: Identifying potential biomarkers for diseases or therapeutic responses."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Total RNA Sequencing - Mobile
                        rx.heading(
                            "Total RNA Sequencing",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Total RNA Sequencing (Total RNA-Seq) is a comprehensive approach that captures all RNA species present in a sample, including mRNA, ribosomal RNA (rRNA), transfer RNA (tRNA), long non-coding RNA (lncRNA), and other small RNAs. This technique provides a complete overview of the transcriptome, allowing for the study of both coding and non-coding regions of RNA.",
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
                            rx.list_item("Transcriptome Profiling: Comprehensive analysis of all RNA molecules to understand the full complexity of gene expression."),
                            rx.list_item("Non-coding RNA Analysis: Investigating the roles of lncRNAs, small RNAs, and other non-coding RNAs in regulating gene expression and cellular processes."),
                            rx.list_item("Comparative Transcriptomics: Comparing the transcriptome between different conditions, species, or tissues to identify conserved or unique RNA species."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # miRNA Sequencing - Mobile
                        rx.heading(
                            "miRNA Sequencing",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "miRNA Sequencing (miRNA-Seq) is a specialized RNA-Seq technique that targets microRNAs (miRNAs), a class of small non-coding RNAs that play critical roles in gene regulation. miRNAs typically bind to the 3' untranslated regions (3' UTRs) of target mRNAs, leading to their degradation or inhibition of translation. miRNA-Seq provides insights into the miRNA landscape of a sample, enabling the study of their regulatory networks and their roles in health and disease.",
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
                            rx.list_item("Regulatory Network Analysis: Understanding how miRNAs regulate gene expression and their impact on cellular pathways."),
                            rx.list_item("Disease Research: Identifying miRNA signatures associated with various diseases, including cancer, cardiovascular diseases, and neurological disorders."),
                            rx.list_item("Therapeutic Targeting: Exploring miRNAs as potential therapeutic targets or biomarkers for diagnosis and prognosis."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Explore our RNA sequencing services to unlock the secrets of your transcriptome. Whether you're interested in mRNA profiling, comprehensive RNA analysis, or the intricate regulatory roles of miRNAs, our cutting-edge sequencing solutions provide the insights you need for your research. Contact us today to learn more about how our services can empower your discoveries.",
                            style=mobile_paragraph_style,
                            margin_top="2rem",
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