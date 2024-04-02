import streamlit as st

st.set_page_config(page_title="Moni's Resume", layout="wide")
st.title("Hi, I am Moni :wave:")

def create_project(title, subheader, description, image):
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(image)
        with col2:
            st.subheader(title)
            st.markdown(f"**{subheader}**")
            for desc in description:
                st.write(f":gray[{desc}]")

with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(
            "### A designer<br /> in Interior & Product & UX & HMI"
        , unsafe_allow_html=True)
        st.write("""
        :gray[Used to be an interior designer.]\n

        :gray[Now doing some hardware and software product design, with the aspiration of becoming a versatile designer capable of working across different disciplines.]
        """)
    with col2:
        st.image("images/Me.jpg")

st.write("---")

st.header("Projects")

projects = [
    {
        "title": "HMI Design",
        "subheader": "AutoShuttle",
        "description": [
            "This is an HMI & APP designed for an automatic driving shuttle, aimed at assisting employees in facilities like Microsoft's campus for commuting short distances, such as to and from work."
        ],
        "image": "images/HMI.jpg"
    },
    {
        "title": "APP Design",
        "subheader": "Mini Program for Tai Koo Li Shopping Mall",
        "description": [
            "1. Book a parking space in advance to avoid blindly looking for a parking spot.",
            "2. Personalized recommended parking spot.",
            "3. Alarm reminder when necessary."
        ],
        "image": "images/APP.jpg"
    },
    {
        "title": "Product Design",
        "subheader": "ClimaSphere",
        "description": [
            "It is an elegant and intuitive weather station that can be hung at the door to remind users to bring an umbrella when they go out."
        ],
        "image": "images/Product.jpg"
    },
    {
        "title": "Interior Design",
        "subheader": "NDB Headquarters Building Interior Design",
        "description": [
            "The New Development Bank is a multinational bank headquarters located at Shanghai Expo Park, completed in 2022."
        ],
        "image": "images/Interior.jpg"
    }
]

for project in projects:
    create_project(project["title"], project["subheader"], project["description"], project["image"])

st.write("---")

with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        st.header("Skills")
        st.write("- **CAD / PS / InDesign / AI**")
        st.write("- **Rhino / Sketchup / Figma**")
        st.write("- **Python**")
    with col2:
        st.header("Contact")
        st.write("monihuangpro@gmail.com")