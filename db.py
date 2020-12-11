import sqlite3


class Database:
    """A module of database that is created with sqlite3"""

    def __init__(self):
        """Initialization"""
        self.conn = sqlite3.connect('store.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name text, specialty text, number text, salary text)')
        self.conn.commit()

    def fetch(self):
        """Fetch rows"""
        self.cur.execute('SELECT * FROM customers')
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, specialty, number, salary):
        """Insert row"""
        self.cur.execute('INSERT INTO customers VALUES(NULL, ?, ?, ?, ?)',
                         (name, specialty, number, salary))
        self.conn.commit()

    def update(self, id, name, specialty, number, salary):
        """Update row"""
        self.cur.execute('UPDATE customers SET name = ?, specialty = ?, number = ?, salary = ? WHERE id = ?',
                         (name, specialty, number, salary, id))
        self.conn.commit()

    def remove(self, id):
        """Remove row"""
        self.cur.execute('DELETE FROM customers WHERE id = ?', (id, ))
        self.conn.commit()

    def __del__(self):
        """Desctructor"""
        self.conn.close()
