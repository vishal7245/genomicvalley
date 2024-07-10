import reflex as rx


class ContactForm(rx.Model, table=True):
    first_name: str
    last_name: str
    phone: str
    email: str
    message: str
    timestamp: str
