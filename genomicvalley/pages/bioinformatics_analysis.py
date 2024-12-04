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

@rx.page(route="/bioinformatics-analysis", title="Bioinformatics Analysis")
def bioinformatics_analysis():
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
                banner("Bioinformatics Analysis"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Our Bioinformatics Analysis service offers comprehensive computational and statistical support to interpret complex biological data. By applying advanced bioinformatics tools and techniques, we help researchers extract meaningful insights from genomic, transcriptomic, and proteomic data, facilitating a deeper understanding of biological processes and supporting data-driven discoveries.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Choose Bioinformatics Analysis?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Advanced Computational Tools: Utilize cutting-edge bioinformatics software and algorithms to analyze large-scale biological datasets, including DNA, RNA, and protein sequences, as well as multi-omics data."),
                                rx.list_item("Customized Analysis: Tailor bioinformatics workflows to meet specific research goals, including sequence alignment, variant calling, gene expression analysis, pathway analysis, and integrative data analysis."),
                                rx.list_item("Data Integration: Combine data from various sources, such as genomic, transcriptomic, and proteomic datasets, to provide a holistic view of biological phenomena and uncover novel insights."),
                                rx.list_item("High-Quality Insights: Obtain accurate and actionable insights from complex datasets, enabling a better understanding of gene function, molecular mechanisms, and disease pathways."),
                                rx.list_item("Expert Support: Benefit from the expertise of our bioinformatics team, who provide guidance on analysis strategies, interpret results, and assist with data visualization and reporting."),
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
                                rx.list_item("Researchers: Access advanced bioinformatics tools and expertise to analyze and interpret genomic, transcriptomic, and proteomic data, advancing research in fields such as cancer genomics, drug discovery, and molecular biology."),
                                rx.list_item("Pharmaceutical & Biotech Companies: Leverage bioinformatics analysis to support drug development, identify therapeutic targets, and understand drug mechanisms and responses."),
                                rx.list_item("Clinical Labs: Utilize bioinformatics to interpret clinical sequencing data, support personalized medicine initiatives, and enhance diagnostic and prognostic capabilities."),
                                rx.list_item("Academic Institutions: Enhance research capabilities by applying bioinformatics to a wide range of scientific investigations, contributing to academic advancements and discoveries."),
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
                                rx.list_item("Data Collection: Collaborate with our team to collect and prepare biological data, including raw sequencing data, gene expression profiles, or proteomic datasets, ensuring high-quality input for analysis."),
                                rx.list_item("Custom Analysis: Apply bioinformatics tools and methodologies to perform sequence alignment, variant analysis, gene expression analysis, and other relevant computational tasks tailored to your research objectives."),
                                rx.list_item("Data Integration: Integrate data from multiple sources to provide a comprehensive analysis, combining genomic, transcriptomic, and proteomic information for a holistic understanding of biological processes."),
                                rx.list_item("Quality Control: Implement rigorous quality control measures to ensure the accuracy and reliability of the analysis, addressing any issues that may affect data interpretation."),
                                rx.list_item("Result Interpretation: Provide detailed interpretation of the analysis results, including identification of key findings, biological significance, and potential implications for research or clinical applications."),
                                rx.list_item("Reporting & Visualization: Generate comprehensive reports and visualizations to present findings clearly and effectively, supporting data-driven decisions and communications."),
                                rx.list_item("Consultation & Support: Offer ongoing support and consultation to address questions, provide additional insights, and assist with integrating bioinformatics findings into your research or clinical practice."),
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
                                "We are committed to delivering high-quality bioinformatics analysis that drives meaningful discoveries and advancements in biology and medicine. By employing advanced computational tools and providing expert support, our Bioinformatics Analysis service helps you unlock the full potential of your biological data, enabling impactful research and informed decision-making.",
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
                banner("Bioinformatics Analysis"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our Bioinformatics Analysis service offers comprehensive computational and statistical support to interpret complex biological data. By applying advanced bioinformatics tools and techniques, we help researchers extract meaningful insights from genomic, transcriptomic, and proteomic data, facilitating a deeper understanding of biological processes and supporting data-driven discoveries.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Why Choose Bioinformatics Analysis?",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Advanced Computational Tools: Utilize cutting-edge bioinformatics software and algorithms to analyze large-scale biological datasets, including DNA, RNA, and protein sequences, as well as multi-omics data."),
                            rx.list_item("Customized Analysis: Tailor bioinformatics workflows to meet specific research goals, including sequence alignment, variant calling, gene expression analysis, pathway analysis, and integrative data analysis."),
                            rx.list_item("Data Integration: Combine data from various sources, such as genomic, transcriptomic, and proteomic datasets, to provide a holistic view of biological phenomena and uncover novel insights."),
                            rx.list_item("High-Quality Insights: Obtain accurate and actionable insights from complex datasets, enabling a better understanding of gene function, molecular mechanisms, and disease pathways."),
                            rx.list_item("Expert Support: Benefit from the expertise of our bioinformatics team, who provide guidance on analysis strategies, interpret results, and assist with data visualization and reporting."),
                            margin_left="1rem", # Smaller margin for mobile
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Who Can Benefit?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Researchers: Access advanced bioinformatics tools and expertise to analyze and interpret genomic, transcriptomic, and proteomic data, advancing research in fields such as cancer genomics, drug discovery, and molecular biology."),
                            rx.list_item("Pharmaceutical & Biotech Companies: Leverage bioinformatics analysis to support drug development, identify therapeutic targets, and understand drug mechanisms and responses."),
                            rx.list_item("Clinical Labs: Utilize bioinformatics to interpret clinical sequencing data, support personalized medicine initiatives, and enhance diagnostic and prognostic capabilities."),
                            rx.list_item("Academic Institutions: Enhance research capabilities by applying bioinformatics to a wide range of scientific investigations, contributing to academic advancements and discoveries."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Our Process",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Data Collection: Collaborate with our team to collect and prepare biological data, including raw sequencing data, gene expression profiles, or proteomic datasets, ensuring high-quality input for analysis."),
                            rx.list_item("Custom Analysis: Apply bioinformatics tools and methodologies to perform sequence alignment, variant analysis, gene expression analysis, and other relevant computational tasks tailored to your research objectives."),
                            rx.list_item("Data Integration: Integrate data from multiple sources to provide a comprehensive analysis, combining genomic, transcriptomic, and proteomic information for a holistic understanding of biological processes."),
                            rx.list_item("Quality Control: Implement rigorous quality control measures to ensure the accuracy and reliability of the analysis, addressing any issues that may affect data interpretation."),
                            rx.list_item("Result Interpretation: Provide detailed interpretation of the analysis results, including identification of key findings, biological significance, and potential implications for research or clinical applications."),
                            rx.list_item("Reporting & Visualization: Generate comprehensive reports and visualizations to present findings clearly and effectively, supporting data-driven decisions and communications."),
                            rx.list_item("Consultation & Support: Offer ongoing support and consultation to address questions, provide additional insights, and assist with integrating bioinformatics findings into your research or clinical practice."),
                            margin_left="1rem",
                            style=mobile_paragraph_style
                        ),
                        rx.heading(
                            "Commitment to Excellence",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "We are committed to delivering high-quality bioinformatics analysis that drives meaningful discoveries and advancements in biology and medicine. By employing advanced computational tools and providing expert support, our Bioinformatics Analysis service helps you unlock the full potential of your biological data, enabling impactful research and informed decision-making.",
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