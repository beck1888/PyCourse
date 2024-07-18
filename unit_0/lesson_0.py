import streamlit as st
from run_code import run_python_code
import time

# Setup the page layout
st.set_page_config(page_title="Python | Unit 0 - Lesson 0", page_icon="assets/favicon.png", layout="wide", initial_sidebar_state="expanded")

if "code" not in st.session_state:
    st.session_state["code"] = ""

if "output" not in st.session_state:
    st.session_state["output"] = []

st.title("Unit 0: Introduction to Python")
st.subheader("Lesson 0: \"Hello, World!\"")

st.markdown("""First, let's learn about the `print` statement. The `print` statement is used to output text to the screen. For example, `print("Hello, World!")` will output the text "Hello, World!" to the screen. 
            
This program is a common way developers test that their programs are running as expected. Go ahead and try it out!""")

st.divider()

col1, col2 = st.columns(2)

def run_code():
    code = st.session_state["code"]
    # print("!!! " + code)
    output = run_python_code(code)

    # print(output)
    
    if output["errors"]:
        st.session_state["output"] = [f"`{output['output']}`", f"❌ **SYNTAX ERROR:** Your code has failed to run. Try again."]
    else:
        if "hello" in output["output"].lower() and "world" in output["output"].lower():
            st.balloons()
            st.session_state["output"] = [f"`{output['output']}`", "✅ **Success!** Your code is correct!"]
        else:
            st.session_state["output"] = [f"`{output['output']}`", "⚠️ **SEMANTIC ERROR:** Your code ran successfully, but didn't give the correct output. Try again."]

with col1:
    st.write("Code:")
    code = st.text_area("Type your code here...", height=300, label_visibility="collapsed", value=st.session_state["code"], key="code")
    run = st.button("Run", use_container_width=True, on_click=run_code)

with col2:
    st.write("Output:")
    with st.container(border=True, height=300):
        if "output" in st.session_state:
            i = 0
            for line in st.session_state["output"]:
                i += 1
                if i % 2 == 0:
                    st.divider()
                st.markdown(line)
