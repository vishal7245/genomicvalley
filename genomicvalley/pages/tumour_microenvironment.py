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


@rx.page(route="/tumor-microenvironment-studies", title="Tumor Microenvironment Studies")
def tumor_microenvironment_studies():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Tumor Microenvironment Studies"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Tumor Microenvironment Studies service offers advanced analysis of the tumor microenvironment (TME), providing critical insights into the complex interactions between tumor cells and their surrounding tissue. By employing cutting-edge technologies and comprehensive analytical approaches, we help to elucidate the role of the TME in cancer progression, treatment response, and therapeutic development.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Tumor Microenvironment Studies?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("In-Depth TME Analysis: Our studies explore the multifaceted components of the TME, including immune cells, fibroblasts, extracellular matrix, and blood vessels, to understand their impact on tumor growth, metastasis, and resistance to therapy."),
                                rx.list_item("Identification of Key Biomarkers: By analyzing the TME, we identify biomarkers that can be used to predict disease progression, response to treatment, and patient prognosis, facilitating more effective and personalized treatment strategies."),
                                rx.list_item("Insights into Immunoediting: Gain a deeper understanding of how tumors evade immune surveillance and develop resistance to immunotherapies by studying immune cell interactions and immune checkpoint regulation within the TME."),
                                rx.list_item("Evaluation of Therapeutic Targets: Discover potential therapeutic targets within the TME that can be exploited for developing novel treatment strategies, including targeted therapies and combination therapies."),
                                rx.list_item("Support for Clinical Research: Our studies provide essential data for clinical trials, helping to design more effective trials and interpret results based on the tumor’s microenvironmental context."),
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
                                rx.list_item("Researchers: Utilize our comprehensive TME data to advance cancer research, uncover new mechanisms of tumor progression, and identify innovative therapeutic targets."),
                                rx.list_item("Oncologists & Healthcare Providers: Access detailed insights into the TME to enhance understanding of tumor behavior, tailor treatment plans, and improve patient management."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Leverage our TME analysis to support drug discovery, develop new therapies, and optimize clinical trial designs based on TME-related factors."),
                                rx.list_item("Clinical Trial Teams: Incorporate TME data into trial designs to evaluate the efficacy of new treatments and understand how the TME influences treatment outcomes."),
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
                                rx.list_item("Sample Collection & Preparation: We provide guidelines for collecting and preparing tumor and surrounding tissue samples to ensure high-quality analysis of the TME."),
                                rx.list_item("Omics Analysis: Employ advanced techniques such as single-cell RNA sequencing, proteomics, and spatial transcriptomics to analyze the components and interactions within the TME."),
                                rx.list_item("Bioinformatics & Data Integration: Our bioinformatics team integrates and analyzes multi-dimensional data to identify key features of the TME and their implications for tumor behavior and treatment response."),
                                rx.list_item("Detailed Reporting: Receive comprehensive reports that include insights into TME composition, identified biomarkers, potential therapeutic targets, and recommendations for further research or clinical application."),
                                rx.list_item("Consultation & Support: Our team of experts is available to discuss findings, provide interpretation, and offer guidance on the implications for research, treatment, and clinical trials."),
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
                                "We are committed to delivering high-quality, actionable insights through rigorous analysis and advanced technologies. Our Tumor Microenvironment Studies service provides a comprehensive view of the TME, driving forward research and improving patient outcomes through a deeper understanding of tumor biology.",
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
                banner("Tumor Microenvironment Studies"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Tumor Microenvironment Studies service offers advanced analysis of the tumor microenvironment (TME), providing critical insights into the complex interactions between tumor cells and their surrounding tissue. By employing cutting-edge technologies and comprehensive analytical approaches, we help to elucidate the role of the TME in cancer progression, treatment response, and therapeutic development.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Tumor Microenvironment Studies? - Mobile
                        rx.heading(
                            "Why Choose Tumor Microenvironment Studies?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("In-Depth TME Analysis: Our studies explore the multifaceted components of the TME, including immune cells, fibroblasts, extracellular matrix, and blood vessels, to understand their impact on tumor growth, metastasis, and resistance to therapy."),
                            rx.list_item("Identification of Key Biomarkers: By analyzing the TME, we identify biomarkers that can be used to predict disease progression, response to treatment, and patient prognosis, facilitating more effective and personalized treatment strategies."),
                            rx.list_item("Insights into Immunoediting: Gain a deeper understanding of how tumors evade immune surveillance and develop resistance to immunotherapies by studying immune cell interactions and immune checkpoint regulation within the TME."),
                            rx.list_item("Evaluation of Therapeutic Targets: Discover potential therapeutic targets within the TME that can be exploited for developing novel treatment strategies, including targeted therapies and combination therapies."),
                            rx.list_item("Support for Clinical Research: Our studies provide essential data for clinical trials, helping to design more effective trials and interpret results based on the tumor’s microenvironmental context."),
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
                            rx.list_item("Researchers: Utilize our comprehensive TME data to advance cancer research, uncover new mechanisms of tumor progression, and identify innovative therapeutic targets."),
                            rx.list_item("Oncologists & Healthcare Providers: Access detailed insights into the TME to enhance understanding of tumor behavior, tailor treatment plans, and improve patient management."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Leverage our TME analysis to support drug discovery, develop new therapies, and optimize clinical trial designs based on TME-related factors."),
                            rx.list_item("Clinical Trial Teams: Incorporate TME data into trial designs to evaluate the efficacy of new treatments and understand how the TME influences treatment outcomes."),
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
                            rx.list_item("Sample Collection & Preparation: We provide guidelines for collecting and preparing tumor and surrounding tissue samples to ensure high-quality analysis of the TME."),
                            rx.list_item("Omics Analysis: Employ advanced techniques such as single-cell RNA sequencing, proteomics, and spatial transcriptomics to analyze the components and interactions within the TME."),
                            rx.list_item("Bioinformatics & Data Integration: Our bioinformatics team integrates and analyzes multi-dimensional data to identify key features of the TME and their implications for tumor behavior and treatment response."),
                            rx.list_item("Detailed Reporting: Receive comprehensive reports that include insights into TME composition, identified biomarkers, potential therapeutic targets, and recommendations for further research or clinical application."),
                            rx.list_item("Consultation & Support: Our team of experts is available to discuss findings, provide interpretation, and offer guidance on the implications for research, treatment, and clinical trials."),
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
                            "We are committed to delivering high-quality, actionable insights through rigorous analysis and advanced technologies. Our Tumor Microenvironment Studies service provides a comprehensive view of the TME, driving forward research and improving patient outcomes through a deeper understanding of tumor biology.",
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