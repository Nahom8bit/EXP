import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from pandasgui import show

class ExpenseTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Expense Tracker App")
        self.geometry("800x600")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.entry_page = EntryPage(self.notebook)
        self.report_page = ReportPage(self.notebook)
        self.review_page = ReviewPage(self.notebook)
        self.account_page = AccountPage(self.notebook)

        self.notebook.add(self.entry_page, text="Entry")
        self.notebook.add(self.report_page, text="Report")
        self.notebook.add(self.review_page, text="Review")
        self.notebook.add(self.account_page, text="Account")

class EntryPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # TODO: Add form fields and submit button

class ReportPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # TODO: Add controls for selecting categories and date range
        # TODO: Display line chart of total expenses over time

class ReviewPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # TODO: Display table of all recorded expenses

class AccountPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # TODO: Display user account information

if __name__ == "__main__":
    app = ExpenseTrackerApp()
    app.mainloop()