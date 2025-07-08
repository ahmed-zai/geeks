# menu_manager.py

from menu_item import MenuItem, get_connection

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT item_name, price FROM menu_items WHERE item_name = %s", (name,))
            result = cur.fetchone()
            if result:
                return MenuItem(result[0], result[1])
            return None
        finally:
            cur.close()
            conn.close()

    @classmethod
    def all_items(cls):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT item_name, price FROM menu_items")
            rows = cur.fetchall()
            return [MenuItem(name, price) for name, price in rows]
        finally:
            cur.close()
            conn.close()
