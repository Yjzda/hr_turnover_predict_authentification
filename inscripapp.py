from flask import Flask, request, jsonify
from db_utils_sqlite import insert_user, get_user_by_email

app = Flask(__name__)

@app.route('/new-user', methods=['POST'])
def new_user():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    # Check if the email already exists in the database
    existing_user = get_user_by_email(email)
    if existing_user:
        return jsonify({'error': 'Email already exists. Please choose another email address.'}), 409
    else:
        # If the email does not exist, proceed with user registration
        insert_user(email, password)
        return jsonify({'message': 'Utilisateur inscrit avec succès'}), 201

if __name__ == '__main__':
    app.run(debug=True)
