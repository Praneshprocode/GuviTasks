#Prime number in the list
lst = [10, 501, 22, 37, 100, 999, 87, 351]
primenumber = []
for j in lst:
    if j > 1:
        for k in range(2, j):
            if j % k == 0:
                break
        else:
            primenumber.append(j)
print("Prime numbers are :", primenumber)
print("Count of prime numbers :", len(primenumber))