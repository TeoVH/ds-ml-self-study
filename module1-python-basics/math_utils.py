# Mathmodule for basic arithmetic operations

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as exc:
        raise ValueError("Cannot divide by zero.") from exc

