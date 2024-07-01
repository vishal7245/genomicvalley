import reflex as rx

def file_row(text: str, filename: str) -> rx.Component:
    return rx.flex(
        rx.text(text, size="4", weight="bold", color="black"),
        rx.link(rx.button("Download", color_scheme="teal"), href=filename),
        justify="between",
        width="60%",  # Ensure the flex container takes full width
        align_items="center",  # Vertically center the items
    )

def investor_content() ->rx.Component:
    return rx.section(
        rx.vstack(
            rx.heading("Different Sections", size="9", margin_top="2rem", margin_bottom="1rem", color="teal", font_weight="bold"),
            file_row("Annual Report", "/annual_report.pdf"),
            file_row("Quarterly Report", "/quarterly_report.pdf"),
            file_row("Investor Presentation", "/investor_presentation.pdf"),
            file_row("Financial Statements", "/financial_statements.pdf"),
            width="100%",
            justify_content="center",
            align_items="center",
        ),
        width="100%",
    )