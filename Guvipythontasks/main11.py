#sub-list with sum equal to Zero
num_lst = [4, 2, -3, 1, 6]
find = False
for i in range(len(num_lst)):
    total = 0
    for j in range(i, len(num_lst)):
        total += num_lst[j]
        if total == 0:
            found = True
if find:
    print("Sub-list with sum 0 exists")
else:
    print("No sub-list with sum 0")