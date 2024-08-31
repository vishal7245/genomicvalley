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

@rx.page(route="/viral-genomics", title="Viral Genomics")
def viral_genomics():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Viral Genomics"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Viral Genomics is the study of viruses at the genetic level, providing deep insights into their structure, evolution, and interaction with hosts. Through advanced genomic techniques, we can identify, characterize, and track viral pathogens, helping in the diagnosis, treatment, and prevention of viral infections. Our Viral Genomics services are designed to address a wide range of needs, from respiratory illnesses to sexually transmitted infections and beyond.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Respiratory Panel Testing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "The Respiratory Panel Testing is focused on detecting and characterizing viruses responsible for respiratory infections, including influenza, RSV, coronaviruses, and others. By analyzing the viral genome, this panel enables accurate identification and monitoring of respiratory pathogens, supporting timely and effective treatment.",
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
                                rx.list_item("Accurate Diagnosis: Identifying viral pathogens responsible for respiratory infections."),
                                rx.list_item("Treatment Planning: Informing therapeutic strategies based on the viral strain."),
                                rx.list_item("Outbreak Monitoring: Supporting the detection and management of respiratory virus outbreaks."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "STI Panel Testing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "The Sexually Transmitted Infections (STI) Panel Testing offers comprehensive genomic analysis for the detection of viruses associated with STIs, such as HIV, HPV, HSV, and others. This testing is crucial for early diagnosis, treatment, and management of sexually transmitted infections.",
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
                                rx.list_item("Early Detection: Identifying viral agents responsible for STIs with high accuracy."),
                                rx.list_item("Patient Management: Supporting the development of effective treatment plans based on the viral profile."),
                                rx.list_item("Public Health: Contributing to the prevention and control of STI spread."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "HepC Testing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Hepatitis C (HepC) Testing involves the genomic analysis of the Hepatitis C virus (HCV) to determine its genotype and resistance profile. This information is vital for tailoring antiviral treatments and achieving the best possible outcomes in patients with HCV infection.",
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
                                rx.list_item("Genotype Identification: Determining the specific HCV genotype for targeted therapy."),
                                rx.list_item("Resistance Profiling: Assessing the presence of mutations that may confer resistance to antiviral drugs."),
                                rx.list_item("Personalized Treatment: Guiding the selection of optimal treatment regimens based on genetic insights."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Adventitious Agent Testing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Adventitious Agent Testing is essential for ensuring the safety of biological products, such as vaccines and therapeutics. This testing involves the detection of unintended viral contaminants that may be present in biopharmaceutical products, safeguarding both patients and the integrity of the product.",
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
                                rx.list_item("Safety Assurance: Detecting viral contaminants in biological products."),
                                rx.list_item("Regulatory Compliance: Meeting stringent regulatory requirements for product safety."),
                                rx.list_item("Product Integrity: Ensuring the purity and safety of biopharmaceuticals through rigorous testing."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Empower your viral research and clinical diagnostics with our comprehensive Viral Genomics services. From respiratory illnesses to STIs and beyond, our cutting-edge genomic analyses provide the insights you need for accurate diagnosis, effective treatment, and robust public health strategies. Contact Us Today to learn more about how our Viral Genomics services can enhance your research and healthcare solutions.",
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
                banner("Viral Genomics"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Viral Genomics is the study of viruses at the genetic level, providing deep insights into their structure, evolution, and interaction with hosts. Through advanced genomic techniques, we can identify, characterize, and track viral pathogens, helping in the diagnosis, treatment, and prevention of viral infections. Our Viral Genomics services are designed to address a wide range of needs, from respiratory illnesses to sexually transmitted infections and beyond.",
                            style=mobile_paragraph_style,
                        ),
                        # Respiratory Panel Testing - Mobile
                        rx.heading(
                            "Respiratory Panel Testing",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "The Respiratory Panel Testing is focused on detecting and characterizing viruses responsible for respiratory infections, including influenza, RSV, coronaviruses, and others. By analyzing the viral genome, this panel enables accurate identification and monitoring of respiratory pathogens, supporting timely and effective treatment.",
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
                            rx.list_item("Accurate Diagnosis: Identifying viral pathogens responsible for respiratory infections."),
                            rx.list_item("Treatment Planning: Informing therapeutic strategies based on the viral strain."),
                            rx.list_item("Outbreak Monitoring: Supporting the detection and management of respiratory virus outbreaks."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # STI Panel Testing - Mobile
                        rx.heading(
                            "STI Panel Testing",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "The Sexually Transmitted Infections (STI) Panel Testing offers comprehensive genomic analysis for the detection of viruses associated with STIs, such as HIV, HPV, HSV, and others. This testing is crucial for early diagnosis, treatment, and management of sexually transmitted infections.",
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
                            rx.list_item("Early Detection: Identifying viral agents responsible for STIs with high accuracy."),
                            rx.list_item("Patient Management: Supporting the development of effective treatment plans based on the viral profile."),
                            rx.list_item("Public Health: Contributing to the prevention and control of STI spread."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # HepC Testing - Mobile
                        rx.heading(
                            "HepC Testing",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Hepatitis C (HepC) Testing involves the genomic analysis of the Hepatitis C virus (HCV) to determine its genotype and resistance profile. This information is vital for tailoring antiviral treatments and achieving the best possible outcomes in patients with HCV infection.",
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
                            rx.list_item("Genotype Identification: Determining the specific HCV genotype for targeted therapy."),
                            rx.list_item("Resistance Profiling: Assessing the presence of mutations that may confer resistance to antiviral drugs."),
                            rx.list_item("Personalized Treatment: Guiding the selection of optimal treatment regimens based on genetic insights."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Adventitious Agent Testing - Mobile
                        rx.heading(
                            "Adventitious Agent Testing",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Adventitious Agent Testing is essential for ensuring the safety of biological products, such as vaccines and therapeutics. This testing involves the detection of unintended viral contaminants that may be present in biopharmaceutical products, safeguarding both patients and the integrity of the product.",
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
                            rx.list_item("Safety Assurance: Detecting viral contaminants in biological products."),
                            rx.list_item("Regulatory Compliance: Meeting stringent regulatory requirements for product safety."),
                            rx.list_item("Product Integrity: Ensuring the purity and safety of biopharmaceuticals through rigorous testing."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Empower your viral research and clinical diagnostics with our comprehensive Viral Genomics services. From respiratory illnesses to STIs and beyond, our cutting-edge genomic analyses provide the insights you need for accurate diagnosis, effective treatment, and robust public health strategies. Contact Us Today to learn more about how our Viral Genomics services can enhance your research and healthcare solutions.",
                            style=mobile_paragraph_style,
                            margin_top="2rem",
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