def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on the operation provided.
    
    :param num1: float - first number
    :param num2: float - second number
    :param operation: str - 'add', 'subtract', 'multiply', or 'divide'
    :return: result of the operation or an error message for invalid cases
    """

    if operation == 'add':
        return num1 + num2

    elif operation == 'subtract':
        return num1 - num2

    elif operation == 'multiply':
        return num1 * num2

    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2

    else:
        return "Error: Invalid operation"
