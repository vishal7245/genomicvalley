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

desktop_image_style = {
    "width": "48%",  # Each image takes up 48% of the width in hstack
    "height": "250px",  # Fixed height to ensure uniformity
    "object-fit": "cover",
    "margin-bottom": "1rem",
}

mobile_image_style = {
    "width": "100%",
    "height": "auto",
    "object-fit": "cover",
    "margin-bottom": "1rem",
}

centered_image_style = {
    "width": "60%",
    "height": "auto",
    "object-fit": "cover",
    "margin-bottom": "1rem",
    "display": "block",
    "margin-left": "auto",
    "margin-right": "auto",
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


@rx.page(route="/plant-genome", title="Plant Genome")
def plant_genome():
    return rx.section(
        rx.desktop_only(  # Start of desktop layout
            rx.vstack(
                navbar(),
                banner("Plant Genomics"),
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "Welcome to Genomic Valley, where innovation meets plant health. Our expertise in plant genomics enables us to deliver cutting-edge tools and technologies that drive sustainable agriculture and enhance crop productivity. One of our flagship products is the Plant Pathogen Detection Kit, designed to detect a range of plant diseases with precision, speed, and reliability.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Plant Pathogen Detection Kit",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "Our Plant Pathogen Detection Kit represents a significant leap forward in plant disease diagnostics. Using state-of-the-art genomic techniques, such as Polymerase Chain Reaction (PCR) and Next-Generation Sequencing (NGS), this kit enables rapid and accurate identification of multiple plant pathogens. By detecting pathogens at the molecular level, it allows for early intervention, preventing widespread crop damage and minimizing economic losses.",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Key features of the kit include:",
                                font_weight="bold",
                                margin_top="1rem",
                                margin_bottom="0.5rem",
                                style=paragraph_style,
                            ),
                            rx.unordered_list(
                                rx.list_item(
                                    "Multi-pathogen detection: Simultaneous identification of various plant pathogens."
                                ),
                                rx.list_item(
                                    "Real-time diagnostics: Fast and reliable results for immediate action."
                                ),
                                rx.list_item(
                                    "Field-ready application: Designed for both laboratory and on-site usage."
                                ),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "This tool is essential for farmers, researchers, and agricultural professionals focused on ensuring crop health and maximizing yield potential.",
                                style=paragraph_style,
                            ),
                            rx.heading(
                                "Key Plant Pathogens Detected by the Plant Pathogen Detection Kit",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            # Blister Blight
                            rx.heading(
                                "Blister Blight",
                                size="8",
                                margin_top="1.5rem",
                                margin_bottom="1rem",
                                color="black",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Pathogen Type: Bacterial"),
                                rx.list_item(
                                    "Crops Affected: Vegetables and leafy crops"
                                ),
                                rx.list_item("Impact:"),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Blister Blight is a bacterial pathogen that causes significant crop loss through leaf spots, wilting, and blight. Due to its rapid spread, early detection is crucial for effective outbreak management. The Plant Pathogen Detection Kit identifies Blister Blight at the genetic level, enabling quick intervention and treatment to minimize damage and prevent large-scale loss.",
                                style=paragraph_style,
                            ),
                            rx.hstack(
                                rx.image(
                                    "/Blister Blight_1.jpg",
                                    style=desktop_image_style,
                                ),
                                rx.image(
                                    "/Blister Blight_2.jpeg",
                                    style=desktop_image_style,
                                ),
                                width="100%",
                                justify_content="space-between",
                                align_items="center",
                            ),
                            # Wheat Rust
                            rx.heading(
                                "Wheat Rust",
                                size="8",
                                margin_top="1.5rem",
                                margin_bottom="1rem",
                                color="black",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item(
                                    "Pathogen Type: Fungal (Puccinia spp.)"
                                ),
                                rx.list_item("Crops Affected: Wheat"),
                                rx.list_item("Impact:"),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Wheat Rust is a highly destructive fungal disease that poses a severe threat to global wheat production. Characterized by rust-coloured pustules on leaves, it can devastate crops if left unchecked. Early detection through our kit facilitates timely fungicide application, reducing crop loss and helping to safeguard food security.",
                                style=paragraph_style,
                            ),
                            rx.hstack(
                                rx.image(
                                    "/Wheat rust_1.jpg",
                                    style=desktop_image_style,
                                ),
                                rx.image(
                                    "/Wheat rust_2.jpg",
                                    style=desktop_image_style,
                                ),
                                width="100%",
                                justify_content="space-between",
                                align_items="center",
                            ),
                            # Rhizobacter Saloni
                            rx.heading(
                                "Rhizobacter Saloni",
                                size="8",
                                margin_top="1.5rem",
                                margin_bottom="1rem",
                                color="black",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Pathogen Type: Fungal"),
                                rx.list_item(
                                    "Crops Affected: Root and tuber crops"
                                ),
                                rx.list_item("Impact:"),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Rhizobacter Saloni is a fungal pathogen that primarily attacks plant root systems, causing nutrient deficiencies and eventual plant death. Its underground activity makes it difficult to detect through visual inspection. However, our genomic detection kit identifies the pathogen early on, allowing for swift action to protect crops from root rot and other related issues.",
                                style=paragraph_style,
                            ),
                            rx.image(
                                "/Rhizobacteria Solani_1.jpg",
                                style=centered_image_style,
                            ),
                            # Apple Scab
                            rx.heading(
                                "Apple Scab (Venturia inaequalis)",
                                size="8",
                                margin_top="1.5rem",
                                margin_bottom="1rem",
                                color="black",
                                font_weight="bold",
                            ),
                            rx.unordered_list(
                                rx.list_item("Pathogen Type: Fungal"),
                                rx.list_item("Crops Affected: Apples"),
                                rx.list_item("Impact:"),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Apple Scab, caused by the fungus Venturia inaequalis, is a major disease impacting apple orchards globally. It produces scabby lesions on fruit and foliage, reducing the quality and market value of the fruit. Early detection through our kit enables precise fungicide application, ensuring healthy apple harvests and protecting growers from economic losses.",
                                style=paragraph_style,
                            ),
                            rx.hstack(
                                rx.image(
                                    "/Apple Scab_1.jpg",
                                    style=desktop_image_style,
                                ),
                                rx.image(
                                    "/Apple Scab_2.jpg",
                                    style=desktop_image_style,
                                ),
                                width="100%",
                                justify_content="space-between",
                                align_items="center",
                            ),
                            rx.heading(
                                "Why Choose Genomic Valley?",
                                size="9",
                                margin_top="2rem",
                                margin_bottom="1rem",
                                color="teal",
                                font_weight="bold",
                            ),
                            rx.text(
                                "At Genomic Valley, we are committed to advancing plant health through genomic research and innovation. Our solutions are designed with the end-user in mind, offering practical, reliable, and cost-effective tools for disease management. By leveraging the latest in plant genomics, we empower agricultural professionals to make informed decisions, protect their crops, and enhance yield outcomes.",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Key Advantages of Our Solutions:",
                                font_weight="bold",
                                margin_top="1rem",
                                margin_bottom="0.5rem",
                                style=paragraph_style,
                            ),
                            rx.unordered_list(
                                rx.list_item(
                                    "Precision diagnostics for early and accurate pathogen detection."
                                ),
                                rx.list_item(
                                    "Innovative technology grounded in robust genomic science."
                                ),
                                rx.list_item(
                                    "Sustainable agriculture by reducing dependency on chemical interventions."
                                ),
                                margin_left="2rem",
                                style=paragraph_style,
                            ),
                            rx.text(
                                "Explore the possibilities with Genomic Valley and take a proactive approach to plant pathogen management. Together, we can safeguard global food production and ensure a greener, healthier future for agriculture.",
                                style=paragraph_style,
                                margin_top="2rem",
                                font_weight="bold",
                            ),
                            rx.button(
                                "Contact Us Today",
                                on_click=rx.redirect("/contact"),
                                style=button_style,
                            ),
                        ),
                        width="70vw",
                        p="4",
                        padding="4rem",
                    ),
                    width="100%",
                    justify_content="center",
                    align_items="center",
                ),
                footer(),
            ),
            width="100%",
            padding="0px",
        ),  # End of desktop layout
        rx.mobile_and_tablet(  # Start of mobile layout
            rx.vstack(
                navbar(),
                banner("Plant Genomics"),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Welcome to Genomic Valley, where innovation meets plant health. Our expertise in plant genomics enables us to deliver cutting-edge tools and technologies that drive sustainable agriculture and enhance crop productivity. One of our flagship products is the Plant Pathogen Detection Kit, designed to detect a range of plant diseases with precision, speed, and reliability.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Plant Pathogen Detection Kit",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "Our Plant Pathogen Detection Kit represents a significant leap forward in plant disease diagnostics. Using state-of-the-art genomic techniques, such as Polymerase Chain Reaction (PCR) and Next-Generation Sequencing (NGS), this kit enables rapid and accurate identification of multiple plant pathogens. By detecting pathogens at the molecular level, it allows for early intervention, preventing widespread crop damage and minimizing economic losses.",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Key features of the kit include:",
                            font_weight="bold",
                            margin_top="1rem",
                            margin_bottom="0.5rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.unordered_list(
                            rx.list_item(
                                "Multi-pathogen detection: Simultaneous identification of various plant pathogens."
                            ),
                            rx.list_item(
                                "Real-time diagnostics: Fast and reliable results for immediate action."
                            ),
                            rx.list_item(
                                "Field-ready application: Designed for both laboratory and on-site usage."
                            ),
                            margin_left="1rem",  # Smaller margin for mobile
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "This tool is essential for farmers, researchers, and agricultural professionals focused on ensuring crop health and maximizing yield potential.",
                            style=mobile_paragraph_style,
                        ),
                        rx.heading(
                            "Key Plant Pathogens Detected by the Plant Pathogen Detection Kit",
                            size="7",  # Smaller heading size for mobile
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        # Blister Blight
                        rx.heading(
                            "Blister Blight",
                            size="6",
                            margin_top="1.5rem",
                            margin_bottom="1rem",
                            color="black",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Pathogen Type: Bacterial"),
                            rx.list_item(
                                "Crops Affected: Vegetables and leafy crops"
                            ),
                            rx.list_item("Impact:"),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Blister Blight is a bacterial pathogen that causes significant crop loss through leaf spots, wilting, and blight. Due to its rapid spread, early detection is crucial for effective outbreak management. The Plant Pathogen Detection Kit identifies Blister Blight at the genetic level, enabling quick intervention and treatment to minimize damage and prevent large-scale loss.",
                            style=mobile_paragraph_style,
                        ),
                        rx.vstack(
                            rx.image(
                                "/Blister Blight_1.jpg",
                                style=mobile_image_style,
                            ),
                            rx.image(
                                "/Blister Blight_2.jpeg",
                                style=mobile_image_style,
                            ),
                        ),
                        # Wheat Rust
                        rx.heading(
                            "Wheat Rust",
                            size="6",
                            margin_top="1.5rem",
                            margin_bottom="1rem",
                            color="black",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item(
                                "Pathogen Type: Fungal (Puccinia spp.)"
                            ),
                            rx.list_item("Crops Affected: Wheat"),
                            rx.list_item("Impact:"),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Wheat Rust is a highly destructive fungal disease that poses a severe threat to global wheat production. Characterized by rust-coloured pustules on leaves, it can devastate crops if left unchecked. Early detection through our kit facilitates timely fungicide application, reducing crop loss and helping to safeguard food security.",
                            style=mobile_paragraph_style,
                        ),
                        rx.vstack(
                            rx.image(
                                "/Wheat rust_1.jpg",
                                style=mobile_image_style,
                            ),
                            rx.image(
                                "/Wheat rust_2.jpg",
                                style=mobile_image_style,
                            ),
                        ),
                        # Rhizobacter Saloni
                        rx.heading(
                            "Rhizobacter Saloni",
                            size="6",
                            margin_top="1.5rem",
                            margin_bottom="1rem",
                            color="black",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Pathogen Type: Fungal"),
                            rx.list_item(
                                "Crops Affected: Root and tuber crops"
                            ),
                            rx.list_item("Impact:"),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Rhizobacter Saloni is a fungal pathogen that primarily attacks plant root systems, causing nutrient deficiencies and eventual plant death. Its underground activity makes it difficult to detect through visual inspection. However, our genomic detection kit identifies the pathogen early on, allowing for swift action to protect crops from root rot and other related issues.",
                            style=mobile_paragraph_style,
                        ),
                        rx.image(
                            "/Rhizobacteria Solani_1.jpg",
                            style=mobile_image_style,
                        ),
                        # Apple Scab
                        rx.heading(
                            "Apple Scab (Venturia inaequalis)",
                            size="6",
                            margin_top="1.5rem",
                            margin_bottom="1rem",
                            color="black",
                            font_weight="bold",
                        ),
                        rx.unordered_list(
                            rx.list_item("Pathogen Type: Fungal"),
                            rx.list_item("Crops Affected: Apples"),
                            rx.list_item("Impact:"),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Apple Scab, caused by the fungus Venturia inaequalis, is a major disease impacting apple orchards globally. It produces scabby lesions on fruit and foliage, reducing the quality and market value of the fruit. Early detection through our kit enables precise fungicide application, ensuring healthy apple harvests and protecting growers from economic losses.",
                            style=mobile_paragraph_style,
                        ),
                        rx.vstack(
                            rx.image(
                                "/Apple Scab_1.jpg",
                                style=mobile_image_style,
                            ),
                            rx.image(
                                "/Apple Scab_2.jpg",
                                style=mobile_image_style,
                            ),
                        ),
                        rx.heading(
                            "Why Choose Genomic Valley?",
                            size="7",
                            margin_top="2rem",
                            margin_bottom="1rem",
                            color="teal",
                            font_weight="bold",
                        ),
                        rx.text(
                            "At Genomic Valley, we are committed to advancing plant health through genomic research and innovation. Our solutions are designed with the end-user in mind, offering practical, reliable, and cost-effective tools for disease management. By leveraging the latest in plant genomics, we empower agricultural professionals to make informed decisions, protect their crops, and enhance yield outcomes.",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Key Advantages of Our Solutions:",
                            font_weight="bold",
                            margin_top="1rem",
                            margin_bottom="0.5rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.unordered_list(
                            rx.list_item(
                                "Precision diagnostics for early and accurate pathogen detection."
                            ),
                            rx.list_item(
                                "Innovative technology grounded in robust genomic science."
                            ),
                            rx.list_item(
                                "Sustainable agriculture by reducing dependency on chemical interventions."
                            ),
                            margin_left="1rem",
                            style=mobile_paragraph_style,
                        ),
                        rx.text(
                            "Explore the possibilities with Genomic Valley and take a proactive approach to plant pathogen management. Together, we can safeguard global food production and ensure a greener, healthier future for agriculture.",
                            style=mobile_paragraph_style,
                            margin_top="2rem",
                            font_weight="bold",
                        ),
                        rx.button(
                            "Contact Us Today",
                            on_click=rx.redirect("/contact"),
                            style=button_style,
                        ),
                    ),
                    width="100%",
                    p="2",  # smaller padding for mobile
                    padding="2rem",
                ),
                footer(),
                width="100%",
                spacing="2",  # smaller spacing for mobile
            ),
            width="100%",
        ),
        margin="0",
        padding="0",
    )
