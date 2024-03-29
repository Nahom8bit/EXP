from datetime import datetime
import csv
import json
import plotly.express as px
import pandas as pd
import streamlit as st
from collections import defaultdict

class ExpenseTracker:
    def __init__(self):
        self.expenses = defaultdict(int)

    def add_expense(self, category, amount, date, comment):
        self.expenses[category] += amount
        try:
            with open('expenses.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([date, category, amount, comment])
        except Exception as e:
            st.error(str(e))

tracker = ExpenseTracker()

st.title('EXP APP')

page = st.sidebar.radio("Go to", ("📝 Entry", "📊 Report", "🔍 Review", "👤 Account"))

# Load the categories from the JSON file
with open('categories.json') as f:
    categories = json.load(f)

# Flatten the categories into a list
flat_categories = []
for category, subcategories in categories['Transactions']['Expenses'].items():
    flat_categories.append(category)

def entry():
    date = st.date_input("Enter Date")
    category = st.selectbox("Select Category", options=flat_categories)
    subcategory = st.selectbox("Select Subcategory", options=categories['Transactions']['Expenses'][category]) if category else None
    amount = st.number_input("Enter Amount", min_value=0.0, step=0.01)
    comment = st.text_input("Comment")

    if st.button('Submit'):
        if category and amount and date and subcategory:
            tracker.add_expense(f"{category}/{subcategory}", amount, date, comment)
            st.success(f'Successfully added {amount:,.2f} UGX to {category}/{subcategory}.')
        else:
            st.error('Please enter all required fields.')

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('expenses.csv', parse_dates=[0], skiprows=1, error_bad_lines=False)
        df.columns = ['Date', 'Category', 'Amount', 'Comment', 'Time']
        return df
    except Exception as e:
        st.error(f'An error occurred while loading the data: {str(e)}. Please check the CSV file.')
        return None

def report():
    if st.button('Refresh Data'):
        df = load_data()
    else:
        df = load_data()

    if df is None:
        return

    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    selected_categories = st.multiselect("Select Categories", options=flat_categories, default=flat_categories)

    if selected_categories:
        df_filtered = df[df['Category'].isin(selected_categories)]
    else:
        df_filtered = df

    start_date = st.date_input("Start Date", value=df['Date'].min())
    end_date = st.date_input("End Date", value=df['Date'].max())

    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)

    df_filtered = df_filtered[(df_filtered['Date'] >= start_date) & (df_filtered['Date'] <= end_date)]

    pivot_table = df_filtered.pivot_table(
        values='Amount',
        index='Date',
        columns='Category',
        aggfunc='sum'
    ).fillna(0)

    chart_type = st.selectbox("Select Chart Type", options=["Line", "Bar"])

    if chart_type == "Line":
        fig = px.line(
            pivot_table,
            labels={'value': 'Amount', 'variable': 'Category'},
            title='Total Expenses Over Time'
        )
        fig.update_traces(mode='lines+markers')
    elif chart_type == "Bar":
        fig = px.bar(
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
    st.plotly_chart(fig, use_container_width=True)

    st.write(df_filtered)

def review():
    if st.button('Refresh Data'):
        df = load_data()
    else:
        df = load_data()

    if df is None:
        return

    st.write(df)

# Define a new function called `account()`
def account():
    st.title('Account Page')
    st.write('This is the Account Page.')

# Call the `account()` function when the "Account Page" option is selected
if page == "📝 Entry":
    entry()
elif page == "📊 Report":
    report()
elif page == "🔍 Review":
    review()
elif page == "👤 Account":
    account()