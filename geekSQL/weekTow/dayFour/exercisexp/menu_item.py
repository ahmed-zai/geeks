# menu_item.py

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

#   create the table if it doesn't exist
def create_table_if_not_exists():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
            item_id SERIAL PRIMARY KEY,
            item_name VARCHAR(30) NOT NULL,
            item_price SMALLINT DEFAULT 0
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

create_table_if_not_exists()



class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)",
                        (self.name, self.price))
            conn.commit()
            print("Item was added successfully.")
        finally:
            cur.close()
            conn.close()

    def delete(self):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM menu_items WHERE item_name = %s", (self.name,))
            conn.commit()
            if cur.rowcount > 0:
                print("Item was deleted successfully.")
            else:
                print("Error: Item not found.")
        finally:
            cur.close()
            conn.close()

    def update(self, new_name, new_price):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("UPDATE menu_items SET item_name = %s, item_price = %s WHERE item_name = %s",
                        (new_name, new_price, self.name))
            conn.commit()
            if cur.rowcount > 0:
                print("Item was updated successfully.")
            else:
                print("Error: Item not found.")
        finally:
            cur.close()
            conn.close()
