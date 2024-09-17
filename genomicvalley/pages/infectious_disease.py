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


@rx.page(route="/infectious-disease", title="Infectious Disease")
def infectious_disease():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Infectious Disease"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Infectious diseases remain a significant global health challenge, with the ability to cause widespread illness and death. Advanced genomic technologies have revolutionized our understanding of these diseases, enabling precise pathogen identification, resistance profiling, and viral characterization. Our Infectious Disease services offer comprehensive solutions to study and combat pathogens, helping to improve diagnosis, treatment, and prevention strategies.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Pathogen Genomics",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Pathogen Genomics involves the in-depth sequencing and analysis of microbial genomes to identify pathogens, understand their virulence factors, and track their spread. This service is crucial for identifying outbreaks, developing targeted therapies, and monitoring the evolution of infectious agents.",
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
                                rx.list_item("Outbreak Detection: Identifying and tracking the spread of infectious pathogens."),
                                rx.list_item("Therapeutic Targeting: Informing the development of targeted treatments based on pathogen genetic profiles."),
                                rx.list_item("Surveillance: Monitoring pathogen evolution and resistance patterns over time."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Antibiotic Resistance (AMR) Studies",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Antibiotic Resistance (AMR) Studies focus on understanding how bacteria develop resistance to antibiotics, which is a growing global health threat. Through genomic analysis, we identify resistance genes, track their spread, and provide insights that guide effective treatment and containment strategies.",
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
                                rx.list_item("Resistance Profiling: Identifying genes responsible for antibiotic resistance in bacterial pathogens."),
                                rx.list_item("Treatment Optimization: Guiding the selection of effective antibiotics based on resistance data."),
                                rx.list_item("Public Health: Supporting efforts to combat the spread of antibiotic-resistant bacteria."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Viral Genomics",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Viral Genomics is dedicated to the study of viruses at the genetic level, providing crucial insights into their structure, function, and evolution. This service is essential for identifying viral pathogens, understanding their mechanisms of infection, and developing vaccines and antiviral therapies.",
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
                                rx.list_item("Viral Identification: Detecting and characterizing viral pathogens."),
                                rx.list_item("Vaccine Development: Informing the design of vaccines based on viral genetic information."),
                                rx.list_item("Epidemiology: Tracking the spread and mutation of viral strains during outbreaks."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Stay ahead in the fight against infectious diseases with our comprehensive genomic services. Whether you’re focused on pathogen detection, combating antibiotic resistance, or understanding viral threats, our expertise in infectious disease genomics can help you achieve your research and healthcare goals. Contact Us Today to learn more about how our Infectious Disease services can enhance your research and clinical strategies.",
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
        ),
        rx.mobile_and_tablet(  # Mobile layout
            rx.vstack(
                navbar(),
                banner("Infectious Disease"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Infectious diseases remain a significant global health challenge, with the ability to cause widespread illness and death. Advanced genomic technologies have revolutionized our understanding of these diseases, enabling precise pathogen identification, resistance profiling, and viral characterization. Our Infectious Disease services offer comprehensive solutions to study and combat pathogens, helping to improve diagnosis, treatment, and prevention strategies.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Pathogen Genomics",
                            size="7",  # Smaller heading size
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Pathogen Genomics involves the in-depth sequencing and analysis of microbial genomes to identify pathogens, understand their virulence factors, and track their spread. This service is crucial for identifying outbreaks, developing targeted therapies, and monitoring the evolution of infectious agents.",
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
                            rx.list_item("Outbreak Detection: Identifying and tracking the spread of infectious pathogens."),
                            rx.list_item("Therapeutic Targeting: Informing the development of targeted treatments based on pathogen genetic profiles."),
                            rx.list_item("Surveillance: Monitoring pathogen evolution and resistance patterns over time."),
                            margin_left="1rem",  # Smaller margin
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Antibiotic Resistance (AMR) Studies",
                            size="7",  # Smaller heading size
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Antibiotic Resistance (AMR) Studies focus on understanding how bacteria develop resistance to antibiotics, which is a growing global health threat. Through genomic analysis, we identify resistance genes, track their spread, and provide insights that guide effective treatment and containment strategies.",
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
                            rx.list_item("Resistance Profiling: Identifying genes responsible for antibiotic resistance in bacterial pathogens."),
                            rx.list_item("Treatment Optimization: Guiding the selection of effective antibiotics based on resistance data."),
                            rx.list_item("Public Health: Supporting efforts to combat the spread of antibiotic-resistant bacteria."),
                            margin_left="1rem",  # Smaller margin
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Viral Genomics",
                            size="7",  # Smaller heading size
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Viral Genomics is dedicated to the study of viruses at the genetic level, providing crucial insights into their structure, function, and evolution. This service is essential for identifying viral pathogens, understanding their mechanisms of infection, and developing vaccines and antiviral therapies.",
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
                            rx.list_item("Viral Identification: Detecting and characterizing viral pathogens."),
                            rx.list_item("Vaccine Development: Informing the design of vaccines based on viral genetic information."),
                            rx.list_item("Epidemiology: Tracking the spread and mutation of viral strains during outbreaks."),
                            margin_left="1rem",  # Smaller margin
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Stay ahead in the fight against infectious diseases with our comprehensive genomic services. Whether you’re focused on pathogen detection, combating antibiotic resistance, or understanding viral threats, our expertise in infectious disease genomics can help you achieve your research and healthcare goals. Contact Us Today to learn more about how our Infectious Disease services can enhance your research and clinical strategies.",
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
                    p="2",  # Smaller padding
                    padding="2rem",
                ),
                footer(),
                width="100%",
                spacing="2"  # Smaller spacing
            ),
            width="100%",
        )
    )