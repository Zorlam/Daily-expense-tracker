print("Welcome to the Daily Expense Tracker!")

# Display menu once
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

# Initialize an empty list to store expenses
expenses = []

while True:
    # Get user choice
    choice = input()
    
    if choice == "1":
        # Add a new expense
        amount = float(input())
        expenses.append(amount)
        print("Expense added successfully!")

    elif choice == "2":
        # View all expenses
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]}")

    #Accumulator variable
    elif choice == "3":
        number = 0
        if len(expenses) == 0:
            print("You have no expenses")
        else:
            for item in expenses:
             number += item
    #Calculating average expense
            average = number / len(expenses)
            print(f'Total expense: {number}')
            print(f'Average expense: {average}')

    elif choice == "4":
        expenses.clear()
        print("All expenses cleared.")

    elif choice == "5":
        # Exit the program
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice, Please try again")