import reflex as rx

def video_section() -> rx.Component:
    return rx.section(
        rx.desktop_only(
            rx.section(
                rx.vstack(
                    rx.heading(
                        "Lab Tour",
                        size="5",
                        weight="bold",
                        margin_bottom="1em",
                        color="green",
                    ),
                    rx.heading(
                        "Our Laboratory Facilities",
                        size="8",
                        weight="medium",
                        color="black",
                        margin_bottom="10px",
                    ),
                    rx.text(
                        "Watch this tour to learn more about us.",
                        size="5",
                        align="center",
                        margin_bottom="1em",
                        color="gray",
                    ),
                    rx.box(
                        rx.hstack(
                            rx.vstack(
                                rx.video(
                                    url="/NGS-lab.mp4",
                                    width="100%",
                                    height="auto",
                                ),
                                rx.text(
                                    "NGS Lab",
                                    size="5",
                                    align="center",
                                    color="gray"
                                ),
                                spacing="0.5em",
                                align_items="center",
                                width="35%",  
                            ),
                            rx.vstack(
                                rx.video(
                                    url="/Pathology-lab.mp4",
                                    width="100%",
                                    height="auto",
                                ),
                                rx.text(
                                    "Pathology Lab",
                                    size="5",
                                    align="center",
                                    color="gray"
                                ),
                                spacing="0.5em",
                                align_items="center",
                                width="35%", 
                            ),
                            spacing="1em",
                            align_items="flex-start",
                            justify_content="center",
                        ),
                        width="100%",  
                        margin="0 auto",
                    ),
                    spacing="2em",
                    align_items="center",
                    justify_content="center",
                    width="100%",
                ),
                width="100%",
                padding="2em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.section(
                rx.vstack(
                    rx.heading(
                        "Lab Tour",
                        size="5",
                        weight="bold",
                        margin_bottom="1em",
                        color="green",
                        align="center",
                    ),
                    rx.heading(
                        "Our Laboratory Facilities",
                        size="6",
                        weight="medium",
                        color="black",
                        margin_bottom="10px",
                        align="center",
                    ),
                    rx.text(
                        "Watch this tour to learn more about us.",
                        size="4",
                        align="center",
                        margin_bottom="1em",
                        color="gray",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.vstack(
                                rx.video(
                                    url="/NGS-lab.mp4",
                                    width="100%",
                                    height="auto",
                                ),
                                rx.text(
                                    "NGS Lab",
                                    size="5",
                                    align="center",
                                    color="gray"
                                ),
                                spacing="0.5em",
                                align_items="center",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.video(
                                    url="/Pathology-lab.mp4",
                                    width="100%",
                                    height="auto",
                                ),
                                rx.text(
                                    "Pathology Lab",
                                    size="5",
                                    align="center",
                                    color="gray"
                                ),
                                spacing="0.5em",
                                align_items="center",
                                width="100%",
                            ),
                            spacing="2em",
                            width="100%",
                            align_items="center",
                        ),
                        width="100%",
                        align_items="center",
                        justify_content="center",
                    ),
                    spacing="2em",
                    align_items="center",
                    justify_content="center",
                    width="100%",
                ),
                justify_content="center",
                align_items="center",
                width="100%",
                padding="1em",
            )
        ),
        width="100%",
    )