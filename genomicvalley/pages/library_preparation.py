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


@rx.page(route="/library-preparation", title="Library Preparation")
def library_preparation():
    return rx.section(
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Library Preparation"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Library Preparation service provides essential support for high-throughput sequencing projects by preparing DNA or RNA samples for analysis. Through meticulous processing and optimization, we ensure that samples are accurately and efficiently converted into sequencing libraries, facilitating high-quality, reliable data for a range of genomic and transcriptomic applications.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Library Preparation?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("High-Quality Libraries: Achieve optimal results by utilizing advanced techniques and protocols to prepare sequencing libraries with minimal biases and high consistency."),
                                rx.list_item("Customizable Protocols: Tailor library preparation workflows to suit specific project needs, including genomic DNA, RNA, or targeted sequencing, ensuring compatibility with various sequencing technologies."),
                                rx.list_item("Enhanced Data Accuracy: Prepare samples with precision to ensure high data quality and reproducibility, supporting reliable downstream analysis and accurate interpretation of results."),
                                rx.list_item("Efficiency and Scalability: Efficiently process large volumes of samples with streamlined workflows and automation, accommodating projects of varying scales and complexity."),
                                rx.list_item("Expert Support: Benefit from the expertise of our skilled technicians who provide guidance and troubleshooting throughout the library preparation process, ensuring optimal outcomes."),
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
                                rx.list_item("Researchers: Utilize library preparation services to prepare samples for a range of genomic and transcriptomic analyses, including whole-genome sequencing (WGS), whole-exome sequencing (WES), RNA sequencing (RNA-seq), and targeted sequencing."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Support drug discovery and development by preparing high-quality sequencing libraries for comprehensive genomic and transcriptomic studies."),
                                rx.list_item("Clinical Labs: Prepare samples for diagnostic and personalized medicine applications, including cancer genomics and rare disease research, ensuring accurate and reliable results."),
                                rx.list_item("Academic Institutions: Enhance research capabilities by utilizing library preparation services to support various genomic and transcriptomic projects, advancing scientific knowledge."),
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
                                rx.list_item("Sample Preparation: Receive detailed guidelines for sample submission, including requirements for DNA or RNA quality and quantity, to ensure successful library preparation."),
                                rx.list_item("Library Construction: Utilize state-of-the-art techniques to convert DNA or RNA samples into sequencing libraries, including fragmentation, adapter ligation, and amplification steps."),
                                rx.list_item("Quality Control: Perform rigorous quality control checks to assess library quality, including size distribution and concentration, to ensure optimal performance during sequencing."),
                                rx.list_item("Data Generation: Prepare libraries for sequencing on your chosen platform, ensuring that libraries meet the specifications and requirements of the sequencing technology."),
                                rx.list_item("Consultation & Support: Our team of experts is available to provide guidance, answer questions, and offer support throughout the library preparation process, ensuring successful outcomes."),
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
                                "We are committed to delivering high-quality library preparation services that support accurate, reliable, and reproducible results. By employing advanced technologies and rigorous quality control measures, our Library Preparation service ensures that your sequencing projects are set up for success, advancing research and discovery in genomics and transcriptomics.",
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
                banner("Library Preparation"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Library Preparation service provides essential support for high-throughput sequencing projects by preparing DNA or RNA samples for analysis. Through meticulous processing and optimization, we ensure that samples are accurately and efficiently converted into sequencing libraries, facilitating high-quality, reliable data for a range of genomic and transcriptomic applications.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Library Preparation? - Mobile
                        rx.heading(
                            "Why Choose Library Preparation?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("High-Quality Libraries: Achieve optimal results by utilizing advanced techniques and protocols to prepare sequencing libraries with minimal biases and high consistency."),
                            rx.list_item("Customizable Protocols: Tailor library preparation workflows to suit specific project needs, including genomic DNA, RNA, or targeted sequencing, ensuring compatibility with various sequencing technologies."),
                            rx.list_item("Enhanced Data Accuracy: Prepare samples with precision to ensure high data quality and reproducibility, supporting reliable downstream analysis and accurate interpretation of results."),
                            rx.list_item("Efficiency and Scalability: Efficiently process large volumes of samples with streamlined workflows and automation, accommodating projects of varying scales and complexity."),
                            rx.list_item("Expert Support: Benefit from the expertise of our skilled technicians who provide guidance and troubleshooting throughout the library preparation process, ensuring optimal outcomes."),
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
                            rx.list_item("Researchers: Utilize library preparation services to prepare samples for a range of genomic and transcriptomic analyses, including whole-genome sequencing (WGS), whole-exome sequencing (WES), RNA sequencing (RNA-seq), and targeted sequencing."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Support drug discovery and development by preparing high-quality sequencing libraries for comprehensive genomic and transcriptomic studies."),
                            rx.list_item("Clinical Labs: Prepare samples for diagnostic and personalized medicine applications, including cancer genomics and rare disease research, ensuring accurate and reliable results."),
                            rx.list_item("Academic Institutions: Enhance research capabilities by utilizing library preparation services to support various genomic and transcriptomic projects, advancing scientific knowledge."),
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
                            rx.list_item("Sample Preparation: Receive detailed guidelines for sample submission, including requirements for DNA or RNA quality and quantity, to ensure successful library preparation."),
                            rx.list_item("Library Construction: Utilize state-of-the-art techniques to convert DNA or RNA samples into sequencing libraries, including fragmentation, adapter ligation, and amplification steps."),
                            rx.list_item("Quality Control: Perform rigorous quality control checks to assess library quality, including size distribution and concentration, to ensure optimal performance during sequencing."),
                            rx.list_item("Data Generation: Prepare libraries for sequencing on your chosen platform, ensuring that libraries meet the specifications and requirements of the sequencing technology."),
                            rx.list_item("Consultation & Support: Our team of experts is available to provide guidance, answer questions, and offer support throughout the library preparation process, ensuring successful outcomes."),
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
                            "We are committed to delivering high-quality library preparation services that support accurate, reliable, and reproducible results. By employing advanced technologies and rigorous quality control measures, our Library Preparation service ensures that your sequencing projects are set up for success, advancing research and discovery in genomics and transcriptomics.",
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
        ),
        margin="0",
        padding="0",
    )