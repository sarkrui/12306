import sqlite3

class DB:
    def __init__(self, name):
        self.db_name = name

    def insert(self, sql, values):
        print(f"Connecting to database: {self.db_name}")
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

    def select(self, sql, values):
        print(f"Connecting to database: {self.db_name}")
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchall()
        conn.close()
        return result

    def update(self, sql, values):
        print(f"Connecting to database: {self.db_name}")
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        conn.close()

    def delete(self, sql, values):
        print(f"Connecting to database: {self.db_name}")
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        conn.close()