print("KPH\tMPH")
for kph in range(60, 140, 10):
    mph = kph * 0.6214
    print(kph, '\t', mph)
    

print("mph\tkm")
for mph in range(40,140,10):
    km = mph / 0.69
    print(mph, '\t', km)