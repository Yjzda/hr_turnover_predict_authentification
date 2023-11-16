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

        try:
            # Send a POST request to the Flask server
            response = requests.post('http://localhost:5000/new-user', json=data_payload)

            # Display the response from the server
            st.write('Response from Flask Server:')
            st.write(response.json())

            # Check if the response indicates successful registration or access granted
            success_messages = ['User registered successfully', 'Access granted']
            if any(message in response.json().get('message', '') for message in success_messages):
                show_pages()

        except requests.exceptions.RequestException as e:
            st.error(f"Error communicating with Flask server: {e}")

def show_pages():
    st.sidebar.title('Navigation')

    # User can choose between Page 1, Page 2, and Page 3
    selected_page = st.sidebar.radio('Select a page:', ['Page 1', 'Page 2', 'Page 3'])

    # Button to send the selected page to the Flask server
    if st.sidebar.button('Send Page'):
        try:
            send_page(selected_page)
        except Exception as e:
            st.error(f"Error sending page to the Flask server: {e}")
    if selected_page == 'Page 1':
        st.write('Content of Page 1')
    elif selected_page == 'Page 2':
        st.write('Content of Page 2')
    elif selected_page == 'Page 3':
        st.write('Content of Page 3')

def send_page(selected_page):
    # Send the selected page to the Flask server (you can implement this part based on your needs)
    payload = {'selected_page': selected_page}
    response = requests.post('http://localhost:5000/send-page', json=payload)

    # Display the response from the server
    st.write('Response from Flask Server:')
    st.write(response.json())

    # Show content based on the selected page
    if selected_page == 'Page 1':
        st.write('Content of Page 1')
    elif selected_page == 'Page 2':
        st.write('Content of Page 2')
    elif selected_page == 'Page 3':
        st.write('Content of Page 3')

if __name__ == '__main__':
    main()
