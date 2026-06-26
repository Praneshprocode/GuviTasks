# First and last digit of number:

findnumber = int(input("Enter a number: "))

last_digit = findnumber % 10
first_digit = int(str(findnumber)[0])

print("Sum =", first_digit + last_digit)