def function_with_uncommon_error_solution(a, b):
    try:
        if a == 0:
            return 0 # handles division by zero by returning a default value
        else:
            return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
        #Or you could raise a custom exception 
        #raise Exception("Division by zero is not allowed!")