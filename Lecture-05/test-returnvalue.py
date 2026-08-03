def calculate_stats(numbers):
    total_sum = sum(numbers) #function sum
    average = total_sum / len(numbers) #len function to get the length of the list
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum , average , maximum , minimum #step by step

numbers = [5 , 10 , 15 , 20 , 25] #list
total , avg , max_num , min_mum = calculate_stats(numbers) #same step by step

print(f"Total Sum: {total}")
print(f"Average: {avg}")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_mum}")