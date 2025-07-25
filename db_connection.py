import sqlite3

def get_db_connection():
    conn = sqlite3.connect('lost_and_found.db')
    return conn