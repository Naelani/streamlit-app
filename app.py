import streamlit as st

st.title("🚀 Fast Streamlit App")
name = st.text_input("What's your name?")
if name:
    st.success(f"Hello, {name}!")
