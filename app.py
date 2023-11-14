# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Create SQLite database and table
import sqlite3
conn = sqlite3.connect('userdb.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE
    )
''')
conn.commit()
conn.close()

@app.route('/register_email', methods=['POST'])
def register_email():
    try:
        data = request.get_json()
        email = data.get('email')

        if not email:
            return jsonify({"error": "Email is required"}), 400

        # Save the email to the database
        conn = sqlite3.connect('userdb.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (email) VALUES (?)', (email,))
        conn.commit()
        conn.close()

        return jsonify({"message": f"Email '{email}' registered successfully"}), 200

    except Exception as e:
        print("Problem with data connection", e)
        return jsonify({"error": "Internal Server Error"}), 500



@app.route('/check_user_email', methods=['POST'])
def check_user_email():
    try:
        data = request.get_json()
        user_email = data.get('user_email')
        print(user_email)

        if not user_email:
            return jsonify({"error": "User email is required"}), 400

        # Check if the user_email is in the database
        conn = sqlite3.connect('userdb.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?', (user_email,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return jsonify({"message": f"User email '{user_email}' found in the database"}), 200
        else:
            return jsonify({"error": f"User email '{user_email}' not found in the database"}), 404

    except Exception as e:
        print("Problem with data connection", e)
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
