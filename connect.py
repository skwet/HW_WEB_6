import sqlite3
from contextlib import contextmanager

database = './uni.db'

@contextmanager
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()
    