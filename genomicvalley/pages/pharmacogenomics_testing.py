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

@rx.page(route="/pharmacogenomics-testing", title="Pharmacogenomics Testing")
def pharmacogenomics_testing():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Pharmacogenomics Testing"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Pharmacogenomics Testing service offers a comprehensive analysis of genetic factors that influence individual responses to medications. By integrating genomic data with drug efficacy and safety profiles, we provide personalized insights that help optimize medication selection and dosage, minimizing adverse effects and enhancing therapeutic outcomes.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Pharmacogenomics Testing?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Personalized Medication: Tailor drug therapies based on individual genetic profiles to enhance efficacy and reduce the risk of adverse drug reactions, leading to more effective and safer treatments."),
                                rx.list_item("Optimized Dosage: Determine the most appropriate dosage for each patient based on their genetic makeup, ensuring therapeutic levels are achieved without overexposure or underdosing."),
                                rx.list_item("Improved Drug Safety: Identify genetic variants that may affect drug metabolism, efficacy, and toxicity, helping to avoid potentially harmful drug interactions and side effects."),
                                rx.list_item("Enhanced Treatment Outcomes: Improve treatment success rates by selecting medications that are more likely to be effective for each patient, based on their genetic predispositions."),
                                rx.list_item("Support for Precision Medicine: Facilitate the implementation of precision medicine strategies by integrating genetic information into treatment planning, thereby advancing personalized healthcare approaches."),
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
                                rx.list_item("Clinicians & Healthcare Providers: Use pharmacogenomics data to make informed decisions about medication choices and dosages, enhancing patient care and treatment outcomes."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Leverage pharmacogenomics testing to support drug development, optimize clinical trial designs, and improve drug labeling with genetic considerations."),
                                rx.list_item("Researchers: Utilize pharmacogenomics data to study the genetic basis of drug response, identify new therapeutic targets, and advance research in personalized medicine."),
                                rx.list_item("Patients: Benefit from personalized treatment plans that account for genetic variations, improving medication efficacy and minimizing the risk of adverse effects."),
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
                                rx.list_item("Sample Collection: We provide clear guidelines for collecting genetic samples, such as blood or saliva, ensuring high-quality DNA for accurate pharmacogenomics analysis."),
                                rx.list_item("Genomic Analysis: Employ advanced sequencing technologies and genomic assays to identify genetic variants that influence drug metabolism, efficacy, and safety."),
                                rx.list_item("Data Interpretation: Our bioinformatics team analyzes genetic data to assess how specific genetic variants affect drug response and recommend optimal medications and dosages."),
                                rx.list_item("Detailed Reporting: Receive comprehensive reports detailing genetic variants, their impact on drug response, and personalized medication recommendations based on the analysis."),
                                rx.list_item("Consultation & Support: Our team of experts is available to discuss results, provide interpretation, and offer guidance on integrating pharmacogenomics findings into clinical practice."),
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
                                "We are dedicated to delivering high-quality, actionable insights through advanced genomic technologies and rigorous analysis. Our Pharmacogenomics Testing service provides essential information for optimizing medication strategies, enhancing patient care, and advancing personalized medicine.",
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
        ),
        rx.mobile_and_tablet(  # Mobile layout
            rx.vstack(
                navbar(),
                banner("Pharmacogenomics Testing"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Pharmacogenomics Testing service offers a comprehensive analysis of genetic factors that influence individual responses to medications. By integrating genomic data with drug efficacy and safety profiles, we provide personalized insights that help optimize medication selection and dosage, minimizing adverse effects and enhancing therapeutic outcomes.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Pharmacogenomics Testing? - Mobile
                        rx.heading(
                            "Why Choose Pharmacogenomics Testing?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Personalized Medication: Tailor drug therapies based on individual genetic profiles to enhance efficacy and reduce the risk of adverse drug reactions, leading to more effective and safer treatments."),
                            rx.list_item("Optimized Dosage: Determine the most appropriate dosage for each patient based on their genetic makeup, ensuring therapeutic levels are achieved without overexposure or underdosing."),
                            rx.list_item("Improved Drug Safety: Identify genetic variants that may affect drug metabolism, efficacy, and toxicity, helping to avoid potentially harmful drug interactions and side effects."),
                            rx.list_item("Enhanced Treatment Outcomes: Improve treatment success rates by selecting medications that are more likely to be effective for each patient, based on their genetic predispositions."),
                            rx.list_item("Support for Precision Medicine: Facilitate the implementation of precision medicine strategies by integrating genetic information into treatment planning, thereby advancing personalized healthcare approaches."),
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
                            rx.list_item("Clinicians & Healthcare Providers: Use pharmacogenomics data to make informed decisions about medication choices and dosages, enhancing patient care and treatment outcomes."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Leverage pharmacogenomics testing to support drug development, optimize clinical trial designs, and improve drug labeling with genetic considerations."),
                            rx.list_item("Researchers: Utilize pharmacogenomics data to study the genetic basis of drug response, identify new therapeutic targets, and advance research in personalized medicine."),
                            rx.list_item("Patients: Benefit from personalized treatment plans that account for genetic variations, improving medication efficacy and minimizing the risk of adverse effects."),
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
                            rx.list_item("Sample Collection: We provide clear guidelines for collecting genetic samples, such as blood or saliva, ensuring high-quality DNA for accurate pharmacogenomics analysis."),
                            rx.list_item("Genomic Analysis: Employ advanced sequencing technologies and genomic assays to identify genetic variants that influence drug metabolism, efficacy, and safety."),
                            rx.list_item("Data Interpretation: Our bioinformatics team analyzes genetic data to assess how specific genetic variants affect drug response and recommend optimal medications and dosages."),
                            rx.list_item("Detailed Reporting: Receive comprehensive reports detailing genetic variants, their impact on drug response, and personalized medication recommendations based on the analysis."),
                            rx.list_item("Consultation & Support: Our team of experts is available to discuss results, provide interpretation, and offer guidance on integrating pharmacogenomics findings into clinical practice."),
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
                            "We are dedicated to delivering high-quality, actionable insights through advanced genomic technologies and rigorous analysis. Our Pharmacogenomics Testing service provides essential information for optimizing medication strategies, enhancing patient care, and advancing personalized medicine.",
                            style=mobile_paragraph_style,
                            margin_top="1rem",
                            font_weight="bold",
                        ),
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
        )
    )