import streamlit as st
from collections import defaultdict

# Initialize the dictionary to store the expenses
expenses = defaultdict(int)

st.title('Expense Tracker')

# Define the categories
categories = ['Utilities', 'Property maintenance', 'Cleaning supplies', 'Staff salaries and wages', 'Employee benefits', 'Property taxes', 'Insurance', 'Promotional expenses', 'Online presence', 'Toiletries and linens', 'Breakfast or other complimentary services', 'Office supplies', 'Accounting and legal fees', 'Budget for periodic renovations and upgrades', 'Property management system (PMS)', 'Online reservation platforms', 'Set aside a portion for unexpected expenses or emergencies']

# Get the category from the user
category = st.selectbox("Select Category", options=categories)

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