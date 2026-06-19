# Simple Calculator

# Take input from user
n = float(input("Enter first number: "))
m = float(input("Enter second number: "))

# Choose operation
print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5.Modulus")

choice = input("Enter choice (1/2/3/4/5: ")

# Perform calculation
if choice == '1':
    print("Result:", n + m)

elif choice == '2':
    print("Result:", n - m)

elif choice == '3':
    print("Result:", n * m)

elif choice == '4':
    if m != 0:
        print("Result:", n / m)
    else:
        print("Error: Division by zero!")

elif choice=='5':
    print("Result:",n%m)
    
else:
    print("Invalid choice ❌")