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


@rx.page(route="/genetic-disorders", title="Genetic Disorders")
def genetic_disorders():
    return rx.section(
        rx.desktop_only(  # Start of desktop layout
            rx.vstack(
                navbar(),
                banner("Genetic Disorders"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Genetic disorders, caused by variations or mutations in an individual’s DNA, can have profound effects on health and development. Understanding these disorders through advanced genomic testing is key to accurate diagnosis, informed treatment, and better management of genetic conditions. Our Genetic Disorders services are designed to provide comprehensive insights into a wide range of genetic conditions, from rare diseases to Mendelian disorders.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Rare Disease Genomics",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Rare Disease Genomics focuses on the identification and characterization of genetic mutations responsible for rare diseases, which often remain undiagnosed due to their low prevalence. By using whole-genome sequencing (WGS) or targeted gene panels, we provide a precise diagnosis that can guide treatment and management for these often-complex conditions.",
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
                                rx.list_item("Accurate Diagnosis: Identifying the genetic basis of rare and undiagnosed diseases."),
                                rx.list_item("Personalized Care: Informing treatment strategies tailored to the specific genetic mutation."),
                                rx.list_item("Family Planning: Offering insights into the hereditary nature of rare diseases for better family planning."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Mendelian Disorders Testing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Mendelian Disorders Testing focuses on genetic conditions that follow Mendelian inheritance patterns, such as cystic fibrosis, sickle cell anemia, and Huntington's disease. Our testing services offer comprehensive analysis to detect mutations in specific genes responsible for these disorders, aiding in diagnosis, carrier screening, and risk assessment.",
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
                                rx.list_item("Carrier Screening: Identifying carriers of Mendelian disorders to inform family planning."),
                                rx.list_item("Early Diagnosis: Providing early detection of Mendelian disorders for timely intervention."),
                                rx.list_item("Risk Assessment: Evaluating the likelihood of passing genetic disorders to offspring."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Genetic Testing and Screening",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Genetic Testing and Screening services offer a broad approach to identifying genetic mutations that may increase the risk of developing certain conditions. Whether for newborn screening, prenatal testing, or general health risk assessments, our comprehensive genetic testing helps individuals and families make informed decisions about their health and well-being.",
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
                                rx.list_item("Newborn Screening: Early detection of genetic disorders in newborns for immediate intervention."),
                                rx.list_item("Prenatal Testing: Assessing genetic risks during pregnancy to prepare for potential outcomes."),
                                rx.list_item("Health Risk Assessment: Evaluating genetic predispositions to various health conditions for proactive care."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Unlock the power of genomics in understanding and managing genetic disorders. Whether you're dealing with rare diseases, Mendelian conditions, or seeking general genetic screening, our services provide the critical insights needed for informed healthcare decisions. Contact Us Today to explore our Genetic Disorders services and find out how we can support you in achieving better health outcomes through advanced genomic testing.",
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
                banner("Genetic Disorders"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Genetic disorders, caused by variations or mutations in an individual’s DNA, can have profound effects on health and development. Understanding these disorders through advanced genomic testing is key to accurate diagnosis, informed treatment, and better management of genetic conditions. Our Genetic Disorders services are designed to provide comprehensive insights into a wide range of genetic conditions, from rare diseases to Mendelian disorders.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Rare Disease Genomics",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Rare Disease Genomics focuses on the identification and characterization of genetic mutations responsible for rare diseases, which often remain undiagnosed due to their low prevalence. By using whole-genome sequencing (WGS) or targeted gene panels, we provide a precise diagnosis that can guide treatment and management for these often-complex conditions.",
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
                            rx.list_item("Accurate Diagnosis: Identifying the genetic basis of rare and undiagnosed diseases."),
                            rx.list_item("Personalized Care: Informing treatment strategies tailored to the specific genetic mutation."),
                            rx.list_item("Family Planning: Offering insights into the hereditary nature of rare diseases for better family planning."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Mendelian Disorders Testing",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Mendelian Disorders Testing focuses on genetic conditions that follow Mendelian inheritance patterns, such as cystic fibrosis, sickle cell anemia, and Huntington's disease. Our testing services offer comprehensive analysis to detect mutations in specific genes responsible for these disorders, aiding in diagnosis, carrier screening, and risk assessment.",
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
                            rx.list_item("Carrier Screening: Identifying carriers of Mendelian disorders to inform family planning."),
                            rx.list_item("Early Diagnosis: Providing early detection of Mendelian disorders for timely intervention."),
                            rx.list_item("Risk Assessment: Evaluating the likelihood of passing genetic disorders to offspring."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Genetic Testing and Screening",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Genetic Testing and Screening services offer a broad approach to identifying genetic mutations that may increase the risk of developing certain conditions. Whether for newborn screening, prenatal testing, or general health risk assessments, our comprehensive genetic testing helps individuals and families make informed decisions about their health and well-being.",
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
                            rx.list_item("Newborn Screening: Early detection of genetic disorders in newborns for immediate intervention."),
                            rx.list_item("Prenatal Testing: Assessing genetic risks during pregnancy to prepare for potential outcomes."),
                            rx.list_item("Health Risk Assessment: Evaluating genetic predispositions to various health conditions for proactive care."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Unlock the power of genomics in understanding and managing genetic disorders. Whether you're dealing with rare diseases, Mendelian conditions, or seeking general genetic screening, our services provide the critical insights needed for informed healthcare decisions. Contact Us Today to explore our Genetic Disorders services and find out how we can support you in achieving better health outcomes through advanced genomic testing.",
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