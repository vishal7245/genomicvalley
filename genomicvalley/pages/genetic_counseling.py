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
                rx.section(
                    rx.heading(
                        "Meet Our Genetic Counselor",
                        size="9",
                        color="teal",
                        font_weight="bold",
                        margin_bottom="5",
                        text_align="center"  # Centering the text
                    ),
                    width="100%",
                    display="flex",
                    justify_content="center"  # Centering the section
                ),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.flex(
                                rx.hstack(
                                    rx.image(
                                        src="/uzma.jpeg",
                                        alt="Dr. Uzma Shamim",
                                        width="400px",
                                        border_radius="10%",
                                        margin_right="3"
                                    ),
                                    rx.vstack(
                                        rx.heading(
                                            "Dr. Uzma Shamim",
                                            size="8",
                                            color="teal",
                                            font_weight="bold",
                                        ),
                                        rx.text(
                                            "Geneticist/Consultant/Genetic Counselor",
                                            font_size="1.2rem",
                                            color="gray",
                                        ),
                                        rx.link(
                                            rx.button(
                                                "Book Now",
                                                size="3",
                                                variant="solid",
                                                color_scheme="teal",
                                            ),
                                            href="https://pages.razorpay.com/genetic-counseling",
                                        ),
                                        align_items="start",
                                    ),
                                    spacing="5",
                                    align="center",
                                    margin_bottom="2rem",
                                ),
                                rx.vstack(
                                    rx.text(
                                        "Over 8 years of experience in Clinical Genomics and Genetics, particularly in the realm of Rare Diseases. I have led comprehensive genetic screening and research programs, significantly contributing to the scientific understanding of complex genomic questions.",
                                        style=paragraph_style,
                                    ),
                                    rx.text(
                                        "With expertise in Genetic Analysis, Clinical Interpretation, and Genetic Reporting, I bring precision to the application of genomics in clinical practice.",
                                        style=paragraph_style,
                                    ),
                                    rx.text(
                                        "As a Genetic Counselor and Geneticist, I specialize in providing personalized genetic guidance and insights to individuals, families, and healthcare providers. With extensive experience in clinical genetics, I support clients in understanding complex genetic information, empowering them to make informed health decisions. My expertise spans genetic testing, risk assessment, and interpretation of genetic conditions, with a focus on hereditary diseases, rare disorders, and personalized medicine.",
                                        style=paragraph_style,
                                    ),
                                    rx.text(
                                        "Through compassionate counseling, I assist patients in navigating the psychosocial and medical implications of genetic conditions, offering a supportive environment to discuss risks, preventive measures, and treatment options. I work closely with healthcare professionals to integrate genetic insights into patient care, helping translate cutting-edge genetic research into actionable healthcare strategies.",
                                        style=paragraph_style,
                                    ),
                                    width="100%",
                                    spacing="1",
                                    align_items="start",
                                    margin_top="2",
                                ),
                                direction="column",
                                width="100%",
                            ),
                            rx.heading(
                                "Key Expertise:",
                                size="8",
                                color="teal",
                                font_weight="bold",
                                margin_bottom="1rem",
                            ),
                            rx.unordered_list(
                                rx.list_item(
                                    "Genetic counseling for hereditary and rare diseases"
                                ),
                                rx.list_item(
                                    "Risk assessment for genetic disorders"
                                ),
                                rx.list_item(
                                    "Interpretation of genetic testing results"
                                ),
                                rx.list_item(
                                    "Personalized medicine and precision health"
                                ),
                                rx.list_item(
                                    "Family planning and reproductive counseling"
                                ),
                                rx.list_item(
                                    "Educating patients and healthcare professionals on genetic risks and conditions"
                                ),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Whether you're seeking genetic insights for personal or family health, or you need guidance on managing a hereditary condition or simply want to consult with an expert on a genetics-related question, I provide information, clarity, and support through every step of your genetic journey.",
                                style=paragraph_style,
                            ),
                            # Accordion
                            rx.accordion.root(
                                rx.accordion.item(
                                    header="What Is Genetic Counseling?",
                                    content=rx.box(
                                        rx.text(
                                            "Genetic counseling is a specialized service aimed at providing information and support to individuals and families to understand the medical and psychological implications of genetic conditions. It involves assessing the risk of inherited disorders, providing information on how genetics affects health, and guiding individuals on their options for diagnosis, prevention, and treatment.",
                                            style=paragraph_style,
                                        ),
                                        rx.text(
                                            "At Genomic Valley Bharat Limited, we integrate cutting-edge genomics with personalized care to offer comprehensive genetic counseling services. The mission is to empower families with knowledge, ensuring they make informed decisions about their health.",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                rx.accordion.item(
                                    header="Why Would Someone See a Genetic Counselor?",
                                    content=rx.box(
                                        rx.text(
                                            "There are many reasons someone might seek genetic counseling. You may be referred to a genetic counselor if you or your family have a history of:",
                                            style=paragraph_style,
                                        ),
                                        rx.unordered_list(
                                            rx.list_item("Inherited genetic conditions"),
                                            rx.list_item("Birth defects"),
                                            rx.list_item("Repeated pregnancy loss"),
                                            rx.list_item(
                                                "Cancers with hereditary links (such as breast, ovarian, or colon cancer)"
                                            ),
                                            rx.list_item("Concerns about family planning or fertility"),
                                            margin_left="2rem",
                                            style=paragraph_style,
                                        ),
                                        rx.text(
                                            "The experienced team at Genomic Valley is equipped to address these concerns with precision, offering genetic insights to support your healthcare journey.",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                rx.accordion.item(
                                    header="Who Should Get Genetic Counseling?",
                                    content=rx.box(
                                        rx.text(
                                            "Genetic counseling is beneficial for:",
                                            style=paragraph_style,
                                        ),
                                        rx.unordered_list(
                                            rx.list_item(
                                                "Individuals or couples with advanced maternal age planning to start a family"
                                            ),
                                            rx.list_item(
                                                "Those with a known family history of a genetic condition"
                                            ),
                                            rx.list_item("Pregnant women with abnormal prenatal test results"),
                                            rx.list_item(
                                                "Individuals diagnosed with or suspected for a genetic disorder"
                                            ),
                                            rx.list_item(
                                                "Cancer patients or those with a family history of hereditary cancers"
                                            ),
                                            margin_left="2rem",
                                            style=paragraph_style,
                                        ),
                                        rx.text(
                                            "Whether you’re looking for information before starting a family or navigating an existing health condition, Genomic Valley Bharat Limited provides tailored genetic counseling to guide you every step of the way.",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                rx.accordion.item(
                                    header="What Happens in Genetic Counseling?",
                                    content=rx.box(
                                        rx.text(
                                            "During a genetic counseling session, the counselor will gather detailed information about your family’s medical history and discuss any potential health concerns. They may suggest genetic testing to further explore your genetic risks and work with you to interpret the results. This process helps in understanding the likelihood of passing genetic conditions on to your children or managing inherited health risks.",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                rx.accordion.item(
                                    header="What Can I Expect in a Genetic Counseling Session?",
                                    content=rx.box(
                                        rx.text(
                                            "A typical genetic counseling session at Genomic Valley includes:",
                                            style=paragraph_style,
                                        ),
                                        rx.unordered_list(
                                            rx.list_item(
                                                "Comprehensive family health review: The counselor will review your medical and family history."
                                            ),
                                            rx.list_item(
                                                "Pedigree analysis: A pedigree chart is created from both parties (husband and wife) to assess inherited conditions."
                                            ),
                                            rx.list_item(
                                                "Education and guidance: You’ll receive detailed explanations about your genetic risks and available testing options."
                                            ),
                                            rx.list_item(
                                                "Psychosocial support: The counselor ensures that you are comfortable and supported throughout the process."
                                            ),
                                            rx.list_item(
                                                "Consent: Secure informed consent is the priority, making you fully aware of all procedures and tests involved."
                                            ),
                                            rx.list_item(
                                                "Interpretation of test results: If genetic testing is pursued, the counselor will explain the results in detail."
                                            ),
                                            rx.list_item(
                                                "Guidance on next steps: The counselor will help you make informed decisions about healthcare options."
                                            ),
                                            rx.list_item(
                                                "Written Summary of the session: Serves as a permanent record of the information discussed."
                                            ),
                                            margin_left="2rem",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                rx.accordion.item(
                                    header="When Might I See a Genetic Counselor?",
                                    content=rx.box(
                                        rx.text(
                                            "You may want to consider seeing a genetic counselor if:",
                                            style=paragraph_style,
                                        ),
                                        rx.unordered_list(
                                            rx.list_item(
                                                "You are planning a pregnancy and want to understand your genetic risks."
                                            ),
                                            rx.list_item(
                                                "You or your partner has a known genetic condition in the family."
                                            ),
                                            rx.list_item(
                                                "You’re pregnant, and your doctor suggests genetic screening or testing based on results or age."
                                            ),
                                            rx.list_item(
                                                "You have concerns about hereditary cancer risks or other inherited conditions."
                                            ),
                                            margin_left="2rem",
                                            style=paragraph_style,
                                        ),
                                        rx.text(
                                            "At Genomic Valley, the counselor is available to help you at every stage, from family planning to post-diagnosis care.",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                rx.accordion.item(
                                    header="What Are the Options After Genetic Counseling?",
                                    content=rx.box(
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
                                    ),
                                ),
                                rx.accordion.item(
                                    header="How Can I Find a Genetic Counsellor?",
                                    content=rx.box(
                                        rx.text(
                                            "Genomic Valley Bharat Limited provides an expert genetic counsellor with deep knowledge in genomics and healthcare. The counselor is highly skilled in guiding through complex genetic information and helping make choices that suit your personal situation. We ensure that each individual receives personalized care, comfort, and attention throughout their counselling journey.",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                width="100%",
                                collapsible=True,
                                variant="ghost",
                                color_scheme="teal"
                            ),
                            rx.heading(
                                "Our Genetic Counselling Process",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "At Genomic Valley, the genetic counselling services are structured around comfort, clarity, and consent. Here’s how our process works:",
                                style=paragraph_style,
                            ),
                            rx.ordered_list(
                                rx.list_item(
                                    "Consent: We ensure that you fully understand and agree to any testing or counseling services before proceeding."
                                ),
                                rx.list_item(
                                    "Make the person comfortable: The counsellor takes time to create a relaxed environment, ensuring you feel supported throughout the session."
                                ),
                                rx.list_item(
                                    "5-6 counseling sessions per day: We maintain a manageable number of sessions to ensure each individual gets adequate time and attention."
                                ),
                                rx.list_item(
                                    "Pedigree chart from both parties (husband and wife): We create detailed family histories for both partners to assess hereditary risks and provide comprehensive insights."
                                ),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "At Genomic Valley Bharat Limited, we believe that personalized care and the integration of advanced genomics are essential to empowering individuals and families with the knowledge they need to make informed decisions about their health. Join us in our mission to revolutionize healthcare with expert genetic counseling.",
                                style=paragraph_style,
                            ),
                            rx.section(
                                rx.hstack(
                                    rx.link(
                                            rx.button(
                                                "Book Now",
                                                size="3",
                                                variant="solid",
                                                color_scheme="teal",
                                            ),
                                            href="https://pages.razorpay.com/genetic-counseling",
                                        ),
                                    rx.link(
                                            rx.button(
                                                "Contact Us",
                                                size="3",
                                                variant="solid",
                                                color_scheme="teal",
                                            ),
                                            href="/contact",
                                        ),    
                                ),
                                width="100%",
                                display="flex",         
                                justify_content="center"  
                            ),
                        ),
                        width="60vw",
                        p="4",
                        padding="3rem",
                    ),
                    width="100%",
                    justify="center",
                    padding="3rem",
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
                        rx.flex(
                            rx.box(
                                rx.image(
                                    src="/uzma.jpeg",
                                    alt="Dr. Uzma Shamim",
                                    width="150px",
                                    border_radius="50%",
                                ),
                                margin_bottom="1rem",
                            ),
                            rx.box(
                                rx.heading(
                                    "Dr. Uzma Shamim",
                                    size="5",
                                    color="teal",
                                    font_weight="bold",
                                    margin_bottom="0.5rem",
                                    text_align="center"  # Centering the text
                                ),
                                rx.text(
                                    "Geneticist/Consultant/Genetic Counselor",
                                    font_size="1rem",
                                    color="gray",
                                    margin_bottom="0.5rem",
                                    text_align="center"  # Centering the text
                                ),
                                rx.link(
                                    rx.button(
                                        "Book Now",
                                        size="3",
                                        variant="solid",
                                        color_scheme="teal",
                                    ),
                                    href="https://pages.razorpay.com/genetic-counseling",
                                    text_align="center"  # Centering the link
                                ),
                                display="flex",           # Use flex display
                                flex_direction="column",  # Stack elements vertically
                                align_items="center",     # Center items horizontally
                                justify_content="center", # Center items vertically
                                text_align="center"       # Ensure text is centered
                            ),
                            direction="column",
                            align="center",
                            width="100%",
                            margin_bottom="1rem",
                        ),
                        rx.text(
                            "Over 8 years of experience in Clinical Genomics and Genetics, particularly in the realm of Rare Diseases. I have led comprehensive genetic screening and research programs, significantly contributing to the scientific understanding of complex genomic questions.",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "With expertise in Genetic Analysis, Clinical Interpretation, and Genetic Reporting, I bring precision to the application of genomics in clinical practice.",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "As a Genetic Counselor and Geneticist, I specialize in providing personalized genetic guidance and insights to individuals, families, and healthcare providers. With extensive experience in clinical genetics, I support clients in understanding complex genetic information, empowering them to make informed health decisions. My expertise spans genetic testing, risk assessment, and interpretation of genetic conditions, with a focus on hereditary diseases, rare disorders, and personalized medicine.",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Through compassionate counseling, I assist patients in navigating the psychosocial and medical implications of genetic conditions, offering a supportive environment to discuss risks, preventive measures, and treatment options. I work closely with healthcare professionals to integrate genetic insights into patient care, helping translate cutting-edge genetic research into actionable healthcare strategies.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Key Expertise:",
                            size="6",
                            color="teal",
                            font_weight="bold",
                            margin_bottom="1rem",
                        ),
                        rx.unordered_list(
                            rx.list_item(
                                "Genetic counseling for hereditary and rare diseases"
                            ),
                            rx.list_item("Risk assessment for genetic disorders"),
                            rx.list_item(
                                "Interpretation of genetic testing results"
                            ),
                            rx.list_item(
                                "Personalized medicine and precision health"
                            ),
                            rx.list_item(
                                "Family planning and reproductive counseling"
                            ),
                            rx.list_item(
                                "Educating patients and healthcare professionals on genetic risks and conditions"
                            ),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Whether you're seeking genetic insights for personal or family health, or you need guidance on managing a hereditary condition or simply want to consult with an expert on a genetics-related question, I provide information, clarity, and support through every step of your genetic journey.",
                            style=mobile_paragraph_style,
                        ),
                        rx.accordion.root(
                                rx.accordion.item(
                                    header="What Is Genetic Counseling?",
                                    content=rx.box(
                                        rx.text(
                                            "Genetic counseling is a specialized service aimed at providing information and support to individuals and families to understand the medical and psychological implications of genetic conditions. It involves assessing the risk of inherited disorders, providing information on how genetics affects health, and guiding individuals on their options for diagnosis, prevention, and treatment.",
                                            style=paragraph_style,
                                        ),
                                        rx.text(
                                            "At Genomic Valley Bharat Limited, we integrate cutting-edge genomics with personalized care to offer comprehensive genetic counseling services. The mission is to empower families with knowledge, ensuring they make informed decisions about their health.",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                rx.accordion.item(
                                    header="Why Would Someone See a Genetic Counselor?",
                                    content=rx.box(
                                        rx.text(
                                            "There are many reasons someone might seek genetic counseling. You may be referred to a genetic counselor if you or your family have a history of:",
                                            style=paragraph_style,
                                        ),
                                        rx.unordered_list(
                                            rx.list_item("Inherited genetic conditions"),
                                            rx.list_item("Birth defects"),
                                            rx.list_item("Repeated pregnancy loss"),
                                            rx.list_item(
                                                "Cancers with hereditary links (such as breast, ovarian, or colon cancer)"
                                            ),
                                            rx.list_item("Concerns about family planning or fertility"),
                                            margin_left="2rem",
                                            style=paragraph_style,
                                        ),
                                        rx.text(
                                            "The experienced team at Genomic Valley is equipped to address these concerns with precision, offering genetic insights to support your healthcare journey.",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                rx.accordion.item(
                                    header="Who Should Get Genetic Counseling?",
                                    content=rx.box(
                                        rx.text(
                                            "Genetic counseling is beneficial for:",
                                            style=paragraph_style,
                                        ),
                                        rx.unordered_list(
                                            rx.list_item(
                                                "Individuals or couples with advanced maternal age planning to start a family"
                                            ),
                                            rx.list_item(
                                                "Those with a known family history of a genetic condition"
                                            ),
                                            rx.list_item("Pregnant women with abnormal prenatal test results"),
                                            rx.list_item(
                                                "Individuals diagnosed with or suspected for a genetic disorder"
                                            ),
                                            rx.list_item(
                                                "Cancer patients or those with a family history of hereditary cancers"
                                            ),
                                            margin_left="2rem",
                                            style=paragraph_style,
                                        ),
                                        rx.text(
                                            "Whether you’re looking for information before starting a family or navigating an existing health condition, Genomic Valley Bharat Limited provides tailored genetic counseling to guide you every step of the way.",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                rx.accordion.item(
                                    header="What Happens in Genetic Counseling?",
                                    content=rx.box(
                                        rx.text(
                                            "During a genetic counseling session, the counselor will gather detailed information about your family’s medical history and discuss any potential health concerns. They may suggest genetic testing to further explore your genetic risks and work with you to interpret the results. This process helps in understanding the likelihood of passing genetic conditions on to your children or managing inherited health risks.",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                rx.accordion.item(
                                    header="What Can I Expect in a Genetic Counseling Session?",
                                    content=rx.box(
                                        rx.text(
                                            "A typical genetic counseling session at Genomic Valley includes:",
                                            style=paragraph_style,
                                        ),
                                        rx.unordered_list(
                                            rx.list_item(
                                                "Comprehensive family health review: The counselor will review your medical and family history."
                                            ),
                                            rx.list_item(
                                                "Pedigree analysis: A pedigree chart is created from both parties (husband and wife) to assess inherited conditions."
                                            ),
                                            rx.list_item(
                                                "Education and guidance: You’ll receive detailed explanations about your genetic risks and available testing options."
                                            ),
                                            rx.list_item(
                                                "Psychosocial support: The counselor ensures that you are comfortable and supported throughout the process."
                                            ),
                                            rx.list_item(
                                                "Consent: Secure informed consent is the priority, making you fully aware of all procedures and tests involved."
                                            ),
                                            rx.list_item(
                                                "Interpretation of test results: If genetic testing is pursued, the counselor will explain the results in detail."
                                            ),
                                            rx.list_item(
                                                "Guidance on next steps: The counselor will help you make informed decisions about healthcare options."
                                            ),
                                            rx.list_item(
                                                "Written Summary of the session: Serves as a permanent record of the information discussed."
                                            ),
                                            margin_left="2rem",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                rx.accordion.item(
                                    header="When Might I See a Genetic Counselor?",
                                    content=rx.box(
                                        rx.text(
                                            "You may want to consider seeing a genetic counselor if:",
                                            style=paragraph_style,
                                        ),
                                        rx.unordered_list(
                                            rx.list_item(
                                                "You are planning a pregnancy and want to understand your genetic risks."
                                            ),
                                            rx.list_item(
                                                "You or your partner has a known genetic condition in the family."
                                            ),
                                            rx.list_item(
                                                "You’re pregnant, and your doctor suggests genetic screening or testing based on results or age."
                                            ),
                                            rx.list_item(
                                                "You have concerns about hereditary cancer risks or other inherited conditions."
                                            ),
                                            margin_left="2rem",
                                            style=paragraph_style,
                                        ),
                                        rx.text(
                                            "At Genomic Valley, the counselor is available to help you at every stage, from family planning to post-diagnosis care.",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                rx.accordion.item(
                                    header="What Are the Options After Genetic Counseling?",
                                    content=rx.box(
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
                                    ),
                                ),
                                rx.accordion.item(
                                    header="How Can I Find a Genetic Counsellor?",
                                    content=rx.box(
                                        rx.text(
                                            "Genomic Valley Bharat Limited provides an expert genetic counsellor with deep knowledge in genomics and healthcare. The counselor is highly skilled in guiding through complex genetic information and helping make choices that suit your personal situation. We ensure that each individual receives personalized care, comfort, and attention throughout their counselling journey.",
                                            style=paragraph_style,
                                        ),
                                    ),
                                ),
                                width="100%",
                                collapsible=True,
                                variant="ghost",
                                color_scheme="teal"
                            ),
                        rx.heading(
                            "Our Genetic Counselling Process",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "At Genomic Valley, the genetic counselling services are structured around comfort, clarity, and consent. Here’s how our process works:",
                            style=mobile_paragraph_style,
                        ),
                        rx.ordered_list(
                            rx.list_item(
                                "Consent: We ensure that you fully understand and agree to any testing or counseling services before proceeding."
                            ),
                            rx.list_item(
                                "Make the person comfortable: The counsellor takes time to create a relaxed environment, ensuring you feel supported throughout the session."
                            ),
                            rx.list_item(
                                "5-6 counseling sessions per day: We maintain a manageable number of sessions to ensure each individual gets adequate time and attention."
                            ),
                            rx.list_item(
                                "Pedigree chart from both parties (husband and wife): We create detailed family histories for both partners to assess hereditary risks and provide comprehensive insights."
                            ),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "At Genomic Valley Bharat Limited, we believe that personalized care and the integration of advanced genomics are essential to empowering individuals and families with the knowledge they need to make informed decisions about their health. Join us in our mission to revolutionize healthcare with expert genetic counseling.",
                            style=mobile_paragraph_style,
                        ),
                        rx.section(
                                rx.hstack(
                                    rx.link(
                                            rx.button(
                                                "Book Now",
                                                size="3",
                                                variant="solid",
                                                color_scheme="teal",
                                            ),
                                            href="https://pages.razorpay.com/genetic-counseling",
                                        ),
                                    rx.link(
                                            rx.button(
                                                "Contact Us",
                                                size="3",
                                                variant="solid",
                                                color_scheme="teal",
                                            ),
                                            href="/contact",
                                        ),    
                                ),
                                width="100%",
                                display="flex",         
                                justify_content="center"  
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
        ),
        margin="0",
        padding="0",
    )
