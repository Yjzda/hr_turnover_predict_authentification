from flask import Flask, request, jsonify
from db_utils_sqlite import insert_user

inscripapp = Flask(__name__)

@inscripapp.route('/new-user', methods=['POST'])
def new_user():
    if request.method == 'POST':
        # Récupérer les données du formulaire en JSON
        data = request.json
        print(data)

        email = data.get('email')
        password = data.get('password')

        if 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Email and password are required'}), 400

        print(f"Email: {email}, Password: {password}")

        # Call the insert_user function to add the user to the SQLite database
        insert_user(email, password)

        return jsonify({'message': 'Utilisateur inscrit avec succès'}), 201

if __name__ == '__main__':
    inscripapp.run(debug=True)
