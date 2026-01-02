# Helper functions
def square(num):
    return num ** 2

def cube(num):
    return num ** 3


# Higher-order function
def transform_list(nums_list, transform_item):
    transformed_0 = transform_item(nums_list[0])
    transformed_1 = transform_item(nums_list[1])
    return [transformed_0, transformed_1]


# Using a helper function
print(transform_list([2, 3], cube))

# Using a lambda function
print(transform_list([2, 3], lambda x: x ** 2))


"""
Key idea demonstrated by this program:

What stays the same:
- The function `transform_list`
- The overall structure of the program
- The flow: take data, apply a transformation, return results

What changes:
- The behavior passed into `transform_list`
- The `transform_item` function (cube, square, or a lambda)

This shows how higher-order functions separate structure from behavior.
The structure remains fixed, while behavior can be swapped freely.
"""
