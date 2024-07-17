import reflex as rx  # type: ignore
from genomicvalley.state import ContactDatabase


class FormState(rx.State):
    show_alert: bool = False
    alert_message: str = ""
    form_data: dict = {}

    def toggle_alert(self):
        self.show_alert = not self.show_alert

    def set_alert_message(self, message: str):
        self.alert_message = message
        self.show_alert = True

    def handle_form_submit(self, form_data: dict):
        self.form_data = form_data
        ContactDatabase.add_entry(
            form_data["first_name"],
            form_data["last_name"],
            form_data["email"],
            form_data["phone"],
            form_data["message"],
        )
        self.set_alert_message(
            "Thank you for your message! We'll get back to you soon."
        )


def alert_dialog():
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("Submission Received"),
            rx.alert_dialog.description(FormState.alert_message),
            rx.flex(
                rx.alert_dialog.action(
                    rx.button(
                        "Close",
                        on_click=FormState.toggle_alert,
                        style=button_style,
                    )
                ),
                justify="end",
            ),
        ),
        open=FormState.show_alert,
    )


def form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label, color="black"),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    type=type,
                    bg="rgba(39,162,85,0.2)",
                    color="black",
                    style={"& input::placeholder": {"color": "gray"}},
                    required=True,
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )


style_contact_form = {
    "background_color": "rgba(128,212,148,0.2);",
}


button_style = {
    "background_color": "teal",
    "color": "white",
    "border": "1px solid black",
}


def contact_form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="mail-plus", size=32, color="black"),
                    color_scheme="green",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Send us a message",
                        size="4",
                        weight="bold",
                        color="black",
                    ),
                    rx.text(
                        "Fill the form to contact us",
                        size="2",
                        color="black",
                    ),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            "First Name",
                            "First Name",
                            "text",
                            "first_name",
                        ),
                        form_field(
                            "Last Name",
                            "Last Name",
                            "text",
                            "last_name",
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        form_field(
                            "Email",
                            "user@reflex.dev",
                            "email",
                            "email",
                        ),
                        form_field("Phone", "Phone", "tel", "phone"),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        rx.text(
                            "Message",
                            style={
                                "font-size": "15px",
                                "font-weight": "500",
                                "line-height": "35px",
                                "color": "black",
                            },
                        ),
                        rx.text_area(
                            placeholder="Message",
                            name="message",
                            resize="vertical",
                            bg="rgba(39,162,85,0.2)",
                            color="black",
                            style={"& text_area::placeholder": {"color": "gray"}},
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.submit(
                        rx.button("Submit", style=button_style),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=FormState.handle_form_submit,
                reset_on_submit=True,
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
        style=style_contact_form,
        max_width="400px",
    )


def contact_section() -> rx.Component:
    return rx.section(
        rx.desktop_only(
            rx.section(
                rx.vstack(
                    rx.heading(
                        "CONTACT",
                        size="5",
                        weight="bold",
                        margin_bottom="1em",
                        color="green",
                    ),
                    rx.heading(
                        "Get in touch with us",
                        size="8",
                        weight="medium",
                        color="black",
                        margin_bottom="10px",
                    ),
                    rx.hstack(
                        rx.box(
                            rx.html(
                                """
                                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d223994.31177902033!2d76.92523341242645!3d28.692305172862714!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390d047309fff32f%3A0xfc5606ed1b5d46c3!2sDelhi!5e0!3m2!1sen!2sin!4v1719246581389!5m2!1sen!2sin" width="700" height="440" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                                """
                            ),
                            padding="1em",
                        ),
                        rx.box(
                            contact_form(),
                            padding="1em",
                            display="flex",
                        ),
                        width="100%",
                        spacing="1",
                        justify_content="center",
                        align_items="center",
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
                    rx.heading(
                        "CONTACT",
                        size="4",
                        weight="bold",
                        margin_bottom="1em",
                        color="green",
                    ),
                    rx.heading(
                        "Get in touch with us",
                        size="6",
                        weight="medium",
                        color="black",
                        margin_bottom="10px",
                    ),
                    rx.box(
                        rx.html(
                            """
                            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d223994.31177902033!2d76.92523341242645!3d28.692305172862714!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390d047309fff32f%3A0xfc5606ed1b5d46c3!2sDelhi!5e0!3m2!1sen!2sin!4v1719246581389!5m2!1sen!2sin" width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                            """
                        ),
                        padding="1em",
                        width="100%",
                    ),
                    rx.box(
                        contact_form(),
                        padding="1em",
                        width="100%",
                    ),
                    justify_content="center",
                    align_items="center",
                    width="100%",
                    spacing="4",
                ),
                width="100%",
            )
        ),
        alert_dialog(),
        width="100%",
    )
