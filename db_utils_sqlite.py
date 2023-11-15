import sqlite3
import os
# -*- coding: utf-8 -*-

def get_connection(database="user_authentification.db"):
    # Check if the database file exists
    if not os.path.exists(database):
        print(f"Database file '{database}' does not exist. Creating and populating...")
        create_and_populate_database(database)
    # Connect to the SQLite database
    connection = sqlite3.connect(database)
    print(f"Connected to database '{database}'")
    return connection

def init_db():
    # Create a customer table in the database if it doesn't exist
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized")

def create_and_populate_database(database):
    new_connection = sqlite3.connect(database)
    with new_connection:
        new_connection.execute('INSERT INTO customer (email, password) VALUES (?, ?)',
                              ("initial_user@example.com", "initial_password"))
    print(f"Database '{database}' created and populated with initial data")

# Create and initialize the SQLite database
init_db()

# The rest of your code remains unchanged

def insert_user(email, password):
    connection = get_connection()
    with connection:
        connection.execute('INSERT INTO customer (email, password) VALUES (?, ?)',
                           (email, password))
    print(f"User inserted: Email - {email}, Password - {password}")

def get_user_by_email(email):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM customer WHERE email = ?', (email,))
    user = cursor.fetchone()

    user_dict = {'id': user[0], 'email': user[1], 'password': user[2]} if user else None
    return user_dict
   
# Example usage
if __name__ == '__main__':
    insert_user("test@example.com", "password123")



