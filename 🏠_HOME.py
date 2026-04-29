import streamlit as  st
st.set_page_config(page_title="My Portfolio",page_icon="🖥️")
st.title("🖥️ Welcome to My Portfolio")


st.subheader("🏠Home")

st.subheader("Hi, I'm Yanesa 🤚")
st.write("Aspiring Developer | Designer | Tech Master")

st.info("Welcome to my portfolio! Explore my work and skills!.")


st.subheader("🙎‍♀️About Me")

st.write("I am a beginner, but i am hardworking and i love solving problems such as logics and creating various designs.")

st.subheader("👩‍🎓 EDUCATION")
st.write("- Bachelor of Science in Computer Science")

st.subheader("🎯 GOALS")
st.write("- Become a Full Stack Developer")
st.write("- Build impactful tech solutionss")


st.subheader("🛠️ Skills")

st.subheader("🖥️ Programming")
st.progress(80)
st.write("Python")

st.progress(50)
st.write("HTML")

st.progress(65)
st.write("CSS")

st.subheader("🎨 Design")
st.progress(80)
st.write("- Canva/ UI Designs")

st.subheader("⚒️ TOOLS")
st.write("- Streamlit")
st.write("- GitHub")
st.write("- Visual Studio Code")


st.subheader("🗂️ My Projects")

projects = {
    "Dormitory Management System": "🏢 Online Booking registration with reports",
    "Shopify":"🛒 Online Shopping"
}

for name, desc in projects.items():
    with st.expander(name):
        st.write(desc)


st.subheader("☎️ Contact Me")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Messagqe")

if st.button("SEND"):
    if name and email and message:
        st.success("Message sent Successfully! ✅")
    else:
        st.error("Please fill fields!")

st.markdown("### 🌐 Social Links")
st.write("- GitHub: https://github.com/yane-x4/Multipage-Portfolio")
st.write("- Facebook: https://web.facebook.com/http.yanee")


