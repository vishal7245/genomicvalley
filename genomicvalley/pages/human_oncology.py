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

@rx.page(route="/human-oncology-inherited-disease-testing", title="Human Oncology and Inherited Disease Testing")
def human_oncology_inherited_disease_testing():
    return rx.section(
        rx.desktop_only(  # Start of desktop layout
            rx.vstack(
                navbar(),
                banner("Human Oncology and Inherited Disease Testing"),
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
                                "Enhance your understanding and management of cancer and inherited diseases with our advanced testing services. Whether you are focusing on DNA-based mutations or RNA fusions, our comprehensive panels and analyses provide the critical insights needed for effective diagnosis and treatment. Contact Us Today to discover how our Human Oncology and Inherited Disease Testing services can support your clinical and research needs.",
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
        ),  # End of desktop layout
        rx.mobile_and_tablet( # Start of mobile layout
            rx.vstack(
                navbar(),
                banner("Human Oncology and Inherited Disease Testing"),
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
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
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
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Enhance your understanding and management of cancer and inherited diseases with our advanced testing services. Whether you are focusing on DNA-based mutations or RNA fusions, our comprehensive panels and analyses provide the critical insights needed for effective diagnosis and treatment. Contact Us Today to discover how our Human Oncology and Inherited Disease Testing services can support your clinical and research needs.",
                            style=mobile_paragraph_style,
                            margin_top="2rem",
                            font_weight="bold",
                        ),
                    ),
                    width="100%",
                    p="2", # smaller padding for mobile
                    padding="2rem",
                ),
                footer(),
                width="100%",
                spacing="2" # smaller spacing for mobile 
            ),
            width="100%",
        ) # End of mobile layout
    )