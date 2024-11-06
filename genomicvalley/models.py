from __future__ import annotations
import reflex as rx
from sqlmodel import Field




class ContactForm(rx.Model, table=True):
    first_name: str
    last_name: str
    phone: str
    email: str
    message: str
    date: str
    seen: bool
    month: int
    year: int





