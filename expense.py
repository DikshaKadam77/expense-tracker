import csv
from datetime import datetime

# Menu

while True:
    print("EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        print("Add Expense")
        
    elif choice == '2':
        print("View Expenses")
        
    elif choice == '3':
        print("Total Spending")
        
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
        
        