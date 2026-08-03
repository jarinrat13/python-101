# keep_going = 'y'
# while keep_going == 'y':
#     sales = float(input('Enter the amount of sales: '))
#     comm_rate = float(input("enter the commission rate: "))
#     commission = sales * comm_rate
#     print(f'The commission is ${commission:2f}')
#     keep_going = input('Do you want to calculate another' + \
#                        'commission (Enter y for yes): ')
    
keep_going = 'y'
while keep_going == 'y':
    wholesales = float(input("Enter the item's wholesale cost: " ))
    retail_price = float(input("enter the retail price: "))
    retail_price = wholesales * 2.5
    print(f'The retail price is ${retail_price:2f}')
    keep_going = input('Do you want to calculate another' + \
                       'retail price (Enter y for yes): ')

    

