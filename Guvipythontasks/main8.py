#First non repeating element in the list

num_lst = [440, 575, 1000, 200, 1000, 200, 440]

for o in num_lst:
    if num_lst.count(o) == 1:
        print("First non-repeating element:", o)
        break