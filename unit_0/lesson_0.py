import streamlit as st
from run_code import run_python_code
from streamlit_lottie import st_lottie
import time
import json

# Setup the page layout
st.set_page_config(page_title="Python | Unit 0 - Lesson 0", page_icon="assets/favicon.png", layout="wide", initial_sidebar_state="expanded")

if "code" not in st.session_state:
    st.session_state["code"] = ""

if "output" not in st.session_state:
    st.session_state["output"] = []

st.title("Unit 0 - Lesson 0: Hello, World!")
st.markdown("🕘 **Time:** 2 minutes")

st.container(height=10, border=False) # Vertical spacer

st.subheader("Lesson")

st.markdown("""First, let's learn about the `print` statement. The `print` statement is used to output text to the screen. For example, `print("Hello, World!")` will output the text "Hello, World!" to the screen. 
            
This program is a common way developers test that their programs are running as expected. Go ahead and try it out!""")

st.container(height=10, border=False) # Vertical spacer
st.subheader("Task")

col1, col2 = st.columns(2)

def run_code():
    code = st.session_state["code"]
    output_container = st.session_state["output_container"]
    output_container.empty()  # Clear previous output
    
    with output_container:
        with st.spinner("Running code..."):
            output = run_python_code(code)
            time.sleep(2)  # Simulate delay for code execution

    if output["errors"]:
        st.session_state["output"] = [f"`{output['output']}`", f"You got a **syntax error** meaning the computer couldn't understand your code. Check the console to see what the error is."]
    else:
        if "hello" in output["output"].lower() and "world" in output["output"].lower():
            st.balloons()
            st.session_state["output"] = [f"`{output['output']}`", "Your code is **correct** because it ran without any errors and gave you the expected output. Good job!"]
        else:
            st.session_state["output"] = [f"`{output['output']}`", "You have a **semantic error** meaning the computer ran your code, but the output didn't match what you expected. Check the console."]


with col1:
    st.write("Write your code here:")
    code = st.text_area("Type your code here...", height=285, label_visibility="collapsed", value=st.session_state["code"], key="code")
    run = st.button("Run", use_container_width=True, on_click=run_code)

with col2:
    st.write("Console:")

    with st.container(height=200, border=True):
        st.session_state["output_container"] = st.empty()  # Placeholder for output

        try:
                st.markdown(st.session_state["output"][0])
        except:
            pass

    st.write("Explanation of the console's output:")
    with st.container(height=85, border=True):
        try:       
            st.markdown(st.session_state["output"][1])
        except:
            pass