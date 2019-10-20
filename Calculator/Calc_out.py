##
## Created By Wesley 10/14/19
## A signifigantly improved and refactored Calculator


class Calculator:
    def __init__(self):
        pass

    def _ask_user(self):
        try:
            x = float(input('Enter a value: '))
            y = float(input('Enter a value: '))
        except ValueError:
            print('please enter an integer or float value')
        return x, y

    def add(self):
        x, y = self._ask_user()
        return x + y

    def subtract(self):
        x, y = self._ask_user()
        return x - y

    def multiply(self):
        x, y = self._ask_user()
        return x * y

    def divide(self):
        x, y = self._ask_user()
        if y == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return x / y

    def modulo(self):
        x, y = self._ask_user()
        if y == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return x % y

    def int_div(self):
        x, y = self._ask_user()
        if y == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return x // y
    
calc = Calculator()

def main():
    print("""Welcome to Wes's claculator. 
    1) for addition
    2) for subtraction
    3) for multiplication
    4) for division
    5) for modulo division
    6) for floor division
    Please choose your method of calculation \n
    Enter 0 if you would like to close the program""")
    
    
    while True:
        try:
            user_input = int(input('Please enter a number for your selection: '))    
            if user_input == 1:
                print(calc.add())
            elif user_input == 2:
                print(calc.subtract())
            elif user_input == 3:
                print(calc.multiply())
            elif user_input == 4:
                print(calc.divide())
            elif user_input == 5:
                print(calc.modulo())
            elif user_input == 6:
                print(calc.int_div())
            elif user_input == 0:
                exit()
            else:
                print('\nYou must choose one through six or 0 to close the app')
        except ValueError:
            print('\nYou must enter one through six or 0 to close the app')
        
if __name__ == '__main__':
        main()
