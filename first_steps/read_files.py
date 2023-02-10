file = open("emp.txt", "r")
for employee in file.readlines():
    print(employee)
file.close()