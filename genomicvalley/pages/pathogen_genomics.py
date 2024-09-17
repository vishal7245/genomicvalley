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


@rx.page(route="/pathogen-genomics", title="Pathogen Genomics")
def pathogen_genomics():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Pathogen Genomics"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Pathogen Genomics service offers cutting-edge genomic analysis of pathogens, enabling precise identification, characterization, and tracking of infectious agents. By analyzing the genetic material of viruses, bacteria, fungi, and parasites, we provide critical insights into pathogen evolution, virulence factors, drug resistance, and outbreak sources. This service is essential for effective disease management, public health surveillance, and research into infectious diseases.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Pathogen Genomics?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Comprehensive Pathogen Identification: Our advanced sequencing technologies allow for the identification of a wide range of pathogens, from common infectious agents to emerging and hard-to-detect organisms."),
                                rx.list_item("Antimicrobial Resistance (AMR) Profiling: Detect genetic markers associated with antimicrobial resistance, providing vital information for tailoring treatment strategies and combating drug-resistant infections."),
                                rx.list_item("Outbreak Tracking: Utilize whole-genome sequencing (WGS) to trace the transmission of pathogens, monitor outbreaks, and identify the sources of infection, helping to control and prevent the spread of diseases."),
                                rx.list_item("Vaccine and Therapeutic Development: Our genomic analysis provides valuable data for the development of vaccines and therapeutics by identifying key virulence factors and genetic variations that affect pathogen behavior and immune response."),
                                rx.list_item("Tailored Reports for Clinical and Research Needs: Whether for clinical diagnostics, public health initiatives, or academic research, our pathogen genomics reports are customized to provide actionable insights that meet your specific requirements."),
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
                                rx.list_item("Clinicians & Infectious Disease Specialists: Gain precise insights into the genetic makeup of pathogens, enabling accurate diagnosis, treatment selection, and monitoring of infections."),
                                rx.list_item("Public Health Authorities: Use genomic data to track pathogen transmission, detect outbreaks early, and implement effective containment strategies to protect public health."),
                                rx.list_item("Researchers: Explore the genomic diversity of pathogens, understand their mechanisms of resistance and virulence, and contribute to the development of new vaccines and treatments."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Leverage pathogen genomics to drive the development of innovative therapeutics and vaccines targeting specific pathogens or resistance mechanisms."),
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
                                rx.list_item("Sample Collection & Preparation: We provide guidelines for the collection and handling of pathogen samples, ensuring the highest quality for genomic analysis."),
                                rx.list_item("Next-Generation Sequencing (NGS): Our state-of-the-art NGS platforms perform comprehensive sequencing of pathogen genomes, capturing detailed genetic information."),
                                rx.list_item("Bioinformatics Analysis: We utilize advanced bioinformatics pipelines to assemble genomes, identify genetic variants, and profile antimicrobial resistance genes, ensuring accurate and reliable results."),
                                rx.list_item("Detailed Reporting: Our reports provide a thorough analysis of the pathogen's genome, highlighting critical information on identification, resistance, virulence, and transmission pathways."),
                                rx.list_item("Consultation & Support: Our team of genomics experts is available to discuss your results, interpret findings, and provide guidance on how to apply the insights to your clinical or research objectives."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Ensuring Quality and Accuracy",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "We adhere to stringent quality control measures throughout our Pathogen Genomics service, ensuring that our results are accurate, reproducible, and clinically relevant. By staying at the forefront of genomic research, we offer a reliable service that you can trust for critical pathogen analysis.",
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
                banner("Pathogen Genomics"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Pathogen Genomics service offers cutting-edge genomic analysis of pathogens, enabling precise identification, characterization, and tracking of infectious agents. By analyzing the genetic material of viruses, bacteria, fungi, and parasites, we provide critical insights into pathogen evolution, virulence factors, drug resistance, and outbreak sources. This service is essential for effective disease management, public health surveillance, and research into infectious diseases.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Pathogen Genomics? - Mobile
                        rx.heading(
                            "Why Choose Pathogen Genomics?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Comprehensive Pathogen Identification: Our advanced sequencing technologies allow for the identification of a wide range of pathogens, from common infectious agents to emerging and hard-to-detect organisms."),
                            rx.list_item("Antimicrobial Resistance (AMR) Profiling: Detect genetic markers associated with antimicrobial resistance, providing vital information for tailoring treatment strategies and combating drug-resistant infections."),
                            rx.list_item("Outbreak Tracking: Utilize whole-genome sequencing (WGS) to trace the transmission of pathogens, monitor outbreaks, and identify the sources of infection, helping to control and prevent the spread of diseases."),
                            rx.list_item("Vaccine and Therapeutic Development: Our genomic analysis provides valuable data for the development of vaccines and therapeutics by identifying key virulence factors and genetic variations that affect pathogen behavior and immune response."),
                            rx.list_item("Tailored Reports for Clinical and Research Needs: Whether for clinical diagnostics, public health initiatives, or academic research, our pathogen genomics reports are customized to provide actionable insights that meet your specific requirements."),
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
                            rx.list_item("Clinicians & Infectious Disease Specialists: Gain precise insights into the genetic makeup of pathogens, enabling accurate diagnosis, treatment selection, and monitoring of infections."),
                            rx.list_item("Public Health Authorities: Use genomic data to track pathogen transmission, detect outbreaks early, and implement effective containment strategies to protect public health."),
                            rx.list_item("Researchers: Explore the genomic diversity of pathogens, understand their mechanisms of resistance and virulence, and contribute to the development of new vaccines and treatments."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Leverage pathogen genomics to drive the development of innovative therapeutics and vaccines targeting specific pathogens or resistance mechanisms."),
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
                            rx.list_item("Sample Collection & Preparation: We provide guidelines for the collection and handling of pathogen samples, ensuring the highest quality for genomic analysis."),
                            rx.list_item("Next-Generation Sequencing (NGS): Our state-of-the-art NGS platforms perform comprehensive sequencing of pathogen genomes, capturing detailed genetic information."),
                            rx.list_item("Bioinformatics Analysis: We utilize advanced bioinformatics pipelines to assemble genomes, identify genetic variants, and profile antimicrobial resistance genes, ensuring accurate and reliable results."),
                            rx.list_item("Detailed Reporting: Our reports provide a thorough analysis of the pathogen's genome, highlighting critical information on identification, resistance, virulence, and transmission pathways."),
                            rx.list_item("Consultation & Support: Our team of genomics experts is available to discuss your results, interpret findings, and provide guidance on how to apply the insights to your clinical or research objectives."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Ensuring Quality and Accuracy - Mobile
                        rx.heading(
                            "Ensuring Quality and Accuracy",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "We adhere to stringent quality control measures throughout our Pathogen Genomics service, ensuring that our results are accurate, reproducible, and clinically relevant. By staying at the forefront of genomic research, we offer a reliable service that you can trust for critical pathogen analysis.",
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
        )
    )