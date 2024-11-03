import reflex as rx  # type: ignore


font_style = {
    "color": "#565957",
}


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium", style=font_style), href=url)


def blur_background():
    return rx.fragment(
        rx.script(
            """
            window.onscroll = function() {
                var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                var scrollThreshold = 100;
                var navbar = document.getElementById('navbar');
                if (!navbar) {
                    return;
                }

                if (scrollTop > scrollThreshold) {
                    navbar.classList.add('blur-navbar');
                } else {
                    navbar.classList.remove('blur-navbar');
                }
            };
            """
        ),
        rx.html(
            """
            <style>
            .blur-navbar {
                border: 1px solid rgba(29, 29, 32, 0.08);
                background: HSLA(147,100%,50%,0.1);
                box-shadow: 0px 24px 54px -17px rgba(13, 12, 16, 0.30), 0px 0px 0px 1px rgba(93, 93, 107, 0.29), 0px 0px 64px 5px rgba(53, 51, 60, 0.30) inset;
                backdrop-filter: blur(20px);
            }
            </style>
            """
        ),
    )


def redirect(url):
    return rx.redirect(url)


hover_style = {"background": "#f0f0f0"}


def navbar_white() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="/logo1.png", alt="Genomic Valley", max_height="100px"
                        ),
                        href="/",
                    ),
                    align_items="center",
                    margin_left="1em",
                    margin_top="1em",
                    max_height="40px",
                    margin_bottom="1em",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About Us", "/about"),
                    navbar_link("Careers", "/career"),
                    navbar_link("Genetic Counseling", "/genetic-counseling"),
                    navbar_link("Plant Genomics", "/plant-genome"),
                    rx.hover_card.root(
                        rx.hover_card.trigger(
                            rx.button(
                                rx.text(
                                    "Services",
                                    size="4",
                                    weight="medium",
                                    style=font_style,
                                ),
                                rx.icon("chevron-down"),
                                weight="medium",
                                variant="ghost",
                                size="3",
                                color="green",
                                _hover={"background": "#93f599"},
                            ),
                        ),
                        rx.hover_card.content(
                            rx.vstack(
                                rx.vstack(
                                    rx.link(
                                        rx.text("Diagnostics Services", weight="bold"),
                                        href="/diagnostic-services",
                                    ),
                                    rx.grid(
                                        rx.vstack(
                                            rx.link(
                                                rx.text(
                                                    "Human Oncology and Inherited Disease Testing",
                                                    weight="medium",
                                                ),
                                                href="/human-oncology-inherited-disease-testing",
                                                _hover=hover_style,  
                                            ),
                                            rx.link(
                                                "DNA-Based Mutations (CNV, SNV, InDel) - Germline and Somatic",
                                                href="/dna-based-mutations",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "RNA Fusion",
                                                href="/rna-fusion",
                                                _hover=hover_style,
                                            ),
                                            align_items="start",
                                            spacing="1",
                                        ),
                                        rx.vstack(
                                            rx.link(
                                                rx.text(
                                                    "Infectious Disease", weight="medium"
                                                ),
                                                href="/infectious-disease",
                                                _hover=hover_style,     
                                            ),
                                            rx.link(
                                                "Pathogen Genomics",
                                                href="/pathogen-genomics",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Antibiotic Resistance (AMR) Studies",
                                                href="/amr-studies",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Viral Genomics",
                                                href="/viral-genomics",
                                                _hover=hover_style,
                                            ),
                                            align_items="start",
                                            spacing="1",
                                        ),
                                        rx.vstack(
                                            rx.link(
                                                rx.text(
                                                    "Genetic Disorders", weight="medium"
                                                ),
                                                href="/genetic-disorders",
                                                _hover=hover_style,     
                                            ),
                                            rx.link(
                                                "Rare Disease Genomics",
                                                href="/rare-disease-genomics",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Mendelian Disorders Testing",
                                                href="/mendelian-disorders-testing",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Genetic Testing and Screening",
                                                href="/genetic-testing-and-screening",
                                                _hover=hover_style,
                                            ),
                                            align_items="start",
                                            spacing="1",
                                        ),
                                        columns="3",
                                        spacing="4",
                                    ),
                                    align_items="start",
                                    width="100%",
                                ),
                                rx.vstack(
                                    rx.link(
                                        rx.text("Research Services", weight="bold"),
                                        href="/research-services",
                                    ),
                                    rx.grid(
                                        rx.vstack(
                                            rx.link(
                                                rx.text("Cancer Research", weight="medium"),
                                                href="/cancer-research",
                                                _hover=hover_style,      
                                            ),
                                            rx.link(
                                                "Pan-cancer Studies",
                                                href="/pan-cancer-studies",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Hereditary Cancer Syndromes Testing",
                                                href="/hereditary-cancer-syndromes-testing",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Tumor Microenvironment Studies",
                                                href="/tumor-microenvironment-studies",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Tumor Profiling",
                                                href="/tumor-profiling",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Liquid Biopsy",
                                                href="/liquid-biopsy",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Mutation Detection",
                                                href="/mutation-detection",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Biomarker Discovery",
                                                href="/biomarker-discovery",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Pharmacogenomics Testing",
                                                href="/pharmacogenomics-testing",
                                                _hover=hover_style,
                                            ),
                                            align_items="start",
                                            spacing="1",
                                        ),
                                        rx.vstack(
                                            rx.link(
                                                rx.text("NGS Services", weight="medium"),
                                                href="/ngs-services",
                                                _hover=hover_style,   
                                            ),
                                            rx.link(
                                                "Library Preparation",
                                                href="/library-preparation",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Sequencing Platforms",
                                                href="/sequencing-platforms",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Bioinformatics Analysis",
                                                href="/bioinformatics-analysis",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Data Interpretation",
                                                href="/data-interpretation",
                                                _hover=hover_style,
                                            ),
                                            align_items="start",
                                            spacing="1",
                                        ),
                                        rx.vstack(
                                            rx.link(
                                                rx.text(
                                                "Key Area of NGS Services",
                                                weight="medium",
                                            ),
                                                href="/key-areas-ngs-services",
                                                _hover=hover_style,  
                                            ),
                                            rx.link(
                                                "Whole Genome Sequencing (WGS)",
                                                href="/whole-genome-sequencing",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Whole Exome Sequencing (WES)",
                                                href="/whole-exome-sequencing",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Targeted Sequencing",
                                                href="/targeted-sequencing",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "RNA Sequencing (RNA-Seq)",
                                                href="/rna-sequencing",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Single-cell Sequencing",
                                                href="/single-cell-sequencing",
                                                _hover=hover_style,
                                            ),
                                            rx.link(
                                                "Metagenomics Testing",
                                                href="/metagenomics-testing",
                                                _hover=hover_style,
                                            ),
                                            align_items="start",
                                            spacing="1",
                                        ),
                                        columns="3",
                                        spacing="4",
                                    ),
                                    align_items="start",
                                    width="100%",
                                ),
                                spacing="4",
                                align_items="start",
                                width="100%",
                            ),
                            width="800px",
                            max_width="90vw",
                        ),
                    ),
                    rx.link(
                        rx.button(
                            rx.text(
                                "Contact",
                                size="4",
                                weight="medium",
                                style=font_style,
                            ),
                            weight="medium",
                            variant="ghost",
                            size="4",
                            _hover={"background": "#93f599"},
                        ),
                        href="/contact",
                    ),
                    justify="end",
                    spacing="5",
                    margin_right="2em",
                    margin_top="1.3em",
                ),
                justify="between",
            ),
        ),
        blur_background(),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30, color="black")),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=lambda: redirect("/")),
                        rx.menu.item("About Us", on_click=lambda: redirect("/about")),
                        rx.menu.item("Collaborations", on_click=lambda: redirect("/collaborations")),
                        rx.menu.item("Careers", on_click=lambda: redirect("/career")),
                        rx.menu.item("Genetic Counseling", on_click=lambda: redirect("/genetic-counseling")),
                        rx.menu.item("Plant Genomics", on_click=lambda: redirect("/plant-genome")),
                        rx.menu.sub(
                            rx.menu.sub_trigger("Services"),
                            rx.menu.sub_content(
                                rx.menu.item("Diagnostics Services", on_click=lambda: redirect("/diagnostic-services")),
                                rx.menu.item("Research Services", on_click=lambda: redirect("/research-services")),
                                rx.menu.item("Human Oncology Testing", on_click=lambda: redirect("/human-oncology-inherited-disease-testing")),
                                rx.menu.item("Infectious Disease Testing", on_click=lambda: redirect("/infectious-disease")),
                                rx.menu.item("Genetic Disorders Testing", on_click=lambda: redirect("/genetic-disorders")),
                                rx.menu.item("Cancer Research" , on_click=lambda: redirect("/cancer-research")),
                                rx.menu.item("NGS Services", on_click=lambda: redirect("/ngs-services")),
                                rx.menu.item("WGS", on_click=lambda: redirect("/whole-genome-sequencing")),
                                rx.menu.item("WES", on_click=lambda: redirect("/whole-exome-sequencing")),
                                rx.menu.item("Targeted Sequencing", on_click=lambda: redirect("/targeted-sequencing")),
                                rx.menu.item("RNA Sequencing (RNA-Seq)", on_click=lambda: redirect("/rna-sequencing")),
                                rx.menu.item("Single-cell Sequencing", on_click=lambda: redirect("/single-cell-sequencing")),
                                rx.menu.item("Metagenomics Testing", on_click=lambda: redirect("/metagenomics-testing")),
                            ),
                        ),
                        rx.menu.item("Contact", on_click=lambda: redirect("/contact")),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        id="navbar",
        padding="1em",
        position="fixed",
        top="0px",
        z_index="5",
        width="100%",
    )
