import streamlit as st
import csv
import plotly.express as px
import pandas as pd
from collections import defaultdict
from datetime import datetime

# Initialize the dictionary to store the expenses
expenses = defaultdict(int)

st.title('Expense Tracker')

# Define the categories
categories = ['Utilities', 'Property maintenance', 'Cleaning supplies', 'Staff salaries and wages', 'Employee benefits', 'Property taxes', 'Insurance', 'Promotional expenses', 'Online presence', 'Toiletries and linens', 'Breakfast or other complimentary services', 'Office supplies', 'Accounting and legal fees', 'Budget for periodic renovations and upgrades', 'Property management system (PMS)', 'Online reservation platforms', 'Set aside a portion for unexpected expenses or emergencies']

# Navigation menu
page = st.sidebar.radio("Go to", ("Entry", "Report"))

if page == "Entry":
    # Get the date from the user
    date = st.date_input("Enter Date")

    # Get the category from the user
    category = st.selectbox("Select Category", options=categories)

    # Get the amount from the user
    amount = st.number_input("Enter Amount", min_value=0.0, step=0.01)

    if st.button('Submit'):
        if category and amount and date:
            expenses[category] += amount
            st.success(f'Successfully added {amount:,.2f} UGX to {category}.')
            try:
                with open('expenses.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([date, category, amount])
            except Exception as e:
                st.error(str(e))
        else:
            st.error('Please enter both category, amount, and date.')

elif page == "Report":
    # Read the data from the CSV file
    try:
        df = pd.read_csv('expenses.csv', parse_dates=[0], names=['Date', 'Category', 'Amount'], header=None, skiprows=1)
    except Exception as e:
        st.error(str(e))
        st.stop()

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Get the selected categories from the user
    selected_categories = st.multiselect("Select Categories", options=categories, default=categories)

    # Filter the DataFrame based on the selected categories
    if selected_categories:
        df_filtered = df[df['Category'].isin(selected_categories)]
    else:
        df_filtered = df

    # Get the start and end dates from the user
    start_date = st.date_input("Start Date", value=df['Date'].min())
    end_date = st.date_input("End Date", value=df['Date'].max())

    # Convert start_date and end_date to datetime
    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)

    # Filter the DataFrame based on the selected dates
    df_filtered = df_filtered[(df_filtered['Date'] >= start_date) & (df_filtered['Date'] <= end_date)]

    # Create a pivot table
    pivot_table = df_filtered.pivot_table(
        values='Amount',
        index='Date',
        columns='Category',
        aggfunc='sum'
    ).fillna(0)

    # Create a line chart with interactive features
    try:
        fig = px.line(
            pivot_table,
            labels={'value': 'Amount', 'variable': 'Category'},
            title='Total Expenses Over Time'
        )
        fig.update_layout(
            xaxis_title='Date',
            yaxis_title='Amount',
            legend_title='Category',
            hovermode='x'
        )
        fig.update_traces(mode='lines+markers')
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(str(e))