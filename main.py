import streamlit as st
import re

# Function to check password strength
def password_strength(password):
    # Criteria for strong passwords
    if len(password) < 6:
        return 0, "Password too short!"
    if not re.search("[a-z]", password):
        return 1, "Password should contain at least one lowercase letter."
    if not re.search("[A-Z]", password):
        return 2, "Password should contain at least one uppercase letter."
    if not re.search("[0-9]", password):
        return 3, "Password should contain at least one number."
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return 4, "Password should contain at least one special character."
    
    return 5, "Strong password!"

# Streamlit app
st.title("Password Strength Checker")

# Input field for password
password = st.text_input("Enter Your Password", type="password")

if password:
    # Check password strength
    score, feedback = password_strength(password)

    # Display password strength
    if score == 0:
        st.warning("Very Weak Password! " + feedback)
    elif score == 1:
        st.warning("Weak Password! " + feedback)
    elif score == 2:
        st.info("Moderate Password! " + feedback)
    elif score == 3:
        st.success("Strong Password! " + feedback)
    elif score == 4:
        st.success("Very Strong Password! " + feedback)
    else:
        st.success("Excellent Password! " + feedback)
