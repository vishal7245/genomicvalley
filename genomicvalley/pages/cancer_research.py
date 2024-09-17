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


@rx.page(route="/cancer-research", title="Cancer Research")
def cancer_research():
    return rx.section(
        rx.desktop_only(
            rx.vstack(
                navbar(),
                banner("Cancer Research"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Cancer research is a dynamic and multifaceted field that drives the discovery and development of new strategies for preventing, diagnosing, and treating cancer. Through cutting-edge technologies and methodologies, cancer research provides critical insights into the underlying mechanisms of cancer, paving the way for personalized medicine, targeted therapies, and improved patient outcomes. Our comprehensive cancer research services encompass a wide range of studies, each contributing to the broader understanding of cancer biology and therapeutic interventions.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Pan-cancer Studies",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Pan-cancer studies analyze genetic, epigenetic, and molecular alterations across multiple cancer types to identify commonalities and unique features. By integrating data from diverse cancers, these studies uncover shared pathways and biomarkers that drive cancer progression, providing insights that can lead to the development of broad-spectrum cancer therapies.",
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
                                rx.list_item("Molecular Pathway Analysis: Identifying key pathways involved in multiple cancer types."),
                                rx.list_item("Biomarker Identification: Discovering biomarkers that are relevant across various cancers."),
                                rx.list_item("Therapeutic Targeting: Developing treatments that target common molecular mechanisms in different cancers."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Hereditary Cancer Syndromes Testing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Hereditary Cancer Syndromes Testing focuses on identifying genetic mutations that predispose individuals to cancer. By analyzing genes associated with hereditary cancer syndromes, such as BRCA1/2 for breast and ovarian cancer, this service helps in assessing cancer risk, guiding preventive measures, and enabling early detection in at-risk individuals.",
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
                                rx.list_item("Risk Assessment: Identifying individuals with a genetic predisposition to cancer."),
                                rx.list_item("Preventive Strategies: Developing personalized preventive measures for those with hereditary cancer syndromes."),
                                rx.list_item("Family Screening: Offering genetic testing to family members of individuals with identified mutations."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Tumor Microenvironment Studies",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Tumor Microenvironment Studies explore the complex interactions between cancer cells and their surrounding environment, including immune cells, blood vessels, and the extracellular matrix. Understanding the tumor microenvironment is crucial for developing therapies that target not only the cancer cells but also the supportive environment that enables tumor growth and metastasis.",
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
                                rx.list_item("Immunotherapy Development: Identifying targets within the tumor microenvironment for immunotherapy."),
                                rx.list_item("Metastasis Research: Understanding how the microenvironment influences cancer spread."),
                                rx.list_item("Therapeutic Resistance: Investigating how the tumor microenvironment contributes to treatment resistance."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Tumor Profiling",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Tumor Profiling involves comprehensive molecular analysis of a tumor to identify genetic mutations, expression patterns, and other biomarkers that drive cancer. This service enables the development of personalized treatment plans by matching patients with therapies that target the specific molecular characteristics of their tumor.",
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
                                rx.list_item("Personalized Medicine: Tailoring treatment plans based on the molecular profile of a tumor."),
                                rx.list_item("Targeted Therapy Selection: Identifying therapies that are most likely to be effective based on the tumor’s genetic makeup."),
                                rx.list_item("Prognostic Evaluation: Assessing the likely course and outcome of the disease based on tumor profiling."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Liquid Biopsy",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Liquid Biopsy is a minimally invasive technique for detecting and analyzing cancer biomarkers from blood or other body fluids. This service allows for the monitoring of tumor dynamics in real-time, providing insights into treatment efficacy, disease progression, and the emergence of resistance without the need for invasive tissue biopsies.",
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
                                rx.list_item("Early Detection: Detecting cancer at an early stage through circulating tumor DNA (ctDNA) or other biomarkers."),
                                rx.list_item("Treatment Monitoring: Tracking changes in tumor burden during treatment to assess response."),
                                rx.list_item("Resistance Detection: Identifying mutations associated with resistance to targeted therapies."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Mutation Detection",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Mutation Detection focuses on identifying genetic mutations that contribute to cancer development and progression. By analyzing DNA or RNA from tumor samples, this service identifies driver mutations, which can be targeted with specific therapies, and provides valuable information for prognosis and treatment planning.",
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
                                rx.list_item("Target Identification: Discovering mutations that can be targeted with specific cancer therapies."),
                                rx.list_item("Prognostic Markers: Identifying mutations associated with poor or favorable outcomes."),
                                rx.list_item("Treatment Stratification: Classifying patients based on their mutation profile to guide therapy decisions."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Biomarker Discovery",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Biomarker Discovery aims to identify and validate biological markers that can be used for cancer diagnosis, prognosis, and treatment. This service involves the comprehensive analysis of genetic, proteomic, and metabolomic data to uncover biomarkers that provide insights into cancer biology and therapeutic responses.",
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
                                rx.list_item("Diagnostic Biomarkers: Identifying markers that can be used for early and accurate cancer diagnosis."),
                                rx.list_item("Prognostic Biomarkers: Discovering markers that predict the likely course of the disease."),
                                rx.list_item("Predictive Biomarkers: Identifying markers that indicate how a patient is likely to respond to a particular therapy."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Pharmacogenomics Testing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Pharmacogenomics Testing studies how genetic variations influence a patient’s response to drugs. In cancer research, this service is crucial for personalizing treatment plans based on an individual’s genetic makeup. By identifying specific genetic markers, pharmacogenomics testing helps predict which drugs will be most effective or cause the fewest side effects for a particular patient, enabling more targeted and efficient cancer therapies.",
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
                                rx.list_item("Personalized Treatment: Tailoring drug therapies to match a patient’s genetic profile for optimal effectiveness."),
                                rx.list_item("Drug Sensitivity Analysis: Identifying genetic variants that affect how a patient metabolizes and responds to specific cancer drugs."),
                                rx.list_item("Adverse Effect Prediction: Reducing the risk of severe side effects by avoiding drugs that a patient’s genetic profile suggests may be harmful."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.button(
                                "Contact Us Today",
                                on_click=rx.redirect("/contact"),
                                style=button_style,
                            )
                        ),
                        width="60vw",
                        p="4",
                        padding="4rem",
                    ),
                    width="100%",
                    justify="center",
                    padding="4rem",
                ),
                footer(),
            ),
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                navbar(),
                banner("Cancer Research"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Cancer research is a dynamic and multifaceted field that drives the discovery and development of new strategies for preventing, diagnosing, and treating cancer. Through cutting-edge technologies and methodologies, cancer research provides critical insights into the underlying mechanisms of cancer, paving the way for personalized medicine, targeted therapies, and improved patient outcomes. Our comprehensive cancer research services encompass a wide range of studies, each contributing to the broader understanding of cancer biology and therapeutic interventions.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Pan-cancer Studies",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Pan-cancer studies analyze genetic, epigenetic, and molecular alterations across multiple cancer types to identify commonalities and unique features. By integrating data from diverse cancers, these studies uncover shared pathways and biomarkers that drive cancer progression, providing insights that can lead to the development of broad-spectrum cancer therapies.",
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
                            rx.list_item("Molecular Pathway Analysis: Identifying key pathways involved in multiple cancer types."),
                            rx.list_item("Biomarker Identification: Discovering biomarkers that are relevant across various cancers."),
                            rx.list_item("Therapeutic Targeting: Developing treatments that target common molecular mechanisms in different cancers."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Hereditary Cancer Syndromes Testing",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Hereditary Cancer Syndromes Testing focuses on identifying genetic mutations that predispose individuals to cancer. By analyzing genes associated with hereditary cancer syndromes, such as BRCA1/2 for breast and ovarian cancer, this service helps in assessing cancer risk, guiding preventive measures, and enabling early detection in at-risk individuals.",
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
                            rx.list_item("Risk Assessment: Identifying individuals with a genetic predisposition to cancer."),
                            rx.list_item("Preventive Strategies: Developing personalized preventive measures for those with hereditary cancer syndromes."),
                            rx.list_item("Family Screening: Offering genetic testing to family members of individuals with identified mutations."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Tumor Microenvironment Studies",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Tumor Microenvironment Studies explore the complex interactions between cancer cells and their surrounding environment, including immune cells, blood vessels, and the extracellular matrix. Understanding the tumor microenvironment is crucial for developing therapies that target not only the cancer cells but also the supportive environment that enables tumor growth and metastasis.",
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
                            rx.list_item("Immunotherapy Development: Identifying targets within the tumor microenvironment for immunotherapy."),
                            rx.list_item("Metastasis Research: Understanding how the microenvironment influences cancer spread."),
                            rx.list_item("Therapeutic Resistance: Investigating how the tumor microenvironment contributes to treatment resistance."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                                "Tumor Profiling",
                                size="7",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Tumor Profiling involves comprehensive molecular analysis of a tumor to identify genetic mutations, expression patterns, and other biomarkers that drive cancer. This service enables the development of personalized treatment plans by matching patients with therapies that target the specific molecular characteristics of their tumor.",
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
                                rx.list_item("Personalized Medicine: Tailoring treatment plans based on the molecular profile of a tumor."),
                                rx.list_item("Targeted Therapy Selection: Identifying therapies that are most likely to be effective based on the tumor’s genetic makeup."),
                                rx.list_item("Prognostic Evaluation: Assessing the likely course and outcome of the disease based on tumor profiling."),
                                margin_left="2rem",
                                style=mobile_paragraph_style
                            ),
                            rx.heading(
                                "Liquid Biopsy",
                                size="7",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Liquid Biopsy is a minimally invasive technique for detecting and analyzing cancer biomarkers from blood or other body fluids. This service allows for the monitoring of tumor dynamics in real-time, providing insights into treatment efficacy, disease progression, and the emergence of resistance without the need for invasive tissue biopsies.",
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
                                rx.list_item("Early Detection: Detecting cancer at an early stage through circulating tumor DNA (ctDNA) or other biomarkers."),
                                rx.list_item("Treatment Monitoring: Tracking changes in tumor burden during treatment to assess response."),
                                rx.list_item("Resistance Detection: Identifying mutations associated with resistance to targeted therapies."),
                                margin_left="2rem",
                                style=mobile_paragraph_style
                            ),
                            rx.heading(
                                "Mutation Detection",
                                size="7",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Mutation Detection focuses on identifying genetic mutations that contribute to cancer development and progression. By analyzing DNA or RNA from tumor samples, this service identifies driver mutations, which can be targeted with specific therapies, and provides valuable information for prognosis and treatment planning.",
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
                                rx.list_item("Target Identification: Discovering mutations that can be targeted with specific cancer therapies."),
                                rx.list_item("Prognostic Markers: Identifying mutations associated with poor or favorable outcomes."),
                                rx.list_item("Treatment Stratification: Classifying patients based on their mutation profile to guide therapy decisions."),
                                margin_left="2rem",
                                style=mobile_paragraph_style
                            ),
                            rx.heading(
                                "Biomarker Discovery",
                                size="7",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Biomarker Discovery aims to identify and validate biological markers that can be used for cancer diagnosis, prognosis, and treatment. This service involves the comprehensive analysis of genetic, proteomic, and metabolomic data to uncover biomarkers that provide insights into cancer biology and therapeutic responses.",
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
                                rx.list_item("Diagnostic Biomarkers: Identifying markers that can be used for early and accurate cancer diagnosis."),
                                rx.list_item("Prognostic Biomarkers: Discovering markers that predict the likely course of the disease."),
                                rx.list_item("Predictive Biomarkers: Identifying markers that indicate how a patient is likely to respond to a particular therapy."),
                                margin_left="2rem",
                                style=mobile_paragraph_style
                            ),
                            rx.heading(
                                "Pharmacogenomics Testing",
                                size="7",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Pharmacogenomics Testing studies how genetic variations influence a patient’s response to drugs. In cancer research, this service is crucial for personalizing treatment plans based on an individual’s genetic makeup. By identifying specific genetic markers, pharmacogenomics testing helps predict which drugs will be most effective or cause the fewest side effects for a particular patient, enabling more targeted and efficient cancer therapies.",
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
                                rx.list_item("Personalized Treatment: Tailoring drug therapies to match a patient’s genetic profile for optimal effectiveness."),
                                rx.list_item("Drug Sensitivity Analysis: Identifying genetic variants that affect how a patient metabolizes and responds to specific cancer drugs."),
                                rx.list_item("Adverse Effect Prediction: Reducing the risk of severe side effects by avoiding drugs that a patient’s genetic profile suggests may be harmful."),
                                margin_left="2rem",
                                style=mobile_paragraph_style
                            ),
                            rx.button(
                                "Contact Us Today",
                                on_click=rx.redirect("/contact"),
                                style=button_style,
                            )
                    ),
                    width="100%",
                    p="4",
                    padding="2rem",
                ),
                footer(),
                width="100%",
                spacing="4",
            ),
            width="100%",
        )
    )
    