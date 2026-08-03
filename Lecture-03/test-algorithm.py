test1 = int(input("Input your score for test 1: "))
test2 = int(input("Input your score for test 2: "))
test3 = int(input("Input your score for test 3: "))
average = (test1 + test2 + test3) / 3
print("Your average score is: ", average)

if average > 95:
    print("Congratulations!")
    print("That's a great average!")