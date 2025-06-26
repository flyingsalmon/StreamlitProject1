import streamlit as st

# To run a streamlit python script at command prompt (from where the py script file is located): streamlit run <scriptfile>.py
# --- this will open the python output in a browser locally. e.g. http://localhost:8501/
# It cannot be run from Thonny or Python IDE.
#
# Streamlit documentation: https://docs.streamlit.io/
# APIs and examples: https://docs.streamlit.io/develop/api-reference
# Tutorial: https://www.youtube.com/watch?v=D0D4Pa22iG0

st.title("My Streamlit Webapp")
name = st.text_input("Enter your name:")
#user_prompt = st.text_area("Enter a question:")
submit = st.button("Submit")

# 
if submit:
    with st.spinner("Processing..."): # this will only show if the process takes some time
        st.write(f"Hello {name}!")
        

