#Lambda function to check if a string is a number
is_number = lambda s: s.isdigit()
print(is_number("1230"))
print(is_number("67.3"))
print(is_number("abnhc"))