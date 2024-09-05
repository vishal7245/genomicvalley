import reflex as rx

from genomicvalley.components.footer import footer
from genomicvalley.components.navbar_2 import navbar_white as navbar
from genomicvalley.components.banner import banner
from genomicvalley.components.image_gallery import image_gallery
from genomicvalley.components.team_section import team_section

paragraph_style = {
    "font-size": "1.2rem",
    "color": "gray",
    "margin-bottom": "1rem",
    "text-align": "justify",
}

first_paragraph_style = {
    "font-size": "1.2rem",
    "color": "gray",
    "margin-bottom": "1rem",
    "text-align": "justify",
}

image_style = {
    "width": "100%",
    "height": "auto",
    "object-fit": "cover",
    "margin-bottom": "1rem",
}

image_urls = [
    "/c6.png",  
    "/c5.png",
    "/c14.png",
]


mobile_paragraph_style = {
    "font-size": "1rem",
    "color": "gray",
    "margin-bottom": "1rem",
    "text-align": "justify",
}


@rx.page(route="/about", title="About Us")
def about_us():
    return rx.section(
        rx.desktop_only(
            rx.vstack(
                navbar(),
                banner("About Us"),
                rx.html("""
                        <style>
                        #first-paragraph::first-letter {
                            font-size: 120px; /* Increase the size */
                            font-weight: bold; /* Make it bold */
                            float: left; /* Align it to the left */
                            margin-right: 5px; /* Add some space between the letter and the rest of the text */
                        }
                        </style>
                        """),
                rx.box(
                rx.hstack(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Welcome to Genomic Valley Biotech Limited, where innovation meets expertise to revolutionize healthcare. With a dedicated team boasting over 10 years of experience in Next-Generation Sequencing (NGS), oncology, and Artificial Intelligence (AI), we are at the forefront of integrating advanced technologies into biotechnology and healthcare solutions. Our team comprises highly skilled professionals passionate about utilizing their extensive knowledge to drive forward the fields of oncology research and diagnostics. We are committed to implementing both novel and validated methods, ensuring the delivery of accurate and confident results in our pursuit of better healthcare outcomes.",
                                style=first_paragraph_style,
                                id="first-paragraph",
                            ),
                            rx.text(
                                "We are inspired by the visionary dream of India's former Prime Minister Shri Atal Bihari Vajpayee to create a Silicon Valley of genomics right here in India. We are on an exhilarating journey to transform this dream into reality by driving innovation and excellence in the field of genomics. Our mission is to establish Genomics Valley as a global epicenter for genomic research, diagnostics, and healthcare solutions, much like Silicon Valley has become for technology. At Genomics Valley Bharat Limited, we believe in the transformative power of AI and IT. By leveraging these cutting-edge technologies, we aim to enhance the precision, efficiency, and effectiveness of oncology diagnostics and research, ultimately contributing to a healthier future for all. Join us on our journey as we pave the way for innovative solutions in biotechnology and healthcare.",
                                style=paragraph_style,
                            ),
                            rx.heading("Our Vision", size="9", margin_top="2rem", margin_bottom="1rem", color="teal", font_weight="bold", id="our-vision"),
                            rx.text(
                                "At Genomic Valley Biotech Limited, our vision is to propel molecular diagnostics into a new era of precision and efficiency through the integration of novel AI-based approaches. We are dedicated to advancing modern healthcare by offering more accurate diagnostics, backed by comprehensive metadata, delivered in significantly less time. Our goal is to provide personalized therapy options, empowering doctors with robust support for decision-making and enabling the identification of effective treatment options. By harnessing the power of AI and IT, we aim to transform oncology research and diagnostics, ensuring that patients receive the most precise and timely care possible.",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "We envision a future where cutting-edge technology and human expertise converge to revolutionize the landscape of molecular diagnostics. Our commitment to innovation and excellence drives us to continuously explore and implement advanced methods, ultimately improving patient outcomes and contributing to the advancement of global healthcare. We are committed to providing comprehensive Research Process Outsourcing (RPO) services tailored to global researchers. With a dedicated team of experts and access to professional software tools, we ensure refined data analysis and deliver optimal solutions. Our services aim to empower researchers worldwide by enhancing their projects with advanced analytical capabilities and meticulous attention to detail.",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Join us in our mission to shape the future of diagnostics and treatment, creating a world where technology and healthcare work hand in hand to deliver unparalleled results.",
                                style=paragraph_style,
                            ),
                        ),
                        width="60vw",
                        p="4",
                        padding="4rem",
                    ),
                    rx.box(
                        rx.vstack(
                            *[rx.image(src=url, style=image_style) for url in image_urls],
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

                image_gallery(),
                team_section(),
                footer(),
                spacing="0",
                width="100%",
            ),    
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                navbar(),
                banner("About Us"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Welcome to Genomic Valley Biotech Limited, where innovation meets expertise to revolutionize healthcare. With a dedicated team boasting over 10 years of experience in Next-Generation Sequencing (NGS), oncology, and Artificial Intelligence (AI), we are at the forefront of integrating advanced technologies into biotechnology and healthcare solutions.",
                            style=mobile_paragraph_style,
                            id="first-paragraph-mobile",
                        ),
                        rx.text(
                            "We are inspired by the visionary dream of India's former Prime Minister Shri Atal Bihari Vajpayee to create a Silicon Valley of genomics right here in India. We are on an exhilarating journey to transform this dream into reality by driving innovation and excellence in the field of genomics.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading("Our Vision", size="7", margin_top="2rem", margin_bottom="1rem", color="teal", font_weight="bold", id="our-vision-mobile"),
                        rx.text(
                            "At Genomic Valley Biotech Limited, our vision is to propel molecular diagnostics into a new era of precision and efficiency through the integration of novel AI-based approaches. We are dedicated to advancing modern healthcare by offering more accurate diagnostics, backed by comprehensive metadata, delivered in significantly less time.",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "We envision a future where cutting-edge technology and human expertise converge to revolutionize the landscape of molecular diagnostics. Our commitment to innovation and excellence drives us to continuously explore and implement advanced methods, ultimately improving patient outcomes and contributing to the advancement of global healthcare.",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Join us in our mission to shape the future of diagnostics and treatment, creating a world where technology and healthcare work hand in hand to deliver unparalleled results.",
                            style=mobile_paragraph_style,
                        ),
                        width="90%",
                        spacing="4",
                        padding="2rem",
                    ),
                ),
                rx.box(
                    rx.vstack(
                        *[rx.image(src=url, style=image_style) for url in image_urls[:2]],  # Displaying fewer images for mobile
                    ),
                    width="90%",
                    p="4",
                    padding="2rem",
                ),
                image_gallery(),
                team_section(),
                footer(),
                spacing="0",
                width="100%",
            )
        ),
        width="100%",
        padding="0px",
    )