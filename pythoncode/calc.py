class Calculator:

    def add(self, a, b):
        return a + b

    def div(self, a, b):
        if b == 0:
            return "divider cannot be 0"
        else:
            return a / b

    def multi(self, a, b):
        return a * b

    def sub(self, a, b):
        return a - b
