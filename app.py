import streamlit as st
import streamlit as st

# Custom CSS to inject for typography styles
st.markdown("""
<style>
.main-header {
    font-family: 'Helvetica', sans-serif;
    font-size: 24px;
    font-weight: bold;
}
.project-title {
    font-family: 'Helvetica', sans-serif;
    font-size: 20px;
    font-weight: bold;
}
.section-title {
    font-family: 'Helvetica', serif;
    font-size: 22px;
    font-weight: bold;
}
.content-text {
    font-family: 'Helvetica', sans-serif;
    font-size: 18px;
}
.contact-text {
    font-family: 'Helvetica', monospace;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Page Configuration
st.set_page_config(page_title="Moni's Personal Website", layout="wide")

# Introduction
st.markdown('<div class="main-header">Hi, I am Moni</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content-text">A designer in Interior & Product & UX & HMI. Used to be an interior designer.
Now doing some hardware and software product design with the aspiration of becoming a versatile designer capable of working across different disciplines.</div>
""", unsafe_allow_html=True)

# Projects
st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
projects = {
    "HMI Design: AutoShuttle": "This is an HMI & APP designed for an automatic driving shuttle aimed at assisting employees in facilities like Microsoft's campus for commuting short distances such as to and from work.",
    "APP Design: Mini Program for Tai Koo Li Shopping Mall": "1. Book a parking space in advance to avoid blindly looking for a parking spot. 2. Personalized recommended parking spot. 3. Warm reminder when necessary.",
    "Product Design: ClimaSphere": "It is an elegant and intuitive weather station that can be hung at the door to remind users to bring an umbrella when they go out.",
    "Interior Design: NDB Headquarters Building Interior Design": "The New Development Bank is a multinational bank headquarter located at Shanghai Expo Park completed in 2022."
}

for title, desc in projects.items():
    st.markdown(f'<div class="project-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="content-text">{desc}</div>', unsafe_allow_html=True)

# Skills
st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
st.markdown("""
<div class="content-text">CAD / PS / Indesign / AI<br>
Rhino / Sketchup /<br>
Figma<br>
Python</div>
""", unsafe_allow_html=True)

# Contact
st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)
st.markdown('<div class="contact-text">monihuangpro@gmail.com</div>', unsafe_allow_html=True)


