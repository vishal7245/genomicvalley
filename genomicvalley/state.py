from __future__ import annotations
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import feedparser
import reflex as rx
from genomicvalley.models import ContactForm
import pytz
import datetime
from sqlmodel import Column, DateTime, Field, func
from sqlmodel import select
from typing import List, Dict, Any


LOGIN_ROUTE = "/admin"


load_dotenv()


class CityStats(rx.Model):
    city: str
    count: int


def getcurrentdate():
    utc_now = datetime.datetime.now(pytz.utc)

    # Convert to IST
    ist_tz = pytz.timezone("Asia/Kolkata")
    ist_now = utc_now.astimezone(ist_tz)

    # Format the date and time
    formatted_date = ist_now.strftime("%d/%m/%y")

    return f"{formatted_date}"


def getcurrentmonth():
    current_date = datetime.datetime.now()
    current_month = current_date.month
    return current_month


def getcurrentyear():
    current_date = datetime.datetime.now()
    current_year = current_date.year
    return current_year




class ContactDatabase(rx.State):
    entries: List[ContactForm] = []

    @classmethod
    def add_entry(cls, first_name, last_name, email, phone, message):  # send mail
        with rx.session() as session:
            session.add(
                ContactForm(
                    first_name=first_name,
                    last_name=last_name,
                    phone=str(phone),
                    email=email,
                    message=message,
                    date=str(getcurrentdate()),
                    seen=False,
                    month=getcurrentmonth(),
                    year=getcurrentyear(),
                )
            )
            session.commit()
        cls.send_email(first_name, last_name, email, phone, message)

    def get_entries(self):
        with rx.session() as session:
            entries = session.exec(select(ContactForm)).all()
            self.entries = entries

    @classmethod
    def send_email(cls, first_name, last_name, email, phone, message):
        sender_email = os.getenv("SENDER_EMAIL")
        receiver_email = os.getenv("RECEIVER_EMAIL")
        subject = "Genomic Valley Contact"
        body = f""" 
                Title: Genomic Valley Contact

                Message: {message}

                Name: {first_name} {last_name}
                Phone: {phone}
                Email: {email}
                Date: {getcurrentdate()}
                """

        smtp_server = "smtp.zoho.in"
        smtp_port = 587
        smtp_username = os.getenv("SENDER_EMAIL")
        smtp_password = os.getenv("PASSWORD")
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())


class GetRss:
    rss_urls = [
        "https://health.economictimes.indiatimes.com/rss/diagnostics",
        "https://health.economictimes.indiatimes.com/rss/medical-devices",
    ]

    @classmethod
    def getnews(cls):
        news = []
        for url in cls.rss_urls:
            entry = cls.parse_news(url)
            news = cls.merge_lists(news, entry)
        return news

    @classmethod
    def get_titles(cls):
        titles = []
        for url in cls.rss_urls:
            entries = cls.parse_news(url)
            titles.extend(entry["title"] for entry in entries)
        return titles

    @staticmethod
    def parse_news(url):
        data = feedparser.parse(url)
        entries = data.get("entries", [])
        return [
            {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "summary": entry.get("summary", ""),
            }
            for entry in entries
        ]

    @staticmethod
    def merge_lists(list1, list2):
        merged_list = []
        for item1, item2 in zip(list1, list2):
            merged_list.extend([item1, item2])
        merged_list.extend(list1[len(list2) :] + list2[len(list1) :])
        return merged_list


# Authentication Logic
#
#
#
