##
## Created By Wesley Ruede
##


class Calculator:
    def __init__(self):
        self.x = 0
        self.x = 0

    def add(self):
        x = int(input('Enter an integer: '))
        y = int(input('Enter an integer: '))
        return(x + y)

    def subtract(self):
        x = input('Enter an integer: ')
        y = input('Enter an integer: ')
        return(x - y)

    def multiply(self):
        x = input('Enter an integer: ')
        y = input('Enter an integer: ')
        return(x * y)

    def divide(self):
        x = int(input('Enter an integer: '))
        y = int(input('Enter an integer: '))
        return(x / y)

    def modulo(self):
        x = input('Enter an integer: ')
        y = input('Enter an integer: ')
        return(x % y)

    def floor(self):
        x = input('Enter an integer: ')
        y = input('Enter an integer: ')
        return(x // y)
    
calc = Calculator()

def main():
    print(calc.add())

if __name__ == '__main__':
    main()
