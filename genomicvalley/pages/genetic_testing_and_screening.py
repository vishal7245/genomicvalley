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


@rx.page(route="/genetic-testing-and-screening", title="Genetic Testing and Screening")
def genetic_testing_and_screening():
    return rx.section(
        rx.desktop_only(  # Start of desktop layout
            rx.vstack(
                navbar(),
                banner("Genetic Testing and Screening"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Genetic Testing and Screening service offers comprehensive genomic analysis to identify genetic predispositions, diagnose inherited conditions, and guide personalized healthcare. By utilizing advanced genomic technologies, we provide critical insights into an individual’s genetic profile, supporting informed decision-making in both clinical and personal contexts.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Genetic Testing and Screening?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Personalized Health Insights: Genetic testing reveals an individual’s genetic predispositions to various conditions, including hereditary diseases, cancer risks, and more. This information allows for tailored health management strategies and proactive care."),
                                rx.list_item("Early Detection and Diagnosis: Early identification of genetic mutations can lead to early diagnosis of genetic disorders and conditions, enabling timely intervention and potentially improving health outcomes."),
                                rx.list_item("Carrier Screening: Identify carrier status for genetic conditions that may be passed to offspring. This is crucial for family planning and understanding the risk of inherited diseases within families."),
                                rx.list_item("Risk Assessment for Common Conditions: Assess genetic risk factors for common diseases such as cardiovascular disorders, diabetes, and cancer, enabling personalized preventive measures and lifestyle modifications."),
                                rx.list_item("Informed Family Planning: Genetic screening provides valuable information for prospective parents, helping to assess the risk of passing genetic conditions to their children and make informed family planning decisions."),
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
                                rx.list_item("Individuals & Families: Gain insights into your genetic makeup, identify potential health risks, and make informed decisions about your health and family planning."),
                                rx.list_item("Clinicians & Healthcare Providers: Use genetic information to enhance patient care by incorporating genetic risk assessments into diagnostic and treatment plans."),
                                rx.list_item("Genetic Counselors: Provide comprehensive counseling based on genetic test results to support individuals and families in understanding their genetic risks and options."),
                                rx.list_item("Researchers: Utilize genetic data to advance research in genetics, study disease mechanisms, and develop new therapeutic approaches."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Leverage genetic testing data to support drug development, personalized medicine, and targeted therapies."),
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
                                rx.list_item("Sample Collection: We provide detailed instructions for the collection of blood, saliva, or other biological samples to ensure the accuracy of genetic testing."),
                                rx.list_item("Genetic Analysis: Using advanced sequencing technologies and screening methods, we analyze genetic material to identify relevant genetic variants and predispositions."),
                                rx.list_item("Bioinformatics Interpretation: Our expert bioinformatics team interprets the genetic data, assessing the clinical significance of identified variants and providing actionable insights."),
                                rx.list_item("Detailed Reporting: Receive comprehensive reports that outline genetic findings, their implications for health, and recommendations for further action or monitoring."),
                                rx.list_item("Consultation & Support: Our team of genetic experts is available to discuss results, provide interpretation, and offer guidance on the next steps in healthcare management or family planning."),
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
                                "We adhere to the highest standards of accuracy and reliability in genetic testing and screening. Our commitment to quality ensures that you receive precise and actionable genetic information, empowering you to make informed health decisions and improve outcomes.",
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
                banner("Genetic Testing and Screening"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Genetic Testing and Screening service offers comprehensive genomic analysis to identify genetic predispositions, diagnose inherited conditions, and guide personalized healthcare. By utilizing advanced genomic technologies, we provide critical insights into an individual’s genetic profile, supporting informed decision-making in both clinical and personal contexts.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Why Choose Genetic Testing and Screening?",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Personalized Health Insights: Genetic testing reveals an individual’s genetic predispositions to various conditions, including hereditary diseases, cancer risks, and more. This information allows for tailored health management strategies and proactive care."),
                            rx.list_item("Early Detection and Diagnosis: Early identification of genetic mutations can lead to early diagnosis of genetic disorders and conditions, enabling timely intervention and potentially improving health outcomes."),
                            rx.list_item("Carrier Screening: Identify carrier status for genetic conditions that may be passed to offspring. This is crucial for family planning and understanding the risk of inherited diseases within families."),
                            rx.list_item("Risk Assessment for Common Conditions: Assess genetic risk factors for common diseases such as cardiovascular disorders, diabetes, and cancer, enabling personalized preventive measures and lifestyle modifications."),
                            rx.list_item("Informed Family Planning: Genetic screening provides valuable information for prospective parents, helping to assess the risk of passing genetic conditions to their children and make informed family planning decisions."),
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
                            rx.list_item("Individuals & Families: Gain insights into your genetic makeup, identify potential health risks, and make informed decisions about your health and family planning."),
                            rx.list_item("Clinicians & Healthcare Providers: Use genetic information to enhance patient care by incorporating genetic risk assessments into diagnostic and treatment plans."),
                            rx.list_item("Genetic Counselors: Provide comprehensive counseling based on genetic test results to support individuals and families in understanding their genetic risks and options."),
                            rx.list_item("Researchers: Utilize genetic data to advance research in genetics, study disease mechanisms, and develop new therapeutic approaches."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Leverage genetic testing data to support drug development, personalized medicine, and targeted therapies."),
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
                            rx.list_item("Sample Collection: We provide detailed instructions for the collection of blood, saliva, or other biological samples to ensure the accuracy of genetic testing."),
                            rx.list_item("Genetic Analysis: Using advanced sequencing technologies and screening methods, we analyze genetic material to identify relevant genetic variants and predispositions."),
                            rx.list_item("Bioinformatics Interpretation: Our expert bioinformatics team interprets the genetic data, assessing the clinical significance of identified variants and providing actionable insights."),
                            rx.list_item("Detailed Reporting: Receive comprehensive reports that outline genetic findings, their implications for health, and recommendations for further action or monitoring."),
                            rx.list_item("Consultation & Support: Our team of genetic experts is available to discuss results, provide interpretation, and offer guidance on the next steps in healthcare management or family planning."),
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
                            "We adhere to the highest standards of accuracy and reliability in genetic testing and screening. Our commitment to quality ensures that you receive precise and actionable genetic information, empowering you to make informed health decisions and improve outcomes.",
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