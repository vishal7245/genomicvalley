import reflex as rx

# Update the accordion_style dictionary
accordion_style = {
    "color": "#000000",  # Change this to your desired color
}


def accordion_faq() -> rx.Component:
    return rx.section(
        rx.accordion.root(
            rx.accordion.item(
                header="What are the primary diagnostic services offered by Genomic Valley Biotech Limited?",
                content=rx.text(
                    "We specialize in Next-Generation Sequencing (NGS)-based molecular diagnostics, focusing on identifying genetic mutations and abnormalities with advanced AI integration. Our services enable early detection and personalized treatment plans, particularly in oncology.",
                    padding="15px 20px",
                    color="gray",
                ),
            ),
            rx.accordion.item(
                header="What are the key components of your personalized healthcare services?",
                content=rx.text(
                    "Our personalized healthcare utilizes NGS and AI technologies to tailor medical treatments based on individual genetic profiles. This approach enhances therapy effectiveness, minimizes adverse effects, and ensures tailored care aligned with each patient's genetic makeup.",
                    padding="15px 20px",
                    color="gray",
                ),
            ),
            rx.accordion.item(
                header="Could you explain your genetic disease predisposition services?",
                content=rx.text(
                    "We offer genetic disease predisposition analysis using NGS to predict susceptibility to hereditary conditions along with pharmacogenomics for recommendation of patient-centred drugs. This service supports proactive healthcare measures and informed decision-making for patients and healthcare providers.",
                    padding="15px 20px",
                    color="gray",
                ),
            ),
            rx.accordion.item(
                header="How does Genomic Valley Biotech Limited support community health through genomic initiatives?",
                content=rx.text(
                    "We envision to integrate AI into NGS to conduct population-wide genetic screening aimed at improving public health outcomes. Our initiatives will help identify prevalent health risks and design targeted community health programs for disease prevention and management.",
                    padding="15px 20px",
                    color="gray",
                ),
            ),
            rx.accordion.item(
                header="How does Genomic Valley Biotech Limited contribute to oncology research?",
                content=rx.text(
                    "We leverage over a decade of experience in NGS and AI to pioneer advancements in cancer research. Our focus includes uncovering novel biomarkers and genetic insights, collaborating with leading institutions to develop more effective diagnostic tools and therapeutic strategies.",
                    padding="15px 20px",
                    color="gray",
                ),
            ),
            collapsible=True,
            width="100%",
            variant="ghost",
            color_scheme="teal"
        ),
        width="60%",
        justify_content="center",
        align_items="center",
    )

    
def mobile_accordion_faq() -> rx.Component:
    return rx.section(
        rx.accordion.root(
            rx.accordion.item(
                header="What are the primary diagnostic services offered by Genomic Valley Biotech Limited?",
                content=rx.text(
                    "We specialize in Next-Generation Sequencing (NGS)-based molecular diagnostics, focusing on identifying genetic mutations and abnormalities with advanced AI integration. Our services enable early detection and personalized treatment plans, particularly in oncology.",
                    padding="15px 20px",
                    color="gray",
                ),
            ),
            rx.accordion.item(
                header="What are the key components of your personalized healthcare services?",
                content=rx.text(
                    "Our personalized healthcare utilizes NGS and AI technologies to tailor medical treatments based on individual genetic profiles. This approach enhances therapy effectiveness, minimizes adverse effects, and ensures tailored care aligned with each patient's genetic makeup.",
                    padding="15px 20px",
                    color="gray",
                ),
            ),
            rx.accordion.item(
                header="Could you explain your genetic disease predisposition services?",
                content=rx.text(
                    "We offer genetic disease predisposition analysis using NGS to predict susceptibility to hereditary conditions along with pharmacogenomics for recommendation of patient-centered drugs. This service supports proactive healthcare measures and informed decision-making for patients and healthcare providers.",
                    padding="15px 20px",
                    color="gray",
                ),
            ),
            rx.accordion.item(
                header="How does Genomic Valley Biotech Limited support community health through genomic initiatives?",
                content=rx.text(
                    "We envision integrating AI into NGS to conduct population-wide genetic screening aimed at improving public health outcomes. Our initiatives will help identify prevalent health risks and design targeted community health programs for disease prevention and management.",
                    padding="15px 20px",
                    color="gray",
                ),
            ),
            rx.accordion.item(
                header="How does Genomic Valley Biotech Limited contribute to oncology research?",
                content=rx.text(
                    "We leverage over a decade of experience in NGS and AI to pioneer advancements in cancer research. Our focus includes uncovering novel biomarkers and genetic insights, collaborating with leading institutions to develop more effective diagnostic tools and therapeutic strategies.",
                    padding="15px 20px",
                    color="gray",
                ),
            ),
            collapsible=True,
            width="100%",
            variant="ghost",
            color_scheme="teal",
        ),
        width="90%",
        justify_content="center",
        align_items="center",
    )



def faq_section() -> rx.Component:
    return rx.section(
                rx.desktop_only(
                  rx.section(
                    rx.vstack(
                        rx.heading("FAQ", size="5", weight="bold", margin_bottom="1em", color="green", align="center", id="faq"),
                        rx.heading("Frequently Asked Questions", size="8", weight="medium", color="black", margin_bottom="10px", align="center"),
                        rx.text(
                            "For any other questions, please feel free to contact us.",
                            size="5", align="center", margin_bottom="1em", color="gray", padding="10px"
                        ),
                        accordion_faq(),
                        justify_content="center",
                        align_items="center",
                        width="100%",
                    ),
                    width="100%",
                ),  
                ),
                rx.mobile_and_tablet(
                    rx.section(
                    rx.vstack(
                        rx.heading("FAQ", size="5", weight="bold", margin_bottom="1em", color="green", align="center", id="faq"),
                        rx.heading("Frequently Asked Questions", size="8", weight="medium", color="black", margin_bottom="10px", align="center"),
                        rx.text(
                            "For any other questions, please feel free to contact us.",
                            size="5", align="center", margin_bottom="1em", color="gray", padding="10px"
                        ),
                        mobile_accordion_faq(),
                        justify_content="center",
                        align_items="center",
                        width="100%",
                    ),
                    width="100%",
                ),    
                ),
            
        width="100%",
    )