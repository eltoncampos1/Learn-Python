n1= float(input("first number: "))
operator=input("operator: ")
n2= float(input("second number: "))
if operator == "+":
    print(n1 + n2)
elif operator == "-":
    print(n1 - n2)
elif operator == "/":
    print(n1 / n2)
elif operator == "*":
    print(n1 * n2)
else:
    print("Invalid operator")