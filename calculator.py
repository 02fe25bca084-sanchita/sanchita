a = int (input("Enter first number:"))
b = int (input("Enter second number:"))

addition = a + b
subtraction = a - b

print("Addition =", addition)
print("Subtraction =", subtraction)

multiplication = a * b
print("Multiplication =", multiplication)

if b != 0:
    division = a / b
    print("Division =", division)
else:
    print("Division is not possible by zero.")