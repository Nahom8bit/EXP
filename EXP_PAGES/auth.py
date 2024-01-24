# auth.py
import streamlit as st
import config

username = st.text_input('Username')
password = st.text_input('Password', type='password')

if st.button('Login'):
    if username == config.username and password == config.password:
        st.success('Logged in successfully!')
        # Here you can use os.system or subprocess.run to run the main.py script
        # os.system('streamlit run main.py')
    else:
        st.error('Invalid credentials')