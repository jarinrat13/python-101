hours_worked = int(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the pay rate: "))
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = 40 * pay_rate
    total_pay = regular_pay + overtime_pay
elif hours_worked <= 40:
    total_pay = hours_worked * pay_rate
print("The gross pay is: $", total_pay)
