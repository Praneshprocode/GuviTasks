#Find all ways to make Rs. 10 using Rs. 1, Rs. 2, Rs. 5, and Rs. 10 coins
for a in range(11):      # Rs.1 coins
    for b in range(6):   # Rs.2 coins
        for c in range(3):  # Rs.5 coins
            for d in range(2):  # Rs.10 coins
                if a + 2*b + 5*c + 10*d == 10:
                    print(f"Rs1={a}, Rs2={b}, Rs5={c}, Rs10={d}")