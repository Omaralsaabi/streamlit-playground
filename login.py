import streamlit as st
import hashlib
import json

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return True
    return False

def load_user_db():
    try:
        with open('database.json', 'r') as f:
            db = json.load(f)
    except FileNotFoundError:
        db = {}
    return db

def save_user_db(db):
    with open('database.json', 'w') as f:
        json.dump(db, f)

def main(): 
    st.title('Labeah NLU Engine')
    st.sidebar.image('/mnt/sata/FutureLookITC/streamlit-playground/labeh-logo.png', width=100)

    if 'login_status' not in st.session_state:
        st.session_state['login_status'] = False
        st.session_state['user'] = None

    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    db = load_user_db()  # Load the database

    if choice == "Home":
        if st.session_state['login_status']:
            st.subheader(f"Welcome, {st.session_state['user']}!")
            st.write("You are now logged in. You can access all the features of the application.")
            if st.button('Logout'):
                st.session_state['login_status'] = False
                st.session_state['user'] = None
                st.experimental_rerun()
        else:
            st.subheader("Home")
            st.info("Please log in to continue.")

    elif choice == "Login":
        if st.session_state['login_status']:
            st.subheader(f"Welcome back, {st.session_state['user']}!")
            if st.button('Logout'):
                st.session_state['login_status'] = False
                st.session_state['user'] = None
                st.experimental_rerun()
        else:
            st.subheader("Login Section")
            username = st.text_input("Username")
            password = st.text_input("Password", type='password')
            if st.button("Login"):
                if username in db and check_hashes(password, db[username]):
                    st.session_state['login_status'] = True
                    st.session_state['user'] = username
                    st.experimental_rerun()  # Rerun the app to update the state
                elif username in db and not check_hashes(password, db[username]):
                    st.warning("Incorrect password. Please try again.")
                else:
                    st.warning("Username not found. Please sign up.") 

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username", key="new_user")
        new_password = st.text_input("Password", type='password', key="new_pass")

        if st.button("Signup"):
            if new_user in db:
                st.warning("Username already exists.")
            else:
                db[new_user] = make_hashes(new_password)
                save_user_db(db)  # Save the updated database
                st.success("Account created successfully. Please go to the Login page to log in.")

if __name__ == '__main__':
    main()
