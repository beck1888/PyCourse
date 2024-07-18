import streamlit as st
# from streamlit_lottie import st_lottie
# import json

# Setup the page layout
st.set_page_config(page_title="Learn Python", page_icon="assets/favicon.png", layout="centered", initial_sidebar_state="expanded")

# Welcome message
st.title("Learn Python Online")
st.subheader("A free and interactive Python course for beginners")

# Description of Python
st.markdown(
"""**What is Python?** Python is a high-level, general-purpose programming language. It was created by Guido van Rossum and first released in 1991.

**What is Python used for?** Python is used in web development, data science, artificial intelligence, and many other fields.

**Is Python easy to learn?** Yes, Python is easy to learn. It is simple, easy to read, and easy to use.

**Why takes this course?** This course is designed to help beginners learn Python. It breaks down Python into small and easy lessons where you get to write and test your code!

**Why is this course free?** I want to showcase my Python skills by helping others learn Python.

**Why does everything start with 0 instead of 1?** In computer science, we use something called *zero indexing* which means we start counting at 0. For example, the first item in a list is at index 0. This course uses this principal for course numbering to help you adapt to this change."""
)

# Get started prompt
# # Load Lottie animation
# with open("assets/lottie_left.json", "r") as f:
#     lottie_l = json.load(f)

# # Display Lottie animation
# st_lottie(
#     lottie_l,
#     speed=0.6,
#     reverse=False,
#     loop=True,
#     quality="high",
#     height=70,
#     width=400,
#     key=None,
# )

if st.button("Get Started", key="home", type="primary", use_container_width=True):
    st.switch_page("unit_0/lesson_0.py")