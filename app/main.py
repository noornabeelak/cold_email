import streamlit as st
st.title("cold email generator")
url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
submit_button = st.button("Submit")

if submit_button:
    st.code("Hello Hiring Manager,I am Noor Nabeela",language='markdown')