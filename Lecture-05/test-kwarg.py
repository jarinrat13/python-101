def display_info(**kwargs): #keyword arguments
    for key, value in kwargs.items():
        print(f'{key}: {value}')

display_info(name="Alice", age=30, city="New York")
