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

@rx.page(route="/genetic-counseling", title="Genetic Counseling")
def genetic_counseling():
    return rx.section(
        rx.desktop_only(
            rx.vstack(
                navbar(),
                banner("Genetic Counseling"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "What Is Genetic Counseling?",
                                size="9",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Genetic counseling is a specialized service aimed at helping individuals and families understand the implications of genetic conditions. It involves assessing the risk of inherited disorders, providing information on how genetics affects health, and guiding individuals on their options for diagnosis, prevention, and treatment.",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "At Genomic Valley Bharat Limited, we integrate cutting-edge genomics with personalized care to offer comprehensive genetic counseling services. Our mission is to empower families with knowledge, ensuring they make informed decisions about their health.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Why Would Someone See a Genetic Counselor?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "There are many reasons someone might seek genetic counseling. You may be referred to a genetic counselor if you or your family have a history of:",
                                style=paragraph_style,
                            ),
                            rx.unordered_list(
                                rx.list_item("Inherited genetic conditions"),
                                rx.list_item("Birth defects"),
                                rx.list_item("Repeated pregnancy loss"),
                                rx.list_item("Cancers with hereditary links (such as breast, ovarian, or colon cancer)"),
                                rx.list_item("Concerns about family planning or fertility"),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Our experienced team at Genomic Valley is equipped to address these concerns with precision, offering genetic insights to support your healthcare journey.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Who Should Get Genetic Counseling?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Genetic counseling is beneficial for:",
                                style=paragraph_style,
                            ),
                            rx.unordered_list(
                                rx.list_item("Individuals or couples planning to start a family"),
                                rx.list_item("Those with a known family history of a genetic condition"),
                                rx.list_item("Pregnant women with abnormal prenatal test results"),
                                rx.list_item("Individuals diagnosed with or at risk for a genetic disorder"),
                                rx.list_item("Cancer patients or those with a family history of hereditary cancers"),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Whether you’re looking for information before starting a family or navigating an existing health condition, Genomic Valley Bharat Limited provides tailored genetic counseling to guide you every step of the way.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "What Happens in Genetic Counseling?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "During a genetic counseling session, a counselor will gather detailed information about your family’s medical history and discuss any potential health concerns. They may suggest genetic testing to further explore your genetic risks and work with you to interpret the results. This process helps in understanding the likelihood of passing genetic conditions on to your children or managing inherited health risks.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "What Can I Expect in a Genetic Counseling Session?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "A typical genetic counseling session at Genomic Valley includes:",
                                style=paragraph_style,
                            ),
                            rx.unordered_list(
                                rx.list_item("Comprehensive family health review: Our counselors will review your medical and family history."),
                                rx.list_item("Pedigree analysis: A pedigree chart is created from both parties (husband and wife) to assess inherited conditions."),
                                rx.list_item("Education and guidance: You’ll receive detailed explanations about your genetic risks and available testing options."),
                                rx.list_item("Emotional support: Our counselors ensure that you are comfortable and supported throughout the process."),
                                rx.list_item("Consent: We make sure to secure informed consent, so you’re fully aware of all procedures and tests involved."),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "When Might I See a Genetic Counselor?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "You may want to consider seeing a genetic counselor if:",
                                style=paragraph_style,
                            ),
                            rx.unordered_list(
                                rx.list_item("You are planning a pregnancy and want to understand your genetic risks."),
                                rx.list_item("You or your partner has a known genetic condition."),
                                rx.list_item("You’re pregnant, and your doctor suggests genetic screening or testing based on results or age."),
                                rx.list_item("You have concerns about hereditary cancer risks or other inherited conditions."),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "At Genomic Valley, our counselors are available to help you at every stage, from family planning to post-diagnosis care.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "What Are the Options After Genetic Counseling?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "After genetic counseling, depending on your personal and family history, you may be offered genetic testing or referred to specialists for further care. You’ll be supported in making informed decisions about:",
                                style=paragraph_style,
                            ),
                            rx.unordered_list(
                                rx.list_item("Family planning"),
                                rx.list_item("Prenatal testing"),
                                rx.list_item("Managing inherited health risks"),
                                rx.list_item("Available treatment or prevention strategies"),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "How Can I Find a Genetic Counselor?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Genomic Valley Bharat Limited provides expert genetic counselors with deep knowledge in genomics and healthcare. Our counselors are highly skilled in guiding you through complex genetic information and helping you make choices that suit your personal situation. We ensure that each individual receives personalized care, comfort, and attention throughout their counseling journey.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Our Genetic Counseling Process",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "At Genomics Valley, our genetic counseling services are structured around comfort, clarity, and consent. Here’s how our process works:",
                                style=paragraph_style,
                            ),
                            rx.ordered_list(
                                rx.list_item("Consent: We ensure that you fully understand and agree to any testing or counseling services before proceeding."),
                                rx.list_item("Make the person comfortable: Our counselors take time to create a relaxed environment, ensuring you feel supported throughout the session."),
                                rx.list_item("3-4 counseling sessions per day: We maintain a manageable number of sessions to ensure each individual gets adequate time and attention."),
                                rx.list_item("Pedigree chart from both parties (husband and wife): We create detailed family histories for both partners to assess hereditary risks and provide comprehensive insights."),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "At Genomic Valley Bharat Limited, we believe that personalized care and the integration of advanced genomics are essential to empowering individuals and families with the knowledge they need to make informed decisions about their health. Join us in our mission to revolutionize healthcare with expert genetic counseling.",
                                style=paragraph_style,
                            ),
                            rx.button(
                                "Contact Us Today",
                                on_click=rx.redirect("/contact"),
                                style=button_style,
                            ),
                        ),
                        width="60vw",
                        p="4",
                        padding="4rem",
                    ),
                    width="100%",
                    justify="center",
                    padding="4rem",
                ),
                footer(),
            ),
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                navbar(),
                banner("Genetic Counseling"),
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "What Is Genetic Counseling?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Genetic counseling is a specialized service aimed at helping individuals and families understand the implications of genetic conditions. It involves assessing the risk of inherited disorders, providing information on how genetics affects health, and guiding individuals on their options for diagnosis, prevention, and treatment.",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "At Genomic Valley Bharat Limited, we integrate cutting-edge genomics with personalized care to offer comprehensive genetic counseling services. Our mission is to empower families with knowledge, ensuring they make informed decisions about their health.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Why Would Someone See a Genetic Counselor?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "There are many reasons someone might seek genetic counseling. You may be referred to a genetic counselor if you or your family have a history of:",
                            style=mobile_paragraph_style,
                        ),
                        rx.unordered_list(
                            rx.list_item("Inherited genetic conditions"),
                            rx.list_item("Birth defects"),
                            rx.list_item("Repeated pregnancy loss"),
                            rx.list_item("Cancers with hereditary links (such as breast, ovarian, or colon cancer)"),
                            rx.list_item("Concerns about family planning or fertility"),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Our experienced team at Genomic Valley is equipped to address these concerns with precision, offering genetic insights to support your healthcare journey.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Who Should Get Genetic Counseling?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Genetic counseling is beneficial for:",
                            style=mobile_paragraph_style,
                        ),
                        rx.unordered_list(
                            rx.list_item("Individuals or couples planning to start a family"),
                            rx.list_item("Those with a known family history of a genetic condition"),
                            rx.list_item("Pregnant women with abnormal prenatal test results"),
                            rx.list_item("Individuals diagnosed with or at risk for a genetic disorder"),
                            rx.list_item("Cancer patients or those with a family history of hereditary cancers"),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Whether you’re looking for information before starting a family or navigating an existing health condition, Genomic Valley Bharat Limited provides tailored genetic counseling to guide you every step of the way.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "What Happens in Genetic Counseling?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "During a genetic counseling session, a counselor will gather detailed information about your family’s medical history and discuss any potential health concerns. They may suggest genetic testing to further explore your genetic risks and work with you to interpret the results. This process helps in understanding the likelihood of passing genetic conditions on to your children or managing inherited health risks.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "What Can I Expect in a Genetic Counseling Session?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "A typical genetic counseling session at Genomic Valley includes:",
                            style=mobile_paragraph_style,
                        ),
                        rx.unordered_list(
                            rx.list_item("Comprehensive family health review: Our counselors will review your medical and family history."),
                            rx.list_item("Pedigree analysis: A pedigree chart is created from both parties (husband and wife) to assess inherited conditions."),
                            rx.list_item("Education and guidance: You’ll receive detailed explanations about your genetic risks and available testing options."),
                            rx.list_item("Emotional support: Our counselors ensure that you are comfortable and supported throughout the process."),
                            rx.list_item("Consent: We make sure to secure informed consent, so you’re fully aware of all procedures and tests involved."),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "When Might I See a Genetic Counselor?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "You may want to consider seeing a genetic counselor if:",
                            style=mobile_paragraph_style,
                        ),
                        rx.unordered_list(
                            rx.list_item("You are planning a pregnancy and want to understand your genetic risks."),
                            rx.list_item("You or your partner has a known genetic condition."),
                            rx.list_item("You’re pregnant, and your doctor suggests genetic screening or testing based on results or age."),
                            rx.list_item("You have concerns about hereditary cancer risks or other inherited conditions."),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "At Genomic Valley, our counselors are available to help you at every stage, from family planning to post-diagnosis care.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "What Are the Options After Genetic Counseling?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "After genetic counseling, depending on your personal and family history, you may be offered genetic testing or referred to specialists for further care. You’ll be supported in making informed decisions about:",
                            style=mobile_paragraph_style,
                        ),
                        rx.unordered_list(
                            rx.list_item("Family planning"),
                            rx.list_item("Prenatal testing"),
                            rx.list_item("Managing inherited health risks"),
                            rx.list_item("Available treatment or prevention strategies"),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "How Can I Find a Genetic Counselor?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Genomic Valley Bharat Limited provides expert genetic counselors with deep knowledge in genomics and healthcare. Our counselors are highly skilled in guiding you through complex genetic information and helping you make choices that suit your personal situation. We ensure that each individual receives personalized care, comfort, and attention throughout their counseling journey.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Our Genetic Counseling Process",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "At Genomics Valley, our genetic counseling services are structured around comfort, clarity, and consent. Here’s how our process works:",
                            style=mobile_paragraph_style,
                        ),
                        rx.ordered_list(
                            rx.list_item("Consent: We ensure that you fully understand and agree to any testing or counseling services before proceeding."),
                            rx.list_item("Make the person comfortable: Our counselors take time to create a relaxed environment, ensuring you feel supported throughout the session."),
                            rx.list_item("3-4 counseling sessions per day: We maintain a manageable number of sessions to ensure each individual gets adequate time and attention."),
                            rx.list_item("Pedigree chart from both parties (husband and wife): We create detailed family histories for both partners to assess hereditary risks and provide comprehensive insights."),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "At Genomic Valley Bharat Limited, we believe that personalized care and the integration of advanced genomics are essential to empowering individuals and families with the knowledge they need to make informed decisions about their health. Join us in our mission to revolutionize healthcare with expert genetic counseling.",
                            style=mobile_paragraph_style,
                        ),
                        rx.button(
                            "Contact Us Today",
                            on_click=rx.redirect("/contact"),
                            style=button_style,
                        ),
                    ),
                    width="100%",
                    p="4",
                    padding="2rem",
                ),
                footer(),
                width="100%",
                spacing="4",
            ),
            width="100%",
        )
    )
