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


@rx.page(route="/data-interpretation", title="Data Interpretation")
def data_interpretation():
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
        rx.desktop_only(  # Start of desktop layout
            rx.vstack(
                navbar(),
                banner("Data Interpretation"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Data Interpretation service provides expert analysis and context for complex biological and experimental data, transforming raw information into actionable insights. By employing advanced analytical techniques and leveraging domain-specific knowledge, we help researchers and organizations understand their data comprehensively, facilitating informed decision-making and driving impactful outcomes.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Data Interpretation?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Expert Analysis: Benefit from the expertise of our data scientists and bioinformaticians who apply sophisticated analytical methods to interpret complex datasets, including genomic, transcriptomic, and proteomic information."),
                                rx.list_item("Contextual Insights: Gain meaningful insights by placing data in the context of biological processes, experimental conditions, and research objectives, enabling a deeper understanding of results."),
                                rx.list_item("Comprehensive Reporting: Receive detailed and clear reports that summarize findings, highlight key results, and provide actionable recommendations based on data interpretation."),
                                rx.list_item("Enhanced Decision-Making: Support strategic decision-making by translating data into practical insights that inform research directions, clinical decisions, and business strategies."),
                                rx.list_item("Custom Solutions: Tailor interpretation services to specific project needs, including hypothesis testing, pattern recognition, and correlation analysis, ensuring relevance to your research or operational goals."),
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
                                rx.list_item("Researchers: Obtain expert interpretation of complex experimental and omics data, facilitating a clear understanding of results and their implications for ongoing research and future studies."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Use data interpretation to inform drug development strategies, optimize clinical trial designs, and understand drug mechanisms and effects."),
                                rx.list_item("Clinical Labs: Leverage data interpretation to support diagnostic and prognostic applications, providing clear insights into genetic and molecular profiles for patient management."),
                                rx.list_item("Academic Institutions: Enhance research capabilities with expert data interpretation, contributing to academic publications and advancing scientific knowledge."),
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
                                rx.list_item("Data Review: Collaborate with our team to review and understand your dataset, including raw data, preprocessing steps, and experimental conditions."),
                                rx.list_item("Analytical Approach: Apply appropriate statistical and computational methods to analyze the data, including hypothesis testing, pattern recognition, and integrative analysis."),
                                rx.list_item("Contextualization: Place data in the context of relevant biological processes, research objectives, and experimental design to provide a comprehensive understanding of findings."),
                                rx.list_item("Result Interpretation: Provide detailed interpretation of results, identifying key patterns, trends, and correlations, and explaining their biological or clinical significance."),
                                rx.list_item("Reporting: Generate comprehensive reports that summarize findings, highlight important results, and offer actionable recommendations based on the interpretation."),
                                rx.list_item("Consultation & Support: Offer ongoing support to discuss results, answer questions, and provide additional insights, ensuring that findings are effectively integrated into research or clinical practice."),
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
                                "We are dedicated to providing high-quality data interpretation services that unlock the full potential of your data and drive meaningful insights. By combining advanced analytical techniques with expert knowledge, our Data Interpretation service ensures that your findings are accurately understood and effectively utilized, supporting informed decision-making and advancing research and clinical outcomes.",
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
                banner("Data Interpretation"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Data Interpretation service provides expert analysis and context for complex biological and experimental data, transforming raw information into actionable insights. By employing advanced analytical techniques and leveraging domain-specific knowledge, we help researchers and organizations understand their data comprehensively, facilitating informed decision-making and driving impactful outcomes.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Why Choose Data Interpretation?",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Expert Analysis: Benefit from the expertise of our data scientists and bioinformaticians who apply sophisticated analytical methods to interpret complex datasets, including genomic, transcriptomic, and proteomic information."),
                            rx.list_item("Contextual Insights: Gain meaningful insights by placing data in the context of biological processes, experimental conditions, and research objectives, enabling a deeper understanding of results."),
                            rx.list_item("Comprehensive Reporting: Receive detailed and clear reports that summarize findings, highlight key results, and provide actionable recommendations based on data interpretation."),
                            rx.list_item("Enhanced Decision-Making: Support strategic decision-making by translating data into practical insights that inform research directions, clinical decisions, and business strategies."),
                            rx.list_item("Custom Solutions: Tailor interpretation services to specific project needs, including hypothesis testing, pattern recognition, and correlation analysis, ensuring relevance to your research or operational goals."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Who Can Benefit?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Researchers: Obtain expert interpretation of complex experimental and omics data, facilitating a clear understanding of results and their implications for ongoing research and future studies."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Use data interpretation to inform drug development strategies, optimize clinical trial designs, and understand drug mechanisms and effects."),
                            rx.list_item("Clinical Labs: Leverage data interpretation to support diagnostic and prognostic applications, providing clear insights into genetic and molecular profiles for patient management."),
                            rx.list_item("Academic Institutions: Enhance research capabilities with expert data interpretation, contributing to academic publications and advancing scientific knowledge."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Our Process",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Data Review: Collaborate with our team to review and understand your dataset, including raw data, preprocessing steps, and experimental conditions."),
                            rx.list_item("Analytical Approach: Apply appropriate statistical and computational methods to analyze the data, including hypothesis testing, pattern recognition, and integrative analysis."),
                            rx.list_item("Contextualization: Place data in the context of relevant biological processes, research objectives, and experimental design to provide a comprehensive understanding of findings."),
                            rx.list_item("Result Interpretation: Provide detailed interpretation of results, identifying key patterns, trends, and correlations, and explaining their biological or clinical significance."),
                            rx.list_item("Reporting: Generate comprehensive reports that summarize findings, highlight important results, and offer actionable recommendations based on the interpretation."),
                            rx.list_item("Consultation & Support: Offer ongoing support to discuss results, answer questions, and provide additional insights, ensuring that findings are effectively integrated into research or clinical practice."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Commitment to Excellence",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "We are dedicated to providing high-quality data interpretation services that unlock the full potential of your data and drive meaningful insights. By combining advanced analytical techniques with expert knowledge, our Data Interpretation service ensures that your findings are accurately understood and effectively utilized, supporting informed decision-making and advancing research and clinical outcomes.",
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