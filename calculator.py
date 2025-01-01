def calculator():
    print("Welcome to the Simple Calculator")
    print("=" * 40)
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("=" * 40)
    
    try:
        # Taking user inputs
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Choose an operation from the menu above (1/2/3/4):")
        choice = input("Enter your choice: ")
        2
        # Performing the selected operation
        if choice == "1":
            result = num1 + num2
            operation = "+"
        elif choice == "2":
            result = num1 - num2
            operation = "-"
        elif choice == "3":
            result = num1 * num2
            operation = "*"
        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                operation = "/"
            else:
                print("Error: Division by zero is not allowed!")
                return
        else:
            print("Invalid choice! Please select a valid operation.")
            return
        
        # Displaying the result
        print("=" * 40)
        print(f"Result: {num1} {operation} {num2} = {result}")
        print("=" * 40)
    except ValueError:
        print("Error: Invalid input! Please enter numeric values only.")

# Run the calculator
calculator()
