#find duplicates in the list
lst_1 = [100, 200, 300, 400, 500]
lst_2 = [300, 400, 500, 600, 700]
lst_3 = [200, 300, 500, 800, 900]

duplicate_find = set(lst_1) & set(lst_2) & set(lst_3)

print("Common elements in the list :", duplicate_find)