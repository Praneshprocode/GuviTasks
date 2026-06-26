#Even and ODD numbers
nums = [10, 501, 22, 37, 100, 999, 87, 351]
evennums = []
oddnums = []
for i in nums:
    if i % 2 == 0:
        evennums.append(i)
    else:
        oddnums.append(i)
print("Even numbers are :", evennums)
print("Odd numbers are :", oddnums)
