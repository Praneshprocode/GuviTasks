#Happycounts

lst = [10, 501, 22, 37, 100, 999, 87, 351]
happy = []
for k in lst:
    number = k
    while number != 1 and number != 4:
        total = 0
        for digit in str(number):
            total += int(digit) * int(digit)
        number = total
    if number == 1:
        happy.append(k)
print("Happy numbers are :", happy)
print("Count of the happy numbers:", len(happy))