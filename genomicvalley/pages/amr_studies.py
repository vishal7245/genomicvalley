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


@rx.page(route="/amr-studies", title="Antibiotic Resistance (AMR) Studies")
def amr_studies():
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
                banner("Antibiotic Resistance (AMR) Studies"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Antibiotic resistance (AMR) is a growing global health challenge, leading to infections that are harder to treat and increasing the risk of disease spread, severe illness, and death. Our AMR Studies focus on understanding and combating this threat by identifying resistance mechanisms, tracking the spread of resistance, and guiding the development of effective treatment strategies.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "AMR Panel",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "The AMR Panel is designed to detect a wide range of antibiotic resistance genes in various pathogens. By identifying these genes, this panel helps in understanding the resistance profile of infectious agents, enabling healthcare providers to make informed decisions about antibiotic use and treatment strategies.",
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
                                rx.list_item("Resistance Profiling: Comprehensive detection of resistance genes in bacterial pathogens."),
                                rx.list_item("Guided Therapy: Informing the selection of effective antibiotics based on resistance data."),
                                rx.list_item("Infection Control: Supporting efforts to manage and contain the spread of antibiotic-resistant infections."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.heading(
                                "MTB WGS AMR Testing",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "The Mycobacterium tuberculosis (MTB) Whole Genome Sequencing (WGS) AMR Testing focuses on identifying drug resistance in tuberculosis (TB) bacteria. This advanced testing method provides a detailed analysis of the genetic mutations associated with resistance to first- and second-line TB drugs, aiding in the effective management of TB cases.",
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
                                rx.list_item("Drug Resistance Detection: Identifying genetic mutations in MTB that confer resistance to TB medications."),
                                rx.list_item("Personalized Treatment: Tailoring TB treatment plans based on the resistance profile of the bacteria."),
                                rx.list_item("Public Health Monitoring: Tracking the spread of drug-resistant TB strains and informing public health strategies."),
                                margin_left="2rem",
                                style=paragraph_style
                            ),
                            rx.text(
                                "Take a stand against antibiotic resistance with our specialized AMR Studies. These services provide critical insights into the mechanisms of resistance, enabling effective treatment planning and helping to curb the spread of resistant infections. Contact Us Today to explore how our AMR testing solutions can support your efforts in combating antibiotic resistance and improving patient outcomes.",
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
                banner("Antibiotic Resistance (AMR) Studies"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Antibiotic resistance (AMR) is a growing global health challenge, leading to infections that are harder to treat and increasing the risk of disease spread, severe illness, and death. Our AMR Studies focus on understanding and combating this threat by identifying resistance mechanisms, tracking the spread of resistance, and guiding the development of effective treatment strategies.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "AMR Panel",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "The AMR Panel is designed to detect a wide range of antibiotic resistance genes in various pathogens. By identifying these genes, this panel helps in understanding the resistance profile of infectious agents, enabling healthcare providers to make informed decisions about antibiotic use and treatment strategies.",
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
                            rx.list_item("Resistance Profiling: Comprehensive detection of resistance genes in bacterial pathogens."),
                            rx.list_item("Guided Therapy: Informing the selection of effective antibiotics based on resistance data."),
                            rx.list_item("Infection Control: Supporting efforts to manage and contain the spread of antibiotic-resistant infections."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "MTB WGS AMR Testing",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "The Mycobacterium tuberculosis (MTB) Whole Genome Sequencing (WGS) AMR Testing focuses on identifying drug resistance in tuberculosis (TB) bacteria. This advanced testing method provides a detailed analysis of the genetic mutations associated with resistance to first- and second-line TB drugs, aiding in the effective management of TB cases.",
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
                            rx.list_item("Drug Resistance Detection: Identifying genetic mutations in MTB that confer resistance to TB medications."),
                            rx.list_item("Personalized Treatment: Tailoring TB treatment plans based on the resistance profile of the bacteria."),
                            rx.list_item("Public Health Monitoring: Tracking the spread of drug-resistant TB strains and informing public health strategies."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.text(
                            "Take a stand against antibiotic resistance with our specialized AMR Studies. These services provide critical insights into the mechanisms of resistance, enabling effective treatment planning and helping to curb the spread of resistant infections. Contact Us Today to explore how our AMR testing solutions can support your efforts in combating antibiotic resistance and improving patient outcomes.",
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