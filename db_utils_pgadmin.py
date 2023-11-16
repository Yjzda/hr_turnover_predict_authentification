import psycopg2
import os

def get_connection(database="", user="postgres", password="physique1er", host="localhost"):
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print(f"Connected to database '{database}'")
    return connection

def init_db():
    # Create a user table in the database if it doesn't exist
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hruser (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized")

def insert_user(email, password):
    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO hruser (email, password) VALUES (%s, %s)', (email, password))
    print(f"User inserted: Email - {email}, Password - {password}")

def get_user_by_email(email):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM hruser WHERE email = %s', (email,))
        user = cursor.fetchone()

    user_dict = {'id': user[0], 'email': user[1], 'password': user[2]} if user else None
    return user_dict

if __name__ == '__main__':
    init_db()
    insert_user("test@example.com", "password123")
    result = get_user_by_email("test@example.com")
    print(result)




