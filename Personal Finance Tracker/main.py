import pandas as pd
import csv
import os
from datetime import datetime
from data_entry import get_amount, get_date, get_category, get_description  
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = 'Finance_data.csv'
    COLUMNS = ['date', 'amount', 'category', 'description']
    FORMAT = "%d-%m-%Y"
    
    @classmethod
    def initialize_csv(cls):
        """Create CSV file with headers if it doesn't exist."""
        if not os.path.exists(cls.CSV_FILE):
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_data(cls, date, amount, description, category):
        """Add a new transaction row to the CSV file."""
        new_row = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }

        file_exists = os.path.isfile(cls.CSV_FILE)
        write_header = not file_exists or os.stat(cls.CSV_FILE).st_size == 0

        with open(cls.CSV_FILE, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=cls.COLUMNS)
            if write_header:
                writer.writeheader()  # Ensure headers are written
            writer.writerow(new_row)

        print(f"✅ Data entry added successfully: {new_row}")
        
    @classmethod
    def get_transactions(cls, start_date, end_date):
        """Display transactions and summary within a date range."""
        df = pd.read_csv(cls.CSV_FILE)

        if 'date' not in df.columns:
            print("❌ Error: 'date' column not found in the CSV file.")
            print("📄 Current columns:", df.columns.tolist())
            return

        df['date'] = pd.to_datetime(df['date'], format=cls.FORMAT)
        start_date = datetime.strptime(start_date, cls.FORMAT)
        end_date = datetime.strptime(end_date, cls.FORMAT)

        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print('⚠️ No transactions found in the given date range.')
        else:
            print(f'📅 Transactions from {start_date.strftime(cls.FORMAT)} to {end_date.strftime(cls.FORMAT)}:')
            print(filtered_df.to_string(
                index=False, 
                formatters={'date': lambda x: x.strftime(cls.FORMAT)}
            ))

            total_income = filtered_df[filtered_df['category'] == 'Income']['amount'].sum()
            total_expenses = filtered_df[filtered_df['category'] == 'Expense']['amount'].sum()

            print('\n📊 Summary:')
            print(f"Total Income: {total_income:.2f}")
            print(f"Total Expenses: {total_expenses:.2f}")
            print(f"Net Balance: {total_income - total_expenses:.2f}")


def add():
    """Helper function to add a transaction using user input."""
    CSV.initialize_csv()
    date = get_date('Enter the date of transaction (dd-mm-yyyy) or press Enter for today: ')
    amount = get_amount()
    description = get_description()
    category = get_category()
    CSV.add_data(date, amount, description, category)
    
def plot_transactions():
    """Plot the income and expense data over time."""
    df = pd.read_csv(CSV.CSV_FILE)

    if 'date' not in df.columns:
        print("❌ Error: 'date' column not found in the CSV file.")
        return

    df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT)

    income_df = df[df['category'] == 'Income']
    expense_df = df[df['category'] == 'Expense']

    plt.figure(figsize=(10, 5))
    plt.plot(income_df['date'], income_df['amount'], marker='o', label='Income', color='green')
    plt.plot(expense_df['date'], expense_df['amount'], marker='o', label='Expenses', color='red')

    plt.title('Income and Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
    
def main():
    """Main menu loop for the finance management tool."""
    CSV.initialize_csv()
    while True:
        print('\n📘 --- Personal Finance Manager ---')
        print('1. Add a new transaction')
        print('2. View transactions & summary within a date range')
        print('3. Plot transactions')
        print('4. Exit')
        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            add()
        elif choice == '2':
            start_date = input('Enter start date (dd-mm-yyyy): ')
            end_date = input('Enter end date (dd-mm-yyyy): ')
            CSV.get_transactions(start_date, end_date)
        elif choice == '3':
            plot_transactions()
        elif choice == '4':
            print('👋 Exiting the program.')
            break
        else:
            print('❗ Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
