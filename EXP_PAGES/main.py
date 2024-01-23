import streamlit as st
import csv
from collections import defaultdict
from datetime import datetime

# Initialize the dictionary to store the expenses
expenses = defaultdict(int)

st.title('Expense Tracker')

# Get the date from the user
date = st.date_input("Enter Date")

# Define the categories
categories = ['Utilities', 'Property maintenance', 'Cleaning supplies', 'Staff salaries and wages', 'Employee benefits', 'Property taxes', 'Insurance', 'Promotional expenses', 'Online presence', 'Toiletries and linens', 'Breakfast or other complimentary services', 'Office supplies', 'Accounting and legal fees', 'Budget for periodic renovations and upgrades', 'Property management system (PMS)', 'Online reservation platforms', 'Set aside a portion for unexpected expenses or emergencies']

# Get the category from the user
category = st.selectbox("Select Category", options=categories)

# Get the amount from the user
amount = st.number_input("Enter Amount", min_value=0.0, step=0.01)

if st.button('Submit'):
    if category and amount and date:
        expenses[category] += amount
        st.success(f'Successfully added {amount:,.2f} UGX to {category}.')
        with open('expenses.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, category, amount])
    else:
        st.error('Please enter both category, amount, and date.')

st.subheader('Total Expenses for Today')
with open('expenses.csv', 'r') as f:
    reader = csv.reader(f)
    total = sum(float(row[2]) for row in reader if row[0] == str(date))
st.write(f'Total: {total:,.2f} UGX')