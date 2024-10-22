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


@rx.page(route="/metagenomics-testing", title="Metagenomics Testing")
def metagenomics_testing():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Metagenomics Testing"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Metagenomics testing opens a window into the complex and diverse microbial communities that inhabit various environments, from the human body to ecosystems across the planet. By analyzing genetic material directly from environmental samples, metagenomics allows researchers to study entire microbial populations in their natural context, bypassing the need for culturing. This advanced approach uncovers the functional capabilities of microbes, identifies pathogens, and sheds light on the intricate relationships within microbial ecosystems.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Shotgun Metagenomics",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Shotgun metagenomics is a comprehensive and unbiased approach to studying microbial communities. Unlike targeted sequencing, shotgun metagenomics sequences all the genetic material in a sample, capturing DNA from bacteria, viruses, fungi, and other microorganisms. This method provides a detailed view of the taxonomic composition, functional potential, and metabolic capabilities of microbial communities, enabling a deep understanding of their roles in various environments.",
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
                                rx.list_item("Microbial Diversity Analysis: Profiling the full spectrum of microbial species within a sample, including rare or previously unknown organisms."),
                                rx.list_item("Functional Genomics: Identifying genes and metabolic pathways involved in critical processes like nutrient cycling, biodegradation, or antibiotic resistance."),
                                rx.list_item("Ecological Studies: Understanding the complex interactions and dynamics within microbial ecosystems, from soil and water environments to the human microbiome."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "Pathogen Detection",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Pathogen detection through metagenomics testing offers a powerful, culture-independent method to identify and characterize pathogens in a variety of samples. By leveraging metagenomic sequencing, this service can detect known and novel pathogens, providing critical insights into infectious diseases, outbreak investigations, and antimicrobial resistance. This approach is particularly valuable in situations where traditional diagnostic methods fail, offering a rapid and accurate tool for pathogen discovery.",
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
                                rx.list_item("Infectious Disease Diagnosis: Rapid identification of pathogens causing infections, especially in cases of unknown etiology."),
                                rx.list_item("Outbreak Investigation: Tracing the source and spread of pathogens in public health emergencies."),
                                rx.list_item("Antimicrobial Resistance Surveillance: Monitoring and detecting resistance genes in pathogenic and commensal organisms."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "16S rRNA Gene Sequencing (16S Metagenomics)",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "16S rRNA gene sequencing, commonly known as 16S metagenomics, is a targeted approach to profiling bacterial communities based on the highly conserved 16S ribosomal RNA gene. This technique selectively amplifies and sequences the 16S rRNA gene, allowing for the precise identification and classification of bacteria present in a sample. While it focuses specifically on bacterial populations, 16S metagenomics is a cost-effective and efficient method for exploring microbial diversity and dynamics, making it a cornerstone of microbial ecology studies.",
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
                                rx.list_item("Microbiome Analysis: Investigating the composition and structure of bacterial communities in various environments, including the human gut, soil, and water."),
                                rx.list_item("Comparative Studies: Comparing bacterial communities across different conditions, treatments, or time points to identify shifts in microbial populations."),
                                rx.list_item("Phylogenetic Studies: Tracing the evolutionary relationships among bacteria, providing insights into their origins and adaptations."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Unlock the secrets of microbial communities with our comprehensive metagenomics testing services. Whether you need an in-depth analysis of microbial diversity, rapid pathogen detection, or precise bacterial profiling through 16S sequencing, our state-of-the-art technologies are designed to meet your research and diagnostic needs. Contact us to discover how metagenomics can drive your scientific discoveries and innovations.",
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
                banner("Metagenomics Testing"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Metagenomics testing opens a window into the complex and diverse microbial communities that inhabit various environments, from the human body to ecosystems across the planet. By analyzing genetic material directly from environmental samples, metagenomics allows researchers to study entire microbial populations in their natural context, bypassing the need for culturing. This advanced approach uncovers the functional capabilities of microbes, identifies pathogens, and sheds light on the intricate relationships within microbial ecosystems.",
                            style=mobile_paragraph_style,
                        ),
                        # Shotgun Metagenomics - Mobile
                        rx.heading(
                            "Shotgun Metagenomics",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Shotgun metagenomics is a comprehensive and unbiased approach to studying microbial communities. Unlike targeted sequencing, shotgun metagenomics sequences all the genetic material in a sample, capturing DNA from bacteria, viruses, fungi, and other microorganisms. This method provides a detailed view of the taxonomic composition, functional potential, and metabolic capabilities of microbial communities, enabling a deep understanding of their roles in various environments.",
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
                            rx.list_item("Microbial Diversity Analysis: Profiling the full spectrum of microbial species within a sample, including rare or previously unknown organisms."),
                            rx.list_item("Functional Genomics: Identifying genes and metabolic pathways involved in critical processes like nutrient cycling, biodegradation, or antibiotic resistance."),
                            rx.list_item("Ecological Studies: Understanding the complex interactions and dynamics within microbial ecosystems, from soil and water environments to the human microbiome."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Pathogen Detection - Mobile
                        rx.heading(
                            "Pathogen Detection",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Pathogen detection through metagenomics testing offers a powerful, culture-independent method to identify and characterize pathogens in a variety of samples. By leveraging metagenomic sequencing, this service can detect known and novel pathogens, providing critical insights into infectious diseases, outbreak investigations, and antimicrobial resistance. This approach is particularly valuable in situations where traditional diagnostic methods fail, offering a rapid and accurate tool for pathogen discovery.",
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
                            rx.list_item("Infectious Disease Diagnosis: Rapid identification of pathogens causing infections, especially in cases of unknown etiology."),
                            rx.list_item("Outbreak Investigation: Tracing the source and spread of pathogens in public health emergencies."),
                            rx.list_item("Antimicrobial Resistance Surveillance: Monitoring and detecting resistance genes in pathogenic and commensal organisms."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # 16S rRNA Gene Sequencing (16S Metagenomics) - Mobile
                        rx.heading(
                            "16S rRNA Gene Sequencing (16S Metagenomics)",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "16S rRNA gene sequencing, commonly known as 16S metagenomics, is a targeted approach to profiling bacterial communities based on the highly conserved 16S ribosomal RNA gene. This technique selectively amplifies and sequences the 16S rRNA gene, allowing for the precise identification and classification of bacteria present in a sample. While it focuses specifically on bacterial populations, 16S metagenomics is a cost-effective and efficient method for exploring microbial diversity and dynamics, making it a cornerstone of microbial ecology studies.",
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
                            rx.list_item("Microbiome Analysis: Investigating the composition and structure of bacterial communities in various environments, including the human gut, soil, and water."),
                            rx.list_item("Comparative Studies: Comparing bacterial communities across different conditions, treatments, or time points to identify shifts in microbial populations."),
                            rx.list_item("Phylogenetic Studies: Tracing the evolutionary relationships among bacteria, providing insights into their origins and adaptations."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Unlock the secrets of microbial communities with our comprehensive metagenomics testing services. Whether you need an in-depth analysis of microbial diversity, rapid pathogen detection, or precise bacterial profiling through 16S sequencing, our state-of-the-art technologies are designed to meet your research and diagnostic needs. Contact us to discover how metagenomics can drive your scientific discoveries and innovations.",
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