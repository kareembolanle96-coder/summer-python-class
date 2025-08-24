# Function to add an expense (amount + category) into the expenses list
def add_expense(expenses, amount, category):
    # Each expense is stored as a dictionary with 'amount' and 'category' keys
    expenses.append({'amount': amount, 'category': category})
    

# Function to print all expenses from the expenses list
def print_expenses(expenses):
    # Loop through each expense dictionary in the list
    for expense in expenses:
        # Display expense details (amount and category)
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    

# Function to calculate the total of all expenses
def total_expenses(expenses):
    # Extract all 'amount' values from each expense and sum them up
    return sum(map(lambda expense: expense['amount'], expenses))
    

# Function to filter expenses by a given category
def filter_expenses_by_category(expenses, category):
    # Return only those expenses where the 'category' matches the input
    # (filter() returns an iterable, not a list)
    return filter(lambda expense: expense['category'] == category, expenses)
    

# Main function to run the expense tracker program
def main():
    # Start with an empty list to hold expenses
    expenses = []

    # Infinite loop to keep showing the menu until user exits
    while True:
        # Menu options
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        # Get user choice
        choice = input('Enter your choice: ')

        # Option 1: Add new expense
        if choice == '1':
            amount = float(input('Enter amount: '))   # Convert amount to float
            category = input('Enter category: ')      # Get expense category
            add_expense(expenses, amount, category)   # Save expense

        # Option 2: Show all expenses
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        # Option 3: Show total expenses
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        # Option 4: Filter expenses by category
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            # Filtered expenses is an iterable, pass it to print_expenses()
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        # Option 5: Exit program
        elif choice == '5':
            print('Exiting the program.')
            break
