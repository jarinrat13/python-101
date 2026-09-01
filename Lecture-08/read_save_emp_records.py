with open('employee.txt', 'r') as file:
    for line in file:
        name, age, department = line.strip().split(',')
        print(f'Name: {name}, Age: {age}, Department: {department}')
        