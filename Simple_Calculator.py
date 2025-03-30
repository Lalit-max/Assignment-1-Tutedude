operand1=float((input("Enter the first number:")))
operand2=float(input("Enter the second number:"))

print("Addition:",operand1+operand2 )

print("Subtraction:",operand1-operand2 )

print("Multiplication:",operand1*operand2 )

if operand2 != 0:
    print(f"Division: {operand1} ÷ {operand2} = {operand1 / operand2}")
else:
    print("Division: Undefined (cannot divide by zero)")

