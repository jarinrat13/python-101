inchar = input("Enter a character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("You in put an Upper Case letter." , inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("You in put a Lower Case letter." , inchar)
elif inchar >= '0' and inchar <= '9':
    print("You in put a Number." , inchar)
else:
    print("It's not a letter or a number." , inchar)
