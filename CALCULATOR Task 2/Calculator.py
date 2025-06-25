# Simple Calculator

# Prompting the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompting the user to choose an operation
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input("Enter your choice (1/2/3/4): ")

# Performing calculation based on user choice
if choice == '1':
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif choice == '2':
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif choice == '3':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice! Please select a valid operation.")
