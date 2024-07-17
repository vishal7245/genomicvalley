import reflex as rx  # type: ignore
from genomicvalley.state import ContactDatabase


def contact_entry_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name", color="black"),
                rx.table.column_header_cell("Email", color="black"),
                rx.table.column_header_cell("Phone", color="black"),
                rx.table.column_header_cell("Message", color="black"),
                rx.table.column_header_cell("Date", color="black"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                ContactDatabase.entries,
                lambda contact: rx.table.row(
                    rx.table.cell(
                        f"{contact.first_name} {contact.last_name}", color="black"
                    ),
                    rx.table.cell(contact.email, color="black"),
                    rx.table.cell(contact.phone, color="black"),
                    rx.table.cell(contact.message, color="black"),
                    rx.table.cell(contact.date, color="black"),
                ),
            )
        ),
    )


def contact_entries() -> rx.Component:
    return rx.vstack(
        contact_entry_table(),
        width="100%",
        align_items="stretch",
        margin_top="3em",
        padding="3em",
    )
