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


@rx.page(route="/dna-based-mutations", title="DNA-Based Mutations")
def dna_based_mutations():
    return rx.section(
        rx.desktop_only(  # Start of desktop layout
            rx.vstack(
                navbar(),
                banner("DNA-Based Mutations"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "DNA mutations play a crucial role in the development of various diseases, including cancer. These mutations can be classified as germline (inherited) or somatic (acquired), and they include different types such as Copy Number Variants (CNVs), Single Nucleotide Variants (SNVs), and Insertions/Deletions (InDels). Understanding these mutations is essential for diagnosing genetic disorders, developing targeted therapies, and advancing personalized medicine. Our DNA-Based Mutations services provide comprehensive solutions for detecting and analyzing these mutations in both germline and somatic contexts.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Somatic Mutations",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Somatic mutations occur in non-germline cells and are often associated with cancer. These mutations can be acquired throughout a person’s life and are not passed on to offspring. Our Somatic Mutations service includes a range of specialized panels designed to detect CNVs, SNVs, and InDels in various cancers. These panels provide detailed insights into the genetic changes driving tumor development and progression, aiding in the development of personalized treatment plans.",
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
                                rx.list_item("Cancer Profiling: Identifying mutations in specific cancer types for targeted therapy."),
                                rx.list_item("Therapeutic Decision-Making: Informing treatment strategies based on the genetic makeup of tumors."),
                                rx.list_item("Prognosis and Monitoring: Assessing mutation status for disease progression and treatment response."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Panels:",
                                font_weight="bold",
                                margin_top="1rem",
                                margin_bottom="0.5rem",
                                style=paragraph_style
                            ),
                            rx.unordered_list(
                                rx.list_item("Breast Cancer Panel"),
                                rx.list_item("Colorectal Panel"),
                                rx.list_item("Myeloid Panel"),
                                rx.list_item("Lung Cancer Panel"),
                                rx.list_item("Pharmacogenomics"),
                                rx.list_item("Comprehensive Cancer Panel"),
                                rx.list_item("Actionable Solid Tumor Panel"),
                                rx.list_item("Mitochondria Panel"),
                                rx.list_item("HRR Panel"),
                                rx.list_item("HRD Panel"),
                                rx.list_item("TMB & MSI Panel"),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Hereditary-Based Testing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Hereditary-based testing focuses on identifying germline mutations that are inherited from parents and present in all cells of the body. These mutations can predispose individuals to certain cancers and other genetic disorders. Our Hereditary-Based Testing service includes panels that target specific hereditary cancer syndromes, providing valuable information for early detection, risk assessment, and prevention strategies.",
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
                                rx.list_item("Risk Assessment: Identifying individuals at risk for hereditary cancers."),
                                rx.list_item("Preventive Care: Informing strategies for early detection and prevention of genetic disorders."),
                                rx.list_item("Family Planning: Providing genetic information for informed reproductive decisions."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Panels:",
                                font_weight="bold",
                                margin_top="1rem",
                                margin_bottom="0.5rem",
                                style=paragraph_style
                            ),
                            rx.unordered_list(
                                rx.list_item("Brain Cancer"),
                                rx.list_item("Hematologic Malignancy"),
                                rx.list_item("Hereditary Pancreatic"),
                                rx.list_item("Whole Exome"),
                                rx.list_item("Actionable Exome"),
                                rx.list_item("Carrier Panel"),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Unlock the potential of genomic insights with our DNA-Based Mutations services. Whether you're focused on somatic mutations in cancer or hereditary-based genetic testing, our comprehensive solutions can guide your research and clinical decisions. Contact Us Today to learn how our advanced mutation analysis services can support your personalized medicine initiatives.",
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
        ),  # End of desktop layout
        rx.mobile_and_tablet( # Start of mobile layout
            rx.vstack(
                navbar(),
                banner("DNA-Based Mutations"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "DNA mutations play a crucial role in the development of various diseases, including cancer. These mutations can be classified as germline (inherited) or somatic (acquired), and they include different types such as Copy Number Variants (CNVs), Single Nucleotide Variants (SNVs), and Insertions/Deletions (InDels). Understanding these mutations is essential for diagnosing genetic disorders, developing targeted therapies, and advancing personalized medicine. Our DNA-Based Mutations services provide comprehensive solutions for detecting and analyzing these mutations in both germline and somatic contexts.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Somatic Mutations",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Somatic mutations occur in non-germline cells and are often associated with cancer. These mutations can be acquired throughout a person’s life and are not passed on to offspring. Our Somatic Mutations service includes a range of specialized panels designed to detect CNVs, SNVs, and InDels in various cancers. These panels provide detailed insights into the genetic changes driving tumor development and progression, aiding in the development of personalized treatment plans.",
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
                            rx.list_item("Cancer Profiling: Identifying mutations in specific cancer types for targeted therapy."),
                            rx.list_item("Therapeutic Decision-Making: Informing treatment strategies based on the genetic makeup of tumors."),
                            rx.list_item("Prognosis and Monitoring: Assessing mutation status for disease progression and treatment response."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Panels:",
                            font_weight="bold",
                            margin_top="1rem",
                            margin_bottom="0.5rem",
                            style=mobile_paragraph_style
                        ),
                        rx.unordered_list(
                            rx.list_item("Breast Cancer Panel"),
                            rx.list_item("Colorectal Panel"),
                            rx.list_item("Myeloid Panel"),
                            rx.list_item("Lung Cancer Panel"),
                            rx.list_item("Pharmacogenomics"),
                            rx.list_item("Comprehensive Cancer Panel"),
                            rx.list_item("Actionable Solid Tumor Panel"),
                            rx.list_item("Mitochondria Panel"),
                            rx.list_item("HRR Panel"),
                            rx.list_item("HRD Panel"),
                            rx.list_item("TMB & MSI Panel"),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Hereditary-Based Testing",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Hereditary-based testing focuses on identifying germline mutations that are inherited from parents and present in all cells of the body. These mutations can predispose individuals to certain cancers and other genetic disorders. Our Hereditary-Based Testing service includes panels that target specific hereditary cancer syndromes, providing valuable information for early detection, risk assessment, and prevention strategies.",
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
                            rx.list_item("Risk Assessment: Identifying individuals at risk for hereditary cancers."),
                            rx.list_item("Preventive Care: Informing strategies for early detection and prevention of genetic disorders."),
                            rx.list_item("Family Planning: Providing genetic information for informed reproductive decisions."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Panels:",
                            font_weight="bold",
                            margin_top="1rem",
                            margin_bottom="0.5rem",
                            style=mobile_paragraph_style
                        ),
                        rx.unordered_list(
                            rx.list_item("Brain Cancer"),
                            rx.list_item("Hematologic Malignancy"),
                            rx.list_item("Hereditary Pancreatic"),
                            rx.list_item("Whole Exome"),
                            rx.list_item("Actionable Exome"),
                            rx.list_item("Carrier Panel"),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Unlock the potential of genomic insights with our DNA-Based Mutations services. Whether you're focused on somatic mutations in cancer or hereditary-based genetic testing, our comprehensive solutions can guide your research and clinical decisions. Contact Us Today to learn how our advanced mutation analysis services can support your personalized medicine initiatives.",
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
                    p="2", # smaller padding for mobile
                    padding="2rem",
                ),
                footer(),
                width="100%",
                spacing="2" # smaller spacing for mobile 
            ),
            width="100%",
        ),
        margin="0",
        padding="0",
    )