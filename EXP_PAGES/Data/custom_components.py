import streamlit as st

import streamlit as st

class NavBar:
    def __init__(self, items):
        self.items = items

    def render(self):
        for item in self.items:
            if st.button(item):
                return item