import streamlit as st

# Function to check email registration and password validation
def authenticate_email(email, password):
    # Dummy database of registered users and their passwords
    registered_users = {"user1@example.com": "password123", "user2@example.com": "securepass"}

    # Check if the email is registered
    if email in registered_users:
        stored_password = registered_users[email]

        # Check if the password is correct
        if password == stored_password:
            return "access_granted"
        else:
            return "access_denied"
    else:
        return "user_subscribed"

# Function for Page 1 content
def page1():
    st.title("Page 1 Content")
    st.write("Welcome to Page 1!")

# Function for Page 2 content
def page2():
    st.title("Page 2 Content")
    st.write("Welcome to Page 2!")

# Function for Page 3 content
def page3():
    st.title("Page 3 Content")
    st.write("Welcome to Page 3!")

# Main Streamlit app
def main():
    st.sidebar.title("Email Authentication")

    # Get the session state or create a new one
    session_state = st.session_state
    if not hasattr(session_state, "authenticated"):
        session_state.authenticated = False
        session_state.page_selection = None  # Set to None initially

    # Email authentication
    email = st.sidebar.text_input("Enter your email:")
    password = st.sidebar.text_input("Enter your password:", type="password")
    authenticate_button = st.sidebar.button("Authenticate")

    authentication_result = None  # Assign a default value

    if authenticate_button:
        authentication_result = authenticate_email(email, password)

        if authentication_result == "access_granted":
            session_state.authenticated = True
            st.sidebar.success("Access granted! Welcome back.")
        elif authentication_result == "access_denied":
            session_state.authenticated = False
            st.sidebar.error("Access denied. Please check your password.")
        elif authentication_result == "user_subscribed":
            session_state.authenticated = False
            st.sidebar.info("User subscribed. Please register or enter a valid email.")

    # Display content based on page selection
    if session_state.authenticated:
        session_state.page_selection = st.sidebar.radio("Select Page:", ["Page 1", "Page 2", "Page 3"], key="authenticated_page_selection")

        if session_state.page_selection == "Page 1":
            page1()
        elif session_state.page_selection == "Page 2":
            page2()
        elif session_state.page_selection == "Page 3":
            page3()

if __name__ == "__main__":
    main()
