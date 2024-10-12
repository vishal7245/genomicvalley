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

@rx.page(route="/human-oncology-inherited-disease-testing", title="Human Oncology and Inherited Disease Testing")
def human_oncology_inherited_disease_testing():
    return rx.section(
        rx.desktop_only(  # Start of desktop layout
            rx.vstack(
                navbar(),
                banner("Human Oncology"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Human Oncology and Inherited Disease Testing encompasses advanced genomic analyses that are crucial for understanding cancer and genetic disorders. These tests provide deep insights into the genetic changes driving cancer development and the inherited mutations that can predispose individuals to various diseases. Our services in DNA-Based Mutations and RNA Fusion offer comprehensive solutions to support diagnosis, treatment planning, and genetic risk assessment.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "DNA-Based Mutations (CNV, SNV, InDel) - Germline and Somatic",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "DNA-based mutations are fundamental in understanding both inherited and acquired genetic alterations. This service covers a broad spectrum of mutations, including Copy Number Variants (CNVs), Single Nucleotide Variants (SNVs), and Insertions/Deletions (InDels). These mutations can be categorized into germline (inherited) and somatic (acquired), each with its implications for disease risk and treatment.",
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
                                rx.list_item("Germline Mutations: These are inherited and present in every cell of the body. They play a significant role in hereditary diseases and cancer predisposition. Our testing helps in identifying these mutations to assess risk and guide preventive measures."),
                                rx.list_item("Somatic Mutations: These mutations occur in specific cells and are often associated with cancer. Our service includes specialized panels for detecting and analyzing somatic mutations in various cancers, providing critical information for targeted therapy and personalized treatment plans."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            # Place the Tables here
                            rx.heading(
                                "Available DNA Panels",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell(
                                            rx.text("DNA Panels", style=paragraph_style)
                                        ),
                                        rx.table.column_header_cell(
                                            rx.text("Number of Genes", style=paragraph_style)
                                        ),
                                    ),
                                ),
                                rx.table.body(
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Human Breast Cancer Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("93", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Human Colorectal Cancer Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("71", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Human Myeloid Neoplasms Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("141", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Human Lung Cancer Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("72", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Human Inherited Disease Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("298", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Human Comprehensive Cancer Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("275", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Human Actionable Solid Tumor Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("22", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Human BRCA1 and BRCA2 Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("2", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Human BRCA1 and BRCA2 Plus Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("6", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Human HRR Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("15", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Human TMB and MSI Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("486", style=paragraph_style)
                                        ),
                                    ),
                                ),
                                width="100%",
                            ),
                            # First new table
                            rx.heading(
                                "Available DNA Pro Panels",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell(
                                            rx.text("DNA Pro Panels", style=paragraph_style)
                                        ),
                                        rx.table.column_header_cell(
                                            rx.text("Number of Genes", style=paragraph_style)
                                        ),
                                    ),
                                ),
                                rx.table.body(
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Comprehensive Cancer Research Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("225", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Breast Cancer Research Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("54", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Colorectal Cancer Research Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("76", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Myeloid Neoplasms Research Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("164", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Brain Cancer Research Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("50", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Lung Cancer Research Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("76", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Comprehensive Cancer Focus Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("164", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Breast Cancer Focus Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("36", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Colorectal Cancer Focus Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("53", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Myeloid Neoplasms Focus Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("92", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Brain Cancer Focus Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("26", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Lung Cancer Focus Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("44", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Comprehensive Hereditary Cancer Research Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("287", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Hereditary Breast and Ovarian Cancer Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("50", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Hereditary Colorectal Cancer Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("44", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Hematologic Malignancy Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("33", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Hereditary Prostate Cancer Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("23", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Hereditary Pancreatic Cancer Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("32", style=paragraph_style)
                                        ),
                                    ),
                                ),
                                width="100%",
                            ),
                            # Second new table
                            rx.heading(
                                "Available DNA Ultra Panels",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.table.root(
                                rx.table.header(
                                    rx.table.row(
                                        rx.table.column_header_cell(
                                            rx.text("DNA Ultra Panels", style=paragraph_style)
                                        ),
                                        rx.table.column_header_cell(
                                            rx.text("Number of Genes", style=paragraph_style)
                                        ),
                                    ),
                                ),
                                rx.table.body(
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Breast Cancer Research Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("14", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Colorectal Cancer Research Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("27", style=paragraph_style)
                                        ),
                                    ),
                                    rx.table.row(
                                        rx.table.row_header_cell(
                                            rx.text("Human Lung Cancer Panel", style=paragraph_style)
                                        ),
                                        rx.table.cell(
                                            rx.text("26", style=paragraph_style)
                                        ),
                                    ),
                                ),
                                width="100%",
                            ),
                            rx.heading(
                                "RNA Fusion",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "RNA Fusion involves the detection of fusion genes formed by the joining of two separate genes, which can result in oncogenic drivers in cancers. This service focuses on identifying these fusion events, which are crucial for accurate diagnosis, prognosis, and the development of targeted therapies.",
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
                                rx.list_item("Fusion Only: Detects gene fusions that are pivotal in various cancers. This focused approach helps in identifying specific fusion events associated with the disease."),
                                rx.list_item("Fusion, Expression, and SNV: Provides a comprehensive analysis by combining fusion detection with gene expression profiling and Single Nucleotide Variant (SNV) analysis, offering a more detailed view of the genetic landscape of the disease."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Enhance your understanding and management of cancer and inherited diseases with our advanced testing services. Whether you are focusing on DNA-based mutations or RNA fusions, our comprehensive panels and analyses provide the critical insights needed for effective diagnosis and treatment. Contact us today to discover how our Human Oncology and Inherited Disease Testing services can support your clinical and research needs.",
                                style=paragraph_style,
                                margin_top="2rem",
                                font_weight="bold",
                            ),
                            rx.button(
                                "Contact Us Today",
                                on_click=rx.redirect("/contact"),
                                style=button_style,
                                margin_top="1rem",
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
        ),  # End of desktop layout
        rx.mobile_and_tablet(  # Start of mobile layout
            rx.vstack(
                navbar(),
                banner("Human Oncology"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Human Oncology and Inherited Disease Testing encompasses advanced genomic analyses that are crucial for understanding cancer and genetic disorders. These tests provide deep insights into the genetic changes driving cancer development and the inherited mutations that can predispose individuals to various diseases. Our services in DNA-Based Mutations and RNA Fusion offer comprehensive solutions to support diagnosis, treatment planning, and genetic risk assessment.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "DNA-Based Mutations (CNV, SNV, InDel) - Germline and Somatic",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "DNA-based mutations are fundamental in understanding both inherited and acquired genetic alterations. This service covers a broad spectrum of mutations, including Copy Number Variants (CNVs), Single Nucleotide Variants (SNVs), and Insertions/Deletions (InDels). These mutations can be categorized into germline (inherited) and somatic (acquired), each with its implications for disease risk and treatment.",
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
                            rx.list_item("Germline Mutations: These are inherited and present in every cell of the body. They play a significant role in hereditary diseases and cancer predisposition. Our testing helps in identifying these mutations to assess risk and guide preventive measures."),
                            rx.list_item("Somatic Mutations: These mutations occur in specific cells and are often associated with cancer. Our service includes specialized panels for detecting and analyzing somatic mutations in various cancers, providing critical information for targeted therapy and personalized treatment plans."),
                            margin_left="1rem",  # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        # Place the Tables here
                        rx.heading(
                            "Available DNA Panels",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell(
                                        rx.text("DNA Panels", style=mobile_paragraph_style)
                                    ),
                                    rx.table.column_header_cell(
                                        rx.text("Number of Genes", style=mobile_paragraph_style)
                                    ),
                                ),
                            ),
                            rx.table.body(
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Human Breast Cancer Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("93", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Human Colorectal Cancer Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("71", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Human Myeloid Neoplasms Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("141", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Human Lung Cancer Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("72", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Human Inherited Disease Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("298", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Human Comprehensive Cancer Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("275", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Human Actionable Solid Tumor Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("22", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Human BRCA1 and BRCA2 Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("2", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Human BRCA1 and BRCA2 Plus Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("6", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Human HRR Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("15", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Human TMB and MSI Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("486", style=mobile_paragraph_style)
                                    ),
                                ),
                            ),
                            width="100%",
                        ),
                        # First new table
                        rx.heading(
                            "Available DNA Pro Panels",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell(
                                        rx.text("DNA Pro Panels", style=mobile_paragraph_style)
                                    ),
                                    rx.table.column_header_cell(
                                        rx.text("Number of Genes", style=mobile_paragraph_style)
                                    ),
                                ),
                            ),
                            rx.table.body(
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Comprehensive Cancer Research Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("225", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Breast Cancer Research Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("54", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Colorectal Cancer Research Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("76", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Myeloid Neoplasms Research Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("164", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Brain Cancer Research Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("50", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Lung Cancer Research Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("76", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Comprehensive Cancer Focus Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("164", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Breast Cancer Focus Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("36", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Colorectal Cancer Focus Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("53", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Myeloid Neoplasms Focus Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("92", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Brain Cancer Focus Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("26", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Lung Cancer Focus Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("44", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Comprehensive Hereditary Cancer Research Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("287", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Hereditary Breast and Ovarian Cancer Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("50", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Hereditary Colorectal Cancer Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("44", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Hematologic Malignancy Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("33", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Hereditary Prostate Cancer Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("23", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Hereditary Pancreatic Cancer Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("32", style=mobile_paragraph_style)
                                    ),
                                ),
                            ),
                            width="100%",
                        ),
                        # Second new table
                        rx.heading(
                            "Available DNA Ultra Panels",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell(
                                        rx.text("DNA Ultra Panels", style=mobile_paragraph_style)
                                    ),
                                    rx.table.column_header_cell(
                                        rx.text("Number of Genes", style=mobile_paragraph_style)
                                    ),
                                ),
                            ),
                            rx.table.body(
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Breast Cancer Research Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("14", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Colorectal Cancer Research Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("27", style=mobile_paragraph_style)
                                    ),
                                ),
                                rx.table.row(
                                    rx.table.row_header_cell(
                                        rx.text("Human Lung Cancer Panel", style=mobile_paragraph_style)
                                    ),
                                    rx.table.cell(
                                        rx.text("26", style=mobile_paragraph_style)
                                    ),
                                ),
                            ),
                            width="100%",
                        ),
                        rx.heading(
                            "RNA Fusion",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "RNA Fusion involves the detection of fusion genes formed by the joining of two separate genes, which can result in oncogenic drivers in cancers. This service focuses on identifying these fusion events, which are crucial for accurate diagnosis, prognosis, and the development of targeted therapies.",
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
                            rx.list_item("Fusion Only: Detects gene fusions that are pivotal in various cancers. This focused approach helps in identifying specific fusion events associated with the disease."),
                            rx.list_item("Fusion, Expression, and SNV: Provides a comprehensive analysis by combining fusion detection with gene expression profiling and Single Nucleotide Variant (SNV) analysis, offering a more detailed view of the genetic landscape of the disease."),
                            margin_left="1rem",  # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Enhance your understanding and management of cancer and inherited diseases with our advanced testing services. Whether you are focusing on DNA-based mutations or RNA fusions, our comprehensive panels and analyses provide the critical insights needed for effective diagnosis and treatment. Contact us today to discover how our Human Oncology and Inherited Disease Testing services can support your clinical and research needs.",
                            style=mobile_paragraph_style,
                            margin_top="2rem",
                            font_weight="bold",
                        ),
                        rx.button(
                            "Contact Us Today",
                            on_click=rx.redirect("/contact"),
                            style=button_style,
                            margin_top="1rem",
                        )
                    ),
                    width="100%",
                    p="2",  # Smaller padding for mobile
                    padding="2rem",
                ),
                footer(),
                width="100%",
                spacing="2",  # Smaller spacing for mobile
            ),
            width="100%",
        ),
        margin="0",
        padding="0",
    )
