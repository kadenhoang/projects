from datetime import datetime

def date_format(due_date):
    while True:
        try:
            # Validate the date format
            valid_date = datetime.strptime(due_date, "%Y-%m-%d")
            return valid_date  # returns datetime object
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            # Ask the user again for input
            due_date = input("Enter due date (YYYY-MM-DD): ")