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

image_urls = [
    "/AI-Based Genome Healthcare.jpg",
    "/Metagenomics and Healthcare.jpg",
    "/Extramural Research Project.jpg",
]


@rx.page(route="/research-services", title="Research Services")
def research_services():
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
        rx.desktop_only(
            rx.vstack(
                navbar(),
                banner("Research Services"),
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.vstack(
                                rx.text(
                                    "Our research services at Genomic Valley Bharat focus on pioneering advancements in oncology through the application of Next-Generation Sequencing (NGS) and artificial intelligence. With over a decade of experience, our team is dedicated to exploring new frontiers in cancer research, utilizing NGS to uncover novel biomarkers and genetic insights. We collaborate with leading academic and industry partners to translate these discoveries into practical solutions, driving innovation and enhancing the understanding of cancer biology. Our goal is to contribute to the development of more effective diagnostic tools and therapeutic strategies, ultimately advancing the field of oncology research.",
                                    style=paragraph_style,
                                ),
                                rx.heading(
                                    "AI-Based Genome Healthcare",
                                    size="9",
                                    margin_top="2rem",
                                    margin_bottom="1rem",
                                    color="teal",
                                    font_weight="bold",
                                ),
                                rx.text(
                                    "At Genomic Valley Bharat, we are pioneering AI-based genome healthcare research to revolutionize the way genetic data is analyzed and interpreted. By developing sophisticated AI algorithms and machine learning models, we enhance the accuracy and speed of genomic diagnostics and research. This approach allows us to uncover complex genetic patterns and associations, driving innovations in personalized medicine and therapeutic strategies.",
                                    style=paragraph_style,
                                ),
                                rx.heading(
                                    "Metagenomics and Healthcare",
                                    size="9",
                                    margin_top="2rem",
                                    margin_bottom="1rem",
                                    color="teal",
                                    font_weight="bold",
                                ),
                                rx.text(
                                    "Our metagenomics research focuses on studying the collective genomes of microbial communities within the human body and their impact on health and disease. Using advanced sequencing technologies, we investigate the role of microbiomes in various health conditions, aiming to identify novel biomarkers and therapeutic targets. This research holds the potential to transform our understanding of the microbiome's influence on human health and to develop microbiome-based treatments and interventions.",
                                    style=paragraph_style,
                                ),
                                rx.heading(
                                    "Extramural Research Project",
                                    size="9",
                                    margin_top="2rem",
                                    margin_bottom="1rem",
                                    color="teal",
                                    font_weight="bold",
                                ),
                                rx.text(
                                    "Our extramural research projects involve collaborating with external academic institutions, research organizations, and industry partners to advance genomic science. These projects leverage our expertise in NGS and AI to explore new frontiers in genetics and healthcare. Through these collaborations, we aim to accelerate the translation of scientific discoveries into practical applications that can benefit patients and the broader healthcare community.",
                                    style=paragraph_style,
                                ),
                            ),
                            width="60vw",
                            p="4",
                            padding="4rem",
                        ),
                        rx.box(
                            rx.vstack(
                                *[
                                    rx.image(src=url, style=image_style)
                                    for url in image_urls
                                ],
                            ),
                            width="40vw",
                            p="4",
                            padding="4rem",
                        ),
                        width="100vw",
                        spacing="0",
                        left="0",
                    ),
                    width="100%",
                    overflow="hidden",
                ),
                footer(),
            ),
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                navbar(),
                banner("Research Services"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Our research services at Genomic Valley Bharat focus on pioneering advancements in oncology through the application of Next-Generation Sequencing (NGS) and artificial intelligence. With over a decade of experience, our team is dedicated to exploring new frontiers in cancer research, utilizing NGS to uncover novel biomarkers and genetic insights. We collaborate with leading academic and industry partners to translate these discoveries into practical solutions, driving innovation and enhancing the understanding of cancer biology. Our goal is to contribute to the development of more effective diagnostic tools and therapeutic strategies, ultimately advancing the field of oncology research.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "AI-Based Genome Healthcare",
                            size="8",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                            id="ai-based-genome-healthcare",
                        ),
                        rx.text(
                            "At Genomic Valley Bharat, we are pioneering AI-based genome healthcare research to revolutionize the way genetic data is analyzed and interpreted. By developing sophisticated AI algorithms and machine learning models, we enhance the accuracy and speed of genomic diagnostics and research. This approach allows us to uncover complex genetic patterns and associations, driving innovations in personalized medicine and therapeutic strategies.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Metagenomics and Healthcare",
                            size="8",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                            id="metagenomics-and-healthcare",
                        ),
                        rx.text(
                            "Our metagenomics research focuses on studying the collective genomes of microbial communities within the human body and their impact on health and disease. Using advanced sequencing technologies, we investigate the role of microbiomes in various health conditions, aiming to identify novel biomarkers and therapeutic targets. This research holds the potential to transform our understanding of the microbiome's influence on human health and to develop microbiome-based treatments and interventions.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Extramural Research Project",
                            size="8",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                            id="extramural-research-project",
                        ),
                        rx.text(
                            "Our extramural research projects involve collaborating with external academic institutions, research organizations, and industry partners to advance genomic science. These projects leverage our expertise in NGS and AI to explore new frontiers in genetics and healthcare. Through these collaborations, we aim to accelerate the translation of scientific discoveries into practical applications that can benefit patients and the broader healthcare community.",
                            style=mobile_paragraph_style,
                        ),
                        rx.vstack(
                            *[
                                rx.image(src=url, style=image_style)
                                for url in image_urls
                            ],
                            spacing="1",
                            margin_top="2rem",
                        ),
                    ),
                    width="100%",
                    p="4",
                    padding="2rem",
                ),
                footer(),
            ),
            width="100%",
            padding="0px",
        ),
        width="100%",
        padding="0px",
    )
