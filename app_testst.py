import streamlit as st
from streamlit.proto.Selectbox_pb2 import Selectbox


def authenticate_email(email):
 
    return bool(email)


def page1():
    st.title("Page 1 Content")
    st.write("Welcome to Page 1!")


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

  
    session_state = st.session_state
    if not hasattr(session_state, "authenticated"):
        session_state.authenticated = False
        session_state.page_selection = "Page 1"

    # Email authentication
    email = st.sidebar.text_input("Enter your email:")
    authenticate_button = st.sidebar.button("Authenticate")

    if authenticate_button:
        if authenticate_email(email):
            session_state.authenticated = True
            st.sidebar.success("Authentication successful!")
        else:
            session_state.authenticated = False
            st.sidebar.error("Authentication failed. Please enter a valid email.")

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
