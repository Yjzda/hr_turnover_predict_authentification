from flask import Flask, request, render_template, jsonify
from db_utils_sqlite import insert_user

inscripapp = Flask(__name__)

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

        # Call the insert_user function to add the user to the SQLite database
        insert_user(email, password)

        return jsonify({'message': 'Utilisateur inscrit avec succès'}), 201

if __name__ == '__main__':
    inscripapp.run(debug=True)
