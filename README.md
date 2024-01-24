# Expense Tracker App

This is a simple expense tracking application built with Streamlit. It allows users to record their expenses, generate reports, and review their spending habits.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- Streamlit
- Pandas
- Plotly Express

You can install these dependencies using pip:
bash pip install streamlit pandas plotly


### Installing

Clone the repository:

```
git clone https://github.com/NahomDaniel/EXP.git cd EXP
```

## Usage

Run the Streamlit app:

```
streamlit run main.py
```

This will start the app and open it in your default web browser.

### Navigation

The app provides three main pages:

- **Entry**: Allows you to record a new expense. Select a date, choose a category and subcategory, enter the amount, and optionally add a comment. Click "Submit" to save the expense.

- **Report**: Generates a line chart showing total expenses over time. You can select one or more categories to include in the report, and specify a date range.

- **Review**: Displays a table of all recorded expenses.

## Built With

- [Streamlit](https://streamlit.io/) - The web framework used
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- [Plotly Express](https://plotly.com/python/plotly-express/) - Data visualization

## Authors

- Nahom Daniel - Initial work

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details