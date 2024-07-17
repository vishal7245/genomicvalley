import reflex as rx


def drawer() -> rx.Component:
    return rx.box(
        rx.drawer.root(
            rx.box(
                rx.drawer.trigger(rx.button("Menu", width="100%")),
                position="fixed",
                top="1em",
                left="1em",
                z_index="100",
            ),
            rx.drawer.overlay(z_index="5"),
            rx.drawer.portal(
                rx.drawer.content(
                    rx.vstack(
                        rx.link(
                            rx.button("Dashboard", width="100%"), href="/dashboard"
                        ),
                        rx.link(
                            rx.button("Logout", width="100%", margin_bottom="2em"),
                            href="/logout",
                        ),
                        rx.drawer.close(rx.button("Close", width="100%")),
                        rx.link(
                            rx.button("Contact Entries", width="100%"),
                            href="/contact_dashboard",
                        ),
                        rx.button("Career Entries", width="100%"),
                        rx.button("Internship Entries", width="100%"),
                        rx.button("Create Announcement", width="100%"),
                        rx.button("Manage Announcement", width="100%"),
                        width="100%",
                        spacing="1",
                        align_items="stretch",
                    ),
                    top="auto",
                    right="auto",
                    height="100%",
                    width="20em",
                    padding="2em",
                    background_color="#FFF",
                )
            ),
            direction="left",
        )
    )
