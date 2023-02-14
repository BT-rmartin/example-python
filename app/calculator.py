class Calculator:

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        # Adding comment1
        if y == 0:
            # Adding comment2
            return 'Cannot divide by 0'
        return x * 1.0 / y
