def calculate_average(*numbers):
    return sum(numbers) / len(numbers)
def calculator_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
def modify_list(values):
    """Demonstrates pass by reference
    Modifies original list"""
    values.appemd(100)