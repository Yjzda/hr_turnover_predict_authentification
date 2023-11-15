from flask import Flask, request, render_template, jsonify
from db_utils_sqlite import insert_user, get_user_by_email
# -*- coding: utf-8 -*-

inscripapp = Flask(__name__, template_folder='templates')

@inscripapp.route('/new-user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'GET':
        # Render the HTML form
        return render_template('signup_form.html')
    elif request.method == 'POST':
        # Retrieve user data from the form
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        # Check if the email already exists in the database
        existing_user = get_user_by_email(email)
        if existing_user:
            # If the email exists, check if the provided password matches the one in the database
            if existing_user['password'] == password:
                return jsonify({'message': 'User connected'}), 200
            else:
                return jsonify({'error': 'Incorrect password. Please try again.'}), 401
        else:
            # If the email does not exist, proceed with user registration
            insert_user(email, password)
            return jsonify({'message': 'User subscribed'}), 201

if __name__ == '__main__':
    inscripapp.run(debug=True)

