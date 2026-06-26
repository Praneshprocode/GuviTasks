#List comprehension for squares of even numbers
numbers_lst = [100, 200, 300, 400, 500, 600, 700, 800]
even = lambda x: x % 2 == 0
square_num = [x ** 2 for x in numbers_lst if even(x)]
print(square_num)
