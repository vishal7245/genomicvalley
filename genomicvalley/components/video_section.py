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
                    rx.video(
                        url="/lab-vid1.mp4",
                        width="60%",
                        height="auto",
                    ),
                    spacing="4",
                    align_items="center",
                    justify_content="center",
                    width="100%",
                ),
                width="100%",
            )
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
                    rx.video(
                        url="/lab-vid1.mp4",
                        width="90%",
                        height="auto",
                    ),
                    spacing="4",
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
