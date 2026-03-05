# Personal-Finance-Tracker

A lightweight Python command-line interface (CLI) application to track daily income and expenses. This tool leverages the pandas library for data manipulation and ensures your financial records are persisted in a local CSV file.

## Features
Persistent Storage: Automatically creates and updates finance.csv. Your data stays saved even after the program closes.
Transaction Logging: Simple prompts to record income and categorize expenses.
Instant Summaries: View your total income, total expenses, and net balance at any time.
Error Handling: Gracefully handles missing files by initializing a new database structure on the fly.

## Getting Started
### Prerequisites
You will need Python 3.x and the pandas library installed.

Bash
pip install pandas
### Running the Application
Open your terminal or command prompt.

Navigate to the folder containing the file and run:

Bash
python main.py

## How to Use
When the program starts, you will be presented with a menu:
Add Income: Enter the amount received. (Default category: salary).
Add Expense: Enter a custom category (e.g., "Rent", "Groceries") and the amount spent.
Show Summary: Displays a breakdown of your current financial standing.

Exit: Important! Always use this option to close the program, as it triggers the final save to finance.csv.