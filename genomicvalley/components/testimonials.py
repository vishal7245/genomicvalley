import reflex as rx


icon_box_style = {
    "background_color": "#f9fafb",
}


def card(name:str, id:str, testimonial: str, ) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
            rx.avatar(fallback=name.upper()[0:2], color_scheme="green", size="5"),
            rx.vstack(
                rx.heading(name, size="5", color="black",),
                rx.text(id, color="gray",),
                margin_left="10px",   
            )
            ),
            rx.text.quote(testimonial, color="gray"),
            spacing="4",
            align_items="start",
        ),
        width="350px",
        padding="20px",
        border="1px solid #e0e0e0",
        border_radius="8px",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
        _hover = {
            "background": "#E5E4E2",
        }
    )

def testimonials_section() -> rx.Component:
    return rx.section(
        rx.desktop_only(
            rx.section(
                rx.vstack(
                    rx.heading("TESTIMONIALS", size="5", weight="bold", margin_bottom="1em", color="green"),
                    rx.heading("What our users say", size="8", weight="medium", color="black", margin_bottom="10px"),
                    rx.text(
                        "Here's what our clients around the internet are saying about us.",
                        size="5", align="center", margin_bottom="1em", color="gray"
                    ),
                    rx.grid(
                        card("John Doe", "@JohnDoe", "Genomic Valley will be a trailblazer in integrating Next-Generation Sequencing and AI into healthcare. Their expertise and commitment to innovation will be evident in the precision and reliability of their diagnostic services. As a healthcare provider, I will trust their data and solutions to enhance patient outcomes and support informed decision-making."),
                        card("Jane Doe", "@JaneDoe", "Genomic Valley will be transformative. Their advanced AI-based genome healthcare research will provide us with invaluable insights into genetic patterns, driving innovation in our personalized medicine approaches. Their dedication to excellence and cutting-edge technology will be truly commendable."),
                        card("John Doe", "@JohnDoe", "The personalized healthcare services at Genomic Valley will revolutionize our approach to patient care. By tailoring treatments based on unique genetic profiles, they will ensure our patients receive the most effective therapies with minimal adverse effects. Their expertise in NGS and AI will be unmatched, making them an invaluable partner in our healthcare journey."),
                        card("Jane Doe", "@JaneDoe", "Genetic disease predisposition services will be a game-changer for proactive healthcare. By identifying individuals' susceptibility to hereditary conditions, we will be able to implement early interventions and preventive measures. Their precise diagnostics and comprehensive genetic analysis will empower us to make informed decisions and improve patient care."),
                        card("John Doe", "@JohnDoe", "Genomic Valley community health support initiatives will significantly impact public health outcomes. Their integration of NGS and AI for population-wide genetic testing will help us design effective health programs and improve disease prevention strategies. Their commitment to enhancing community well-being will be truly inspiring."),
                        card("Jane Doe", "@JaneDoe", "Genomic Valley's research services will be instrumental in advancing our understanding of cancer biology. Their pioneering work in oncology research, utilizing Next-Generation Sequencing and AI, will lead to groundbreaking discoveries and practical solutions. Their collaboration will be invaluable in developing more effective diagnostic tools and therapeutic strategies."),
                        columns="3",
                        spacing="5",
                    ),
                    justify_content="center",
                    align_items="center",
                    width="100%",
                ),
                width="100%",
            )
        ),
        rx.mobile_and_tablet(
            rx.section(
                rx.vstack(
                    rx.heading("TESTIMONIALS", size="4", weight="bold", margin_bottom="1em", color="green"),
                    rx.heading("What our users say", size="6", weight="medium", color="black", margin_bottom="10px"),
                    rx.text(
                        "Here's what our clients around the internet are saying about us.",
                        size="4", align="center", margin_bottom="1em", color="gray"
                    ),
                    rx.vstack(
                        card("John Doe", "@JohnDoe", "Genomic Valley will be a trailblazer in integrating Next-Generation Sequencing and AI into healthcare. Their expertise and commitment to innovation will be evident in the precision and reliability of their diagnostic services."),
                        card("Jane Doe", "@JaneDoe", "Genomic Valley will be transformative. Their advanced AI-based genome healthcare research will provide us with invaluable insights into genetic patterns, driving innovation in our personalized medicine approaches."),
                        card("John Doe", "@JohnDoe", "The personalized healthcare services at Genomic Valley will revolutionize our approach to patient care. By tailoring treatments based on unique genetic profiles, they will ensure our patients receive the most effective therapies with minimal adverse effects."),
                        spacing="4",
                        width="100%",
                    ),
                    justify_content="center",
                    align_items="center",
                    width="100%",
                ),
                width="100%",
            )
        ),
        width="100%",
    )