from functools import reduce 

# Lambda Functions
square = lambda x: x* x 
cube = lambda x: x*x*x

def square_list(numbers):
    return list(map(lambda x: x*x,numbers))
def even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0,numbers))
def sum_all(numbers):
    return reduce(lambda a, b: a + b, numbers)
