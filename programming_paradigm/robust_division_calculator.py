def safe_divide(numerator, denominator):
    """
    Performs division with robust error handling.
    
    Parameters:
        numerator (str or float): The numerator value.
        denominator (str or float): The denominator value.
    
    Returns:
        str: Result or appropriate error message.
    """
    try:
        # Convert to float
        num = float(numerator)
        den = float(denominator)
        # Division
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
