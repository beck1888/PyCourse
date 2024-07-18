import streamlit as st

# Define the pages in the site
# Home and other non-content pages
home = st.Page("home.py", title="Home", icon="🏠", url_path="home")

# Content pages
# Unit 0
unit_0_lesson_0 = st.Page("unit_0/lesson_0.py", title="Lesson 0: Hello World!", icon="0️⃣", url_path="lesson_0")

# Build the navigation menu
pg = st.navigation(
    {"App": [home],
    "Unit 0": [unit_0_lesson_0]}
    )

pg.run() # Implement the pages