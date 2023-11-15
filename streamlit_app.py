import streamlit as st
import requests

def main():
    st.title('Streamlit Flask Integration')

    # User input for email and password
    email = st.text_input('Enter your email:')
    password = st.text_input('Enter your password:', type='password')

    # Button to send data to Flask server
    if st.button('Register User'):
        # Define the data payload
        data_payload = {'email': email, 'password': password}

        # Send a POST request to the Flask server
        response = requests.post('http://localhost:5000/new-user', json=data_payload)

        # Display the response from the server
        st.write('Response from Flask Server:')
        st.write(response.json())

if __name__ == '__main__':
    main()
