import reflex as rx


class EditorState(rx.State):
    content: str = "<p>Editor content</p>"

    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content


def editor():
    return rx.vstack(
        rx.editor(
            set_contents=EditorState.content,
            on_change=EditorState.handle_change,
        ),
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


def create_announcement() -> rx.Component:
    return rx.section(
        rx.card(
            rx.vstack(
                rx.form(
                    form_field(
                        label="Title", placeholder="Title", type="text", name="title"
                    ),
                    form_field(
                        label="Author", placeholder="Author", type="text", name="author"
                    ),
                    editor(),
                    rx.button("Submit", color_scheme="green", margin_top="20px"),
                )
            ),
            width="70%",
        ),
        width="100%",
        display="flex",
        justify_content="center",
        align_items="flex-start",
    )
