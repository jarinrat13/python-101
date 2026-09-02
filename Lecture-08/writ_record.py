import struct
num_records = int(input('How many records do you want to create? '))
with open("records.bin", "wb") as file:
    for _ in range(num_records):
        id = int(input('Enter ID: '))
        name = input('Enter name: ').ljust(20)[:20]
        age = int(input('Enter age: '))
        gpa = float(input('Enter GPA: '))
        data = struct.pack('i20sif', id, name.encode(), age, gpa)
        file.write(data)
        
print(f'{num_records} records have been written to records.bin')