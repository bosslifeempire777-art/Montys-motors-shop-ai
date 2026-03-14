import streamlit as st
import streamlit_authenticator as stauth
import hashlib

st.set_page_config(page_title="Monty's Motors Shop AI", page_icon="🔧", layout="wide")

credentials = {
    "usernames": {
        "greg": {"name": "Greg Montoya", "password": hashlib.sha256("montys1956".encode()).hexdigest(), "roles": ["admin"]},
        "tech1": {"name": "Tech One", "password": hashlib.sha256("tech123".encode()).hexdigest(), "roles": ["tech"]}
    }
}

authenticator = stauth.Authenticate(credentials, "montys_cookie", "montys1956secret", 30)

st.markdown("""
<div style="text-align: center; padding: 30px; background: linear-gradient(to right, #1a3c6d, #2c5282); color: white; border-radius: 12px;">
<h1>🔧 Monty's Motors Shop AI</h1>
<h3>Family Owned & Operated Since 1956</h3>
<p>601 E Fry Blvd, Sierra Vista, AZ | 520-458-2061</p>
</div>
""", unsafe_allow_html=True)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:

    roles = credentials["usernames"][username]["roles"]

    authenticator.logout("Logout", "sidebar")

    st.sidebar.title(f"Welcome, {name}")

    if "admin" in roles:

        st.sidebar.page_link("pages/01_Dashboard.py", label="Admin Dashboard")
        st.sidebar.page_link("pages/02_AI_Chat.py", label="AI Master Tech Chat")
        st.sidebar.page_link("pages/03_Schedule.py", label="Schedule")
        st.sidebar.page_link("pages/04_Customers.py", label="Customers")
        st.sidebar.page_link("pages/05_Inventory.py", label="Inventory")
        st.sidebar.page_link("pages/06_Invoices_Payroll.py", label="Invoices & Payroll")
        st.sidebar.page_link("pages/07_Resources.py", label="Reports")

    else:

        st.sidebar.page_link("pages/02_AI_Chat.py", label="AI Tech Chat")
        st.sidebar.page_link("pages/03_Schedule.py", label="My Work")

    st.success(f"Logged in as {name}")

else:

    st.warning("Please login")
  
