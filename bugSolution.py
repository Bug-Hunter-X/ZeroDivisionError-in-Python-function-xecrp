def function(a, b):
    if b == 0:
        return "Division by zero"
    else:
        return a / b

result = function(10, 0)
print(result)  # Output: Division by zero

#Alternative solution using exception handling
def function(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Division by zero"
result = function(10,0)
print(result) # Output: Division by zero