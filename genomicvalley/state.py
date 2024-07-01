import reflex as rx

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
        
