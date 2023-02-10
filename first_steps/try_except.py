try:
    value = 10/ 0
    num = int(input("Enter a number:"))
    print(num)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")