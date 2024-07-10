import os
import smtplib
import sqlite3
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
import feedparser
import reflex as rx

load_dotenv()


class ContactDatabase:
    def __init__(self, db_name="contact_entries.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT,
            message TEXT,
            timestamp DATETIME
        )
        """)
        self.conn.commit()

    def add_entry(self, first_name, last_name, email, phone, message):
        cursor = self.conn.cursor()
        timestamp = datetime.now().isoformat()
        cursor.execute(
            """
        INSERT INTO contact_entries (first_name, last_name, email, phone, message, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
            (first_name, last_name, email, phone, message, timestamp),
        )
        self.conn.commit()

        # send mail
        sender_email = os.getenv("SENDER_EMAIL")
        receiver_email = os.getenv("RECEIVER_EMAIL")
        subject = "Genomic Valley Contact"
        body = f""" 
                Title: Genomic Valley Contact

                Message: {message}

                Name: {first_name} {last_name}
                Phone: {phone}
                Email: {email}
                timestamp: {timestamp}
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

    def close(self):
        self.conn.close()


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
