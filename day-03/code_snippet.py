num_list = [2, 3, 4, 5, 6]

# Using map() with a lambda function
print(list(map(lambda x: x ** 3, num_list)))

# Using filter() with a lambda function
print(list(filter(lambda x: x % 2 == 0, num_list)))


"""
Key idea demonstrated:

map():
- Keeps the structure of the data the same
- Changes every value by applying a function

filter():
- Keeps the values unchanged
- Changes the structure by selecting elements based on a condition

In both cases, lambda functions are used to provide short, one-time behavior
directly at the point where it is needed.
"""
