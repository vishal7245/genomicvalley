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


@rx.page(route="/mendelian-disorders-testing", title="Mendelian Disorders Testing")
def mendelian_disorders_testing():
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
        rx.desktop_only(  # Desktop layout
            rx.vstack(
                navbar(),
                banner("Mendelian Disorders Testing"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Mendelian Disorders Testing service offers specialized genetic analysis to diagnose and understand Mendelian disorders—conditions caused by single-gene mutations that follow Mendelian inheritance patterns. By leveraging advanced genomic technologies, we provide detailed insights into the genetic basis of these disorders, enabling accurate diagnosis, personalized treatment, and informed genetic counseling.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Mendelian Disorders Testing?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Precise Genetic Diagnosis: Utilizing state-of-the-art next-generation sequencing (NGS) and targeted genetic testing, we identify mutations in specific genes associated with Mendelian disorders, ensuring accurate diagnosis."),
                                rx.list_item("Comprehensive Gene Panels: Our service includes comprehensive panels covering a wide range of Mendelian disorders, including rare and complex conditions, to provide a thorough assessment of potential genetic causes."),
                                rx.list_item("Inheritance Pattern Analysis: We analyze genetic variants according to Mendelian inheritance patterns—autosomal dominant, autosomal recessive, X-linked, and others—providing clarity on the genetic mechanisms involved in the disorder."),
                                rx.list_item("Personalized Treatment Options: Identifying the exact genetic mutation enables the development of personalized treatment plans tailored to the individual’s genetic profile, improving management and outcomes."),
                                rx.list_item("Family Planning and Genetic Counseling: Our testing supports informed family planning and genetic counseling by identifying carrier status and the risk of passing the disorder to future generations."),
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
                                rx.list_item("Clinicians & Geneticists: Access detailed genetic information to diagnose Mendelian disorders, guide treatment decisions, and offer genetic counseling to patients and their families."),
                                rx.list_item("Patients & Families: Obtain precise diagnoses for rare or unexplained conditions, leading to targeted treatment options and informed decisions about family planning."),
                                rx.list_item("Researchers: Leverage our genetic data to study the underlying mechanisms of Mendelian disorders, identify new genetic variants, and advance research in genetics and genomics."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Use our data to support the development of new therapies and drugs targeting specific genetic mutations associated with Mendelian disorders."),
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
                                rx.list_item("Sample Collection & Preparation: We provide clear instructions for collecting and preparing samples to ensure high-quality genetic analysis."),
                                rx.list_item("Genetic Sequencing: Using advanced NGS technology or targeted gene panels, we sequence relevant genes to identify mutations associated with Mendelian disorders."),
                                rx.list_item("Bioinformatics Analysis: Our bioinformatics tools analyze the sequencing data to detect pathogenic variants, interpret their significance, and provide a detailed understanding of the genetic basis of the disorder."),
                                rx.list_item("Comprehensive Reporting: We deliver detailed reports that include the identified genetic mutations, their implications for diagnosis and treatment, and recommendations for further action."),
                                rx.list_item("Consultation & Support: Our team of genetic experts is available to discuss results, provide insights into the clinical implications, and offer guidance on treatment options and genetic counseling."),
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
                                "We adhere to the highest standards of quality control and utilize the latest genomic technologies to ensure accurate and reliable results. Our Mendelian Disorders Testing service provides actionable insights to support clinicians, researchers, and patients in understanding and managing Mendelian disorders.",
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
                banner("Mendelian Disorders Testing"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Mendelian Disorders Testing service offers specialized genetic analysis to diagnose and understand Mendelian disorders—conditions caused by single-gene mutations that follow Mendelian inheritance patterns. By leveraging advanced genomic technologies, we provide detailed insights into the genetic basis of these disorders, enabling accurate diagnosis, personalized treatment, and informed genetic counseling.",
                            style=mobile_paragraph_style,
                        ),
                        # Why Choose Mendelian Disorders Testing? - Mobile
                        rx.heading(
                            "Why Choose Mendelian Disorders Testing?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Precise Genetic Diagnosis: Utilizing state-of-the-art next-generation sequencing (NGS) and targeted genetic testing, we identify mutations in specific genes associated with Mendelian disorders, ensuring accurate diagnosis."),
                            rx.list_item("Comprehensive Gene Panels: Our service includes comprehensive panels covering a wide range of Mendelian disorders, including rare and complex conditions, to provide a thorough assessment of potential genetic causes."),
                            rx.list_item("Inheritance Pattern Analysis: We analyze genetic variants according to Mendelian inheritance patterns—autosomal dominant, autosomal recessive, X-linked, and others—providing clarity on the genetic mechanisms involved in the disorder."),
                            rx.list_item("Personalized Treatment Options: Identifying the exact genetic mutation enables the development of personalized treatment plans tailored to the individual’s genetic profile, improving management and outcomes."),
                            rx.list_item("Family Planning and Genetic Counseling: Our testing supports informed family planning and genetic counseling by identifying carrier status and the risk of passing the disorder to future generations."),
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
                            rx.list_item("Clinicians & Geneticists: Access detailed genetic information to diagnose Mendelian disorders, guide treatment decisions, and offer genetic counseling to patients and their families."),
                            rx.list_item("Patients & Families: Obtain precise diagnoses for rare or unexplained conditions, leading to targeted treatment options and informed decisions about family planning."),
                            rx.list_item("Researchers: Leverage our genetic data to study the underlying mechanisms of Mendelian disorders, identify new genetic variants, and advance research in genetics and genomics."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Use our data to support the development of new therapies and drugs targeting specific genetic mutations associated with Mendelian disorders."),
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
                            rx.list_item("Sample Collection & Preparation: We provide clear instructions for collecting and preparing samples to ensure high-quality genetic analysis."),
                            rx.list_item("Genetic Sequencing: Using advanced NGS technology or targeted gene panels, we sequence relevant genes to identify mutations associated with Mendelian disorders."),
                            rx.list_item("Bioinformatics Analysis: Our bioinformatics tools analyze the sequencing data to detect pathogenic variants, interpret their significance, and provide a detailed understanding of the genetic basis of the disorder."),
                            rx.list_item("Comprehensive Reporting: We deliver detailed reports that include the identified genetic mutations, their implications for diagnosis and treatment, and recommendations for further action."),
                            rx.list_item("Consultation & Support: Our team of genetic experts is available to discuss results, provide insights into the clinical implications, and offer guidance on treatment options and genetic counseling."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),

                        # Commitment to Quality - Mobile
                        rx.heading(
                            "Commitment to Quality",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "We adhere to the highest standards of quality control and utilize the latest genomic technologies to ensure accurate and reliable results. Our Mendelian Disorders Testing service provides actionable insights to support clinicians, researchers, and patients in understanding and managing Mendelian disorders.",
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