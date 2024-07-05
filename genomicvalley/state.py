import reflex as rx
import feedparser
import sqlite3
from datetime import datetime

class ContactDatabase:
    def __init__(self, db_name="contact_entries.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT,
            message TEXT,
            timestamp DATETIME
        )
        ''')
        self.conn.commit()

    def add_entry(self, first_name, last_name, email, phone, message):
        cursor = self.conn.cursor()
        timestamp = datetime.now().isoformat()
        cursor.execute('''
        INSERT INTO contact_entries (first_name, last_name, email, phone, message, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, email, phone, message, timestamp))
        self.conn.commit()

    def close(self):
        self.conn.close()
        

class GetRss:
    rss_urls = [
        "https://health.economictimes.indiatimes.com/rss/diagnostics",
        "https://health.economictimes.indiatimes.com/rss/medical-devices"
    ]

    @classmethod
    def getnews(cls):
        news = []
        for url in cls.rss_urls:
            entry = cls.parse_news(url)
            news = cls.merge_lists(news, entry)
        return news

    @staticmethod
    def parse_news(url):
        data = feedparser.parse(url)
        entries = data.get('entries', [])
        return [
            {
                'title': entry.get('title', ''),
                'link': entry.get('link', ''),
                'summary': entry.get('summary', '')
            }
            for entry in entries
        ]

    @staticmethod
    def merge_lists(list1, list2):
        merged_list = []
        for item1, item2 in zip(list1, list2):
            merged_list.extend([item1, item2])
        merged_list.extend(list1[len(list2):] + list2[len(list1):])
        return merged_list
        
