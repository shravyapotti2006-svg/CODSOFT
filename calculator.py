# Simple Calculator

# Step 1: Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Show operation choices
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Step 3: Get user's choice
choice = input("Enter 1, 2, 3, or 4: ")

# Step 4: Perform calculation
if choice == '1':
    result = num1 + num2
    operation = '+'
elif choice == '2':
    result = num1 - num2
    operation = '-'
elif choice == '3':
    result = num1 * num2
    operation = '*'
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        operation = '/'
    else:
        print("Error: Cannot divide by zero.")
        exit()
else:
    print("Invalid choice.")
    exit()

# Step 5: Display result
print(f"{num1} {operation} {num2} = {result}")
