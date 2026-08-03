def is_armstrong(num):
    str_num = str(num)
    power = len(str_num)
    result = 0
    for i in str_num:
        result += int(i) ** power
    return result == num
        
        
    
num = [153 , 9474 , 123]
total = str(num)
print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))