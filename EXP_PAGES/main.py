import streamlit as st
from collections import defaultdict

# Initialize the dictionary to store the expenses
expenses = defaultdict(int)

st.title('Expense Tracker')

# Get the category from the user
category = st.text_input("Enter Category")

# Get the amount from the user
amount = st.number_input("Enter Amount", min_value=0.0, step=0.01)

if st.button('Submit'):
    if category and amount:
        expenses[category] += amount
        st.success(f'Successfully added {amount} to {category}.')
    else:
        st.error('Please enter both category and amount.')

st.subheader('Total Expenses')
for category, total in expenses.items():
    st.write(f'{category}: ${total:.2f}')