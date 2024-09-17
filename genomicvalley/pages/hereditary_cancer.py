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


@rx.page(route="/hereditary-cancer-syndromes-testing", title="Hereditary Cancer Syndromes Testing")
def hereditary_cancer_syndromes_testing():
    return rx.section(
        rx.desktop_only(  # Start of desktop layout
            rx.vstack(
                navbar(),
                banner("Hereditary Cancer Syndromes Testing"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Hereditary Cancer Syndromes Testing service offers advanced genetic analysis to identify inherited mutations associated with various hereditary cancer syndromes. By using cutting-edge genomic technologies, we provide crucial insights into an individual’s genetic risk for specific cancer syndromes, enabling early detection, personalized management, and informed decision-making.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Hereditary Cancer Syndromes Testing?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Early Detection of Genetic Risk: Identifying genetic mutations linked to hereditary cancer syndromes allows for early intervention and surveillance, potentially reducing cancer incidence and improving patient outcomes."),
                                rx.list_item("Comprehensive Genetic Panels: Our testing includes a broad range of cancer syndromes such as BRCA1/BRCA2 (breast and ovarian cancer), Lynch syndrome (colorectal and other cancers), and other well-established hereditary cancer syndromes, providing a thorough assessment of genetic risk."),
                                rx.list_item("Personalized Risk Assessment: By pinpointing specific genetic mutations, we offer personalized risk assessments that inform tailored screening strategies, preventive measures, and treatment options based on individual genetic profiles."),
                                rx.list_item("Informed Family Planning: Genetic testing helps individuals understand their hereditary cancer risks and make informed decisions about family planning, including the potential risk of passing these mutations to future generations."),
                                rx.list_item("Support for Clinical Decision-Making: Healthcare providers can use genetic information to guide clinical decisions, develop personalized care plans, and offer targeted therapies based on the specific genetic mutations identified."),
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
                                rx.list_item("Individuals & Families: Obtain detailed information about hereditary cancer risks, enabling proactive health management, early detection, and personalized preventive strategies."),
                                rx.list_item("Clinicians & Oncologists: Access precise genetic data to enhance diagnostic accuracy, guide treatment decisions, and develop personalized care plans based on hereditary cancer risks."),
                                rx.list_item("Genetic Counselors: Provide comprehensive genetic counseling and support to individuals and families, helping them understand their genetic risks and options for managing hereditary cancer syndromes."),
                                rx.list_item("Researchers: Utilize genetic data to study hereditary cancer syndromes, explore new biomarkers, and advance research into the genetic basis of cancer susceptibility."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Leverage genetic testing data to support the development of targeted therapies and drugs for hereditary cancer syndromes."),
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
                                rx.list_item("Sample Collection: We provide clear instructions for the collection and preparation of biological samples, ensuring accurate and reliable genetic analysis."),
                                rx.list_item("Genetic Sequencing: Using advanced next-generation sequencing (NGS) and targeted genetic panels, we analyze relevant genes associated with hereditary cancer syndromes."),
                                rx.list_item("Bioinformatics Analysis: Our expert bioinformatics team interprets the sequencing data, identifying pathogenic mutations and assessing their clinical significance in relation to hereditary cancer risks."),
                                rx.list_item("Detailed Reporting: Receive comprehensive reports that outline identified genetic mutations, associated cancer risks, and recommendations for further action, including preventive measures and screening."),
                                rx.list_item("Consultation & Support: Our team of genetic experts is available to discuss results, provide insights into the implications for health management, and offer guidance on preventive strategies and family planning."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Commitment to Quality",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "We are dedicated to providing the highest quality results through rigorous analysis and the latest genomic technologies. Our Hereditary Cancer Syndromes Testing service ensures accurate, actionable insights that support effective cancer risk management and personalized patient care.",
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
                banner("Hereditary Cancer Syndromes Testing"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Hereditary Cancer Syndromes Testing service offers advanced genetic analysis to identify inherited mutations associated with various hereditary cancer syndromes. By using cutting-edge genomic technologies, we provide crucial insights into an individual’s genetic risk for specific cancer syndromes, enabling early detection, personalized management, and informed decision-making.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Why Choose Hereditary Cancer Syndromes Testing?",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Early Detection of Genetic Risk: Identifying genetic mutations linked to hereditary cancer syndromes allows for early intervention and surveillance, potentially reducing cancer incidence and improving patient outcomes."),
                            rx.list_item("Comprehensive Genetic Panels: Our testing includes a broad range of cancer syndromes such as BRCA1/BRCA2 (breast and ovarian cancer), Lynch syndrome (colorectal and other cancers), and other well-established hereditary cancer syndromes, providing a thorough assessment of genetic risk."),
                            rx.list_item("Personalized Risk Assessment: By pinpointing specific genetic mutations, we offer personalized risk assessments that inform tailored screening strategies, preventive measures, and treatment options based on individual genetic profiles."),
                            rx.list_item("Informed Family Planning: Genetic testing helps individuals understand their hereditary cancer risks and make informed decisions about family planning, including the potential risk of passing these mutations to future generations."),
                            rx.list_item("Support for Clinical Decision-Making: Healthcare providers can use genetic information to guide clinical decisions, develop personalized care plans, and offer targeted therapies based on the specific genetic mutations identified."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Who Can Benefit?",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Individuals & Families: Obtain detailed information about hereditary cancer risks, enabling proactive health management, early detection, and personalized preventive strategies."),
                            rx.list_item("Clinicians & Oncologists: Access precise genetic data to enhance diagnostic accuracy, guide treatment decisions, and develop personalized care plans based on hereditary cancer risks."),
                            rx.list_item("Genetic Counselors: Provide comprehensive genetic counseling and support to individuals and families, helping them understand their genetic risks and options for managing hereditary cancer syndromes."),
                            rx.list_item("Researchers: Utilize genetic data to study hereditary cancer syndromes, explore new biomarkers, and advance research into the genetic basis of cancer susceptibility."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Leverage genetic testing data to support the development of targeted therapies and drugs for hereditary cancer syndromes."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Our Process",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Sample Collection: We provide clear instructions for the collection and preparation of biological samples, ensuring accurate and reliable genetic analysis."),
                            rx.list_item("Genetic Sequencing: Using advanced next-generation sequencing (NGS) and targeted genetic panels, we analyze relevant genes associated with hereditary cancer syndromes."),
                            rx.list_item("Bioinformatics Analysis: Our expert bioinformatics team interprets the sequencing data, identifying pathogenic mutations and assessing their clinical significance in relation to hereditary cancer risks."),
                            rx.list_item("Detailed Reporting: Receive comprehensive reports that outline identified genetic mutations, associated cancer risks, and recommendations for further action, including preventive measures and screening."),
                            rx.list_item("Consultation & Support: Our team of genetic experts is available to discuss results, provide insights into the implications for health management, and offer guidance on preventive strategies and family planning."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Commitment to Quality",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "We are dedicated to providing the highest quality results through rigorous analysis and the latest genomic technologies. Our Hereditary Cancer Syndromes Testing service ensures accurate, actionable insights that support effective cancer risk management and personalized patient care.",
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
        ) # End of mobile layout
    )