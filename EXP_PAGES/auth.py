# auth.py
import streamlit as st
import config
import os

username = st.text_input('Username')
password = st.text_input('Password', type='password')

if st.button('Login'):
    if username == config.username and password == config.password:
        st.success('Logged in successfully!')
        # Run the main.py script
        os.system('streamlit run main.py')
    else:
        st.error('Invalid credentials')