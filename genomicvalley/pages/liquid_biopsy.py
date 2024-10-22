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


@rx.page(route="/liquid-biopsy", title="Liquid Biopsy")
def liquid_biopsy():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Liquid Biopsy"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Liquid Biopsy service offers a non-invasive approach to cancer diagnosis, monitoring, and personalized treatment by analyzing biomarkers in blood or other bodily fluids. By utilizing advanced technologies and sophisticated analytical methods, we provide valuable insights into tumor dynamics, treatment response, and disease progression, enhancing clinical decision-making and patient care.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Liquid Biopsy?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Non-Invasive Testing: Liquid biopsy provides a less invasive alternative to traditional tissue biopsies, reducing patient discomfort and risk while still offering critical information about the tumor."),
                                rx.list_item("Early Detection and Diagnosis: Detect genetic mutations, tumor-associated biomarkers, and cancer-related changes at an early stage, improving the likelihood of early intervention and successful treatment."),
                                rx.list_item("Monitoring Disease Progression: Regular liquid biopsy testing allows for continuous monitoring of disease status, treatment response, and potential relapse, enabling timely adjustments to treatment plans."),
                                rx.list_item("Assessment of Treatment Response: Evaluate how effectively a treatment is working by analyzing changes in tumor-derived biomarkers, helping to optimize therapeutic strategies and improve patient outcomes."),
                                rx.list_item("Detection of Minimal Residual Disease: Identify residual cancer cells or genetic alterations after treatment, providing insights into disease persistence and guiding subsequent therapeutic decisions."),
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
                                rx.list_item("Oncologists & Healthcare Providers: Use liquid biopsy data to make informed decisions about diagnosis, treatment, and monitoring, enhancing personalized care for cancer patients."),
                                rx.list_item("Researchers: Leverage liquid biopsy findings to study tumor biology, explore new biomarkers, and advance research in cancer diagnostics and therapeutics."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Utilize liquid biopsy data to support drug development, clinical trials, and the evaluation of new therapies based on real-time tumor monitoring."),
                                rx.list_item("Clinical Trial Teams: Incorporate liquid biopsy results into trial designs to evaluate the efficacy of novel treatments, monitor patient responses, and refine therapeutic strategies."),
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
                                rx.list_item("Sample Collection: We provide detailed instructions for the collection of blood or other bodily fluid samples, ensuring high-quality and reliable results for liquid biopsy analysis."),
                                rx.list_item("Biomarker Analysis: Employ advanced technologies such as circulating tumor DNA (ctDNA) sequencing, RNA sequencing, and protein assays to analyze biomarkers associated with tumors."),
                                rx.list_item("Bioinformatics & Data Interpretation: Our bioinformatics team processes and interprets the data to identify relevant biomarkers, genetic mutations, and other indicators of tumor dynamics and treatment response."),
                                rx.list_item("Detailed Reporting: Receive comprehensive reports that outline key findings, including biomarker profiles, insights into disease status, and recommendations for treatment or further monitoring."),
                                rx.list_item("Consultation & Support: Our team of experts is available to discuss results, provide interpretation, and offer guidance on the implications for patient care and research."),
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
                                "We are committed to providing high-quality, actionable insights through state-of-the-art technologies and rigorous analysis. Our Liquid Biopsy service offers a powerful tool for non-invasive cancer diagnosis and management, supporting personalized care and advancing the field of oncology.",
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
                banner("Liquid Biopsy"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Liquid Biopsy service offers a non-invasive approach to cancer diagnosis, monitoring, and personalized treatment by analyzing biomarkers in blood or other bodily fluids. By utilizing advanced technologies and sophisticated analytical methods, we provide valuable insights into tumor dynamics, treatment response, and disease progression, enhancing clinical decision-making and patient care.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Liquid Biopsy? - Mobile
                        rx.heading(
                            "Why Choose Liquid Biopsy?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Non-Invasive Testing: Liquid biopsy provides a less invasive alternative to traditional tissue biopsies, reducing patient discomfort and risk while still offering critical information about the tumor."),
                            rx.list_item("Early Detection and Diagnosis: Detect genetic mutations, tumor-associated biomarkers, and cancer-related changes at an early stage, improving the likelihood of early intervention and successful treatment."),
                            rx.list_item("Monitoring Disease Progression: Regular liquid biopsy testing allows for continuous monitoring of disease status, treatment response, and potential relapse, enabling timely adjustments to treatment plans."),
                            rx.list_item("Assessment of Treatment Response: Evaluate how effectively a treatment is working by analyzing changes in tumor-derived biomarkers, helping to optimize therapeutic strategies and improve patient outcomes."),
                            rx.list_item("Detection of Minimal Residual Disease: Identify residual cancer cells or genetic alterations after treatment, providing insights into disease persistence and guiding subsequent therapeutic decisions."),
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
                            rx.list_item("Oncologists & Healthcare Providers: Use liquid biopsy data to make informed decisions about diagnosis, treatment, and monitoring, enhancing personalized care for cancer patients."),
                            rx.list_item("Researchers: Leverage liquid biopsy findings to study tumor biology, explore new biomarkers, and advance research in cancer diagnostics and therapeutics."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Utilize liquid biopsy data to support drug development, clinical trials, and the evaluation of new therapies based on real-time tumor monitoring."),
                            rx.list_item("Clinical Trial Teams: Incorporate liquid biopsy results into trial designs to evaluate the efficacy of novel treatments, monitor patient responses, and refine therapeutic strategies."),
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
                            rx.list_item("Sample Collection: We provide detailed instructions for the collection of blood or other bodily fluid samples, ensuring high-quality and reliable results for liquid biopsy analysis."),
                            rx.list_item("Biomarker Analysis: Employ advanced technologies such as circulating tumor DNA (ctDNA) sequencing, RNA sequencing, and protein assays to analyze biomarkers associated with tumors."),
                            rx.list_item("Bioinformatics & Data Interpretation: Our bioinformatics team processes and interprets the data to identify relevant biomarkers, genetic mutations, and other indicators of tumor dynamics and treatment response."),
                            rx.list_item("Detailed Reporting: Receive comprehensive reports that outline key findings, including biomarker profiles, insights into disease status, and recommendations for treatment or further monitoring."),
                            rx.list_item("Consultation & Support: Our team of experts is available to discuss results, provide interpretation, and offer guidance on the implications for patient care and research."),
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
                            "We are committed to providing high-quality, actionable insights through state-of-the-art technologies and rigorous analysis. Our Liquid Biopsy service offers a powerful tool for non-invasive cancer diagnosis and management, supporting personalized care and advancing the field of oncology.",
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