numbers = [4, 2, 9, 1, 5, 6]

lenght = len(numbers)
print(f"Length of the lit: {lenght}")

total_sum = sum(numbers)
print(f"Sum of all elements: {total_sum}")

max_value = max(numbers)
print(f"Maximum value: {max_value}")

min_value =min(numbers)
print(f"Minimum value: {min_value}")

sorted_numbers = sorted(numbers)
print(f"Sotred list: {sorted_numbers}")

bool_list = [False, True, False]
any_true = any(bool_list)
print(f"Is any element True? {bool_list}")

all_true = all(bool_list)
print(f"Are all element True {all_true}")

string = 'hello'
char_list = list(string)
print(f"List  of characters : {char_list}")

reversed_numbers = list(reversed(numbers))
print(f"Reversed list : {reversed_numbers}")

enumerate_numbers = list(enumerate(numbers))
print(f"Enumerate list : {enumerate_numbers}")