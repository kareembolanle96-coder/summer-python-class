# Expense Tracker

This is a simple **command-line Expense Tracker** built with Python.  
It allows users to add expenses, view them, calculate totals, and filter by category.

## Features
- Add a new expense with an **amount** and **category**.
- List all recorded expenses.
- Calculate and display the **total expenses**.
- Filter expenses by a chosen category.
- Exit option to quit the program.

## How It Works
1. Run the script in your terminal.
2. You will see a menu with options to:
   - Add an expense
   - View all expenses
   - Show total expenses
   - Filter expenses by category
   - Exit the program

### Example Usage
```
Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit
```

If you choose `1`, you’ll be prompted to enter:
```
Enter amount: 45.5
Enter category: Food
```

If you choose `2`, it might display:
```
All Expenses:
Amount: 45.5, Category: Food
```

If you choose `3`, it will calculate:
```
Total Expenses: 45.5
```

If you choose `4`, you can filter expenses by category:
```
Enter category to filter: Food

Expenses for Food:
Amount: 45.5, Category: Food
```

## Requirements
- Python 3.x

No external libraries are required.

## Running the Program
1. Save the code into a file called `expense_tracker.py`.
2. Open a terminal in the same directory.
3. Run:
   ```bash
   python expense_tracker.py
   ```

Enjoy tracking your expenses! 🎉
