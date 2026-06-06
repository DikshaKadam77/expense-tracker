import csv
from datetime import datetime

#  Add Expense function

def add_expense():
    amount = input("Enter amount spend: ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    
    
    date = datetime.now().strftime("%Y-%m-%d")
    
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
        
        print("Expense added successfully!")
        
# View Expenses function

def view_expenses():
    try:
        with open('expenses.csv', "r") as file:
            reader = csv.reader(file)
            
            print("\nALL EXPENSES:")
            
            for row in reader:
                print(f"Date: {row[0]}")
                print(f"Amount: {row[1]}")
                print(f"Category: {row[2]}")
                print(f"Description: {row[3]}")
                print("-" * 30)
                
    except FileNotFoundError:
        print("No expenses found.")
        
# Total spending function

def total_spending():
    total = 0
    
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            
            for row in reader:
                total += float(row[1])
                
        print(f"Total Spending: {total}")
        
    except FileNotFoundError:
        print("No expenses found.")
        
#  Category summary function

def category_summary():
    categories = {}
    
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            
            for row in reader:
                category = row[2]
                amount = float(row[1])
                
                if category in categories:
                    categories[category] += amount
                else:
                    categories[category] = amount
                    
        print("\nCATEGORY SUMMARY:")
        
        for category, total in categories.items():
            print(f"{category}: {total}")
    
    except FileNotFoundError:
        print("No expenses found.")
    
#  Exit function

def exit_program():
    print("Thank you for using the Expense Tracker.")
    
# Menu

while True:
    print("EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Category Summary")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        add_expense()
        
    elif choice == '2':
        view_expenses()
        
    elif choice == '3':
        total_spending()
        
    elif choice == '4':
        category_summary()
    elif choice == '5':
        exit_program()
        break
    else:
        print("Invalid Choice")
        
