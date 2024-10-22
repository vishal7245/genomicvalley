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


@rx.page(route="/biomarker-discovery", title="Biomarker Discovery")
def biomarker_discovery():
    return rx.section(
        rx.desktop_only(  # Start of desktop layout
            rx.vstack(
                navbar(),
                banner("Biomarker Discovery"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Biomarker discovery is at the forefront of personalized medicine, offering a powerful tool for detecting, diagnosing, and monitoring diseases at the molecular level. By identifying specific biological markers associated with different types of cancer, researchers can develop targeted therapies, improve early detection, and enhance patient outcomes. Our biomarker discovery services provide comprehensive research panels tailored to specific cancers, enabling precise and actionable insights into disease mechanisms and treatment responses.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Breast Cancer Research Panel",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "The Breast Cancer Research Panel is designed to uncover biomarkers associated with the onset, progression, and treatment response of breast cancer. This panel focuses on identifying genetic mutations, gene expression patterns, and protein markers that are critical for understanding breast cancer biology. By leveraging this panel, researchers can explore key pathways involved in hormone receptor status, HER2 expression, and other molecular subtypes, paving the way for personalized treatment strategies.",
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
                                rx.list_item("Early Detection: Identifying biomarkers for early diagnosis of breast cancer, improving prognosis and survival rates."),
                                rx.list_item("Therapeutic Targeting: Discovering markers that guide the selection of targeted therapies, such as hormone therapy or HER2 inhibitors."),
                                rx.list_item("Monitoring Treatment Response: Assessing changes in biomarker levels to evaluate the effectiveness of treatments and detect recurrence."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Colorectal Cancer Research Panel",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "The Colorectal Cancer Research Panel is tailored to identify biomarkers that play a pivotal role in the development and progression of colorectal cancer. This panel targets genetic mutations, epigenetic changes, and protein alterations associated with colorectal cancer, enabling researchers to understand the molecular drivers of the disease. The insights gained from this panel can lead to the development of targeted therapies and improve screening methods.",
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
                                rx.list_item("Risk Assessment: Identifying genetic markers that indicate a higher risk of developing colorectal cancer, facilitating preventive measures."),
                                rx.list_item("Targeted Therapy Development: Discovering biomarkers that can be targeted by novel therapies, particularly in cases with specific mutations such as KRAS, BRAF, or MSI status."),
                                rx.list_item("Prognosis and Monitoring: Using biomarkers to predict disease progression and monitor treatment effectiveness."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Brain Cancer Research Panel",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "The Brain Cancer Research Panel is focused on uncovering biomarkers specific to brain tumors, including gliomas, meningiomas, and other central nervous system cancers. This panel analyzes genetic alterations, protein expressions, and epigenetic modifications to provide insights into tumor biology, treatment resistance, and patient prognosis. The panel supports the development of precision medicine approaches tailored to the unique challenges of brain cancer.",
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
                                rx.list_item("Tumor Classification: Identifying biomarkers that distinguish between different types of brain tumors, aiding in accurate diagnosis and treatment planning."),
                                rx.list_item("Targeting Treatment Resistance: Discovering markers associated with resistance to therapies such as temozolomide or radiation, guiding the development of alternative treatments."),
                                rx.list_item("Patient Prognosis: Using biomarkers to predict patient outcomes and tailor treatment strategies accordingly."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Lung Cancer Research Panel",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "The Lung Cancer Research Panel is designed to identify biomarkers that drive the initiation, progression, and therapeutic response of lung cancer. This panel focuses on detecting genetic mutations, gene expression profiles, and protein markers that are crucial for understanding the heterogeneity of lung cancer. The panel supports the development of targeted therapies and helps in optimizing treatment regimens based on individual patient profiles.",
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
                                rx.list_item("Molecular Profiling: Identifying biomarkers that classify lung cancer subtypes, such as non-small cell lung cancer (NSCLC) and small cell lung cancer (SCLC)."),
                                rx.list_item("Targeted Therapy Selection: Discovering biomarkers for selecting and monitoring targeted treatments, including EGFR inhibitors, ALK inhibitors, and immunotherapies."),
                                rx.list_item("Treatment Monitoring: Using biomarkers to track treatment efficacy and detect early signs of resistance or recurrence."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Comprehensive Cancer Research Panel",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "The Comprehensive Cancer Research Panel provides a broad and in-depth analysis of biomarkers across multiple cancer types. This panel integrates data from various cancer-specific panels, offering a holistic view of the molecular landscape of cancers. It is ideal for studies focused on cancer genomics, drug discovery, and the identification of biomarkers with cross-cancer relevance. The panel enables a comprehensive understanding of cancer biology, facilitating the development of universal biomarkers and therapeutic targets.",
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
                                rx.list_item("Cross-Cancer Analysis: Identifying biomarkers that are relevant across different types of cancers, providing insights into shared and unique molecular features."),
                                rx.list_item("Personalized Medicine: Supporting the development of personalized treatment strategies that consider the complex interplay of biomarkers across multiple cancers."),
                                rx.list_item("Drug Discovery: Discovering potential biomarkers for the development of novel cancer therapies with broad-spectrum efficacy."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Elevate your cancer research with our advanced biomarker discovery services. Whether you’re focused on a specific cancer type or seeking comprehensive insights across multiple cancers, our specialized research panels provide the tools you need to drive breakthroughs in diagnosis, treatment, and personalized medicine. Contact us to learn how our expertise in biomarker discovery can empower your research and clinical innovations.",
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
                banner("Biomarker Discovery"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Biomarker discovery is at the forefront of personalized medicine, offering a powerful tool for detecting, diagnosing, and monitoring diseases at the molecular level. By identifying specific biological markers associated with different types of cancer, researchers can develop targeted therapies, improve early detection, and enhance patient outcomes. Our biomarker discovery services provide comprehensive research panels tailored to specific cancers, enabling precise and actionable insights into disease mechanisms and treatment responses.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Breast Cancer Research Panel",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "The Breast Cancer Research Panel is designed to uncover biomarkers associated with the onset, progression, and treatment response of breast cancer. This panel focuses on identifying genetic mutations, gene expression patterns, and protein markers that are critical for understanding breast cancer biology. By leveraging this panel, researchers can explore key pathways involved in hormone receptor status, HER2 expression, and other molecular subtypes, paving the way for personalized treatment strategies.",
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
                            rx.list_item("Early Detection: Identifying biomarkers for early diagnosis of breast cancer, improving prognosis and survival rates."),
                            rx.list_item("Therapeutic Targeting: Discovering markers that guide the selection of targeted therapies, such as hormone therapy or HER2 inhibitors."),
                            rx.list_item("Monitoring Treatment Response: Assessing changes in biomarker levels to evaluate the effectiveness of treatments and detect recurrence."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Colorectal Cancer Research Panel",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "The Colorectal Cancer Research Panel is tailored to identify biomarkers that play a pivotal role in the development and progression of colorectal cancer. This panel targets genetic mutations, epigenetic changes, and protein alterations associated with colorectal cancer, enabling researchers to understand the molecular drivers of the disease. The insights gained from this panel can lead to the development of targeted therapies and improve screening methods.",
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
                            rx.list_item("Risk Assessment: Identifying genetic markers that indicate a higher risk of developing colorectal cancer, facilitating preventive measures."),
                            rx.list_item("Targeted Therapy Development: Discovering biomarkers that can be targeted by novel therapies, particularly in cases with specific mutations such as KRAS, BRAF, or MSI status."),
                            rx.list_item("Prognosis and Monitoring: Using biomarkers to predict disease progression and monitor treatment effectiveness."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Brain Cancer Research Panel",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "The Brain Cancer Research Panel is focused on uncovering biomarkers specific to brain tumors, including gliomas, meningiomas, and other central nervous system cancers. This panel analyzes genetic alterations, protein expressions, and epigenetic modifications to provide insights into tumor biology, treatment resistance, and patient prognosis. The panel supports the development of precision medicine approaches tailored to the unique challenges of brain cancer.",
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
                            rx.list_item("Tumor Classification: Identifying biomarkers that distinguish between different types of brain tumors, aiding in accurate diagnosis and treatment planning."),
                            rx.list_item("Targeting Treatment Resistance: Discovering markers associated with resistance to therapies such as temozolomide or radiation, guiding the development of alternative treatments."),
                            rx.list_item("Patient Prognosis: Using biomarkers to predict patient outcomes and tailor treatment strategies accordingly."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Lung Cancer Research Panel",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "The Lung Cancer Research Panel is designed to identify biomarkers that drive the initiation, progression, and therapeutic response of lung cancer. This panel focuses on detecting genetic mutations, gene expression profiles, and protein markers that are crucial for understanding the heterogeneity of lung cancer. The panel supports the development of targeted therapies and helps in optimizing treatment regimens based on individual patient profiles.",
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
                            rx.list_item("Molecular Profiling: Identifying biomarkers that classify lung cancer subtypes, such as non-small cell lung cancer (NSCLC) and small cell lung cancer (SCLC)."),
                            rx.list_item("Targeted Therapy Selection: Discovering biomarkers for selecting and monitoring targeted treatments, including EGFR inhibitors, ALK inhibitors, and immunotherapies."),
                            rx.list_item("Treatment Monitoring: Using biomarkers to track treatment efficacy and detect early signs of resistance or recurrence."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Comprehensive Cancer Research Panel",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "The Comprehensive Cancer Research Panel provides a broad and in-depth analysis of biomarkers across multiple cancer types. This panel integrates data from various cancer-specific panels, offering a holistic view of the molecular landscape of cancers. It is ideal for studies focused on cancer genomics, drug discovery, and the identification of biomarkers with cross-cancer relevance. The panel enables a comprehensive understanding of cancer biology, facilitating the development of universal biomarkers and therapeutic targets.",
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
                            rx.list_item("Cross-Cancer Analysis: Identifying biomarkers that are relevant across different types of cancers, providing insights into shared and unique molecular features."),
                            rx.list_item("Personalized Medicine: Supporting the development of personalized treatment strategies that consider the complex interplay of biomarkers across multiple cancers."),
                            rx.list_item("Drug Discovery: Discovering potential biomarkers for the development of novel cancer therapies with broad-spectrum efficacy."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Elevate your cancer research with our advanced biomarker discovery services. Whether you’re focused on a specific cancer type or seeking comprehensive insights across multiple cancers, our specialized research panels provide the tools you need to drive breakthroughs in diagnosis, treatment, and personalized medicine. Contact us to learn how our expertise in biomarker discovery can empower your research and clinical innovations.",
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