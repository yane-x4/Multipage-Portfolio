import streamlit as st

st.title("☎️ CONTACT ME")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Messagqe")

if st.button("SEND"):
    if name and email and message:
        st.success("Message sent Successfully! ✅")
    else:
        st.error("Please fill fields!")

st.markdown("### 🌐 Social Links")
st.write("- GitHub: https://github.com/")
st.write("- Facebook: https://facebook.com/")
