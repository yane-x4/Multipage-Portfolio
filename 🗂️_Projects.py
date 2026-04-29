import streamlit as st

st.title("🗂️ MY PROJECTS")

projects = {
    "Dormitory Management System": "🏢 Online Booking registration with reports",
    "Shopify":"🛒 Online Shopping"
}

for name, desc in projects.items():
    with st.expander(name):
        st.write(desc)