##
## Created By Wesley Ruede 10/20/19
## An attempt at creating a calculator that only uses addition no matter
## the math function with a Clear button and an attempt at creating
## state between each math e.g 5 + 5 = 10, 10 + 5 = 15, C (clear) = 0.


import functools

class Calculator:
    def __init__(self, current=0):
        self.current = current
        self.last_x = None
        self.last_operation = None
        self.last_y = None
                
        
    def interpret(self, string):
        """Interprets a user input string and performs an operation."""
        
        inputs = string.strip().split(" ")
        
        # repeat last command if possible
        if not inputs:
            if self.last_operation and self.last_y:
                result = self.last_operation(self.current, self.last_y)
                self.current = result
        
        # If len inputs is invalid
        if len(inputs) not in (2, 3):
            print("Invalid input")
            return None
            
        
        operations = {
            "*": self.mul, # <-- function only, no () so we can provide
                            # this ourself later
            "-": self.sub,
            "/": self.div,
            "//": self.floordiv,
            "%": self.mod,
        }
        
        try:
            if len(inputs) == 2:
                x = self.current
                operation, y = inputs
                y = float(y)
            else:
                x, operation, y = inputs
                x, y = float(x), float(y)
            
            operation = operations[operation]
        except KeyError:
            print("Invalid operation.")
            return None
        except ValueError:
            print("Invalid input.")
            return None
            
        result = operation(x, y)
        
        self.current = result
        self.last_x = x
        self.last_operation = operation
        self.last_y = y
             
        return result
    
    def input_loop(self):
        while True:
            user_input = input("> ")
            if user_input == "quit":
                break
            
            result = self.interpret(user_input)
            if result:
                print(result)
            else:
                print("Invalid input.")
                continue
            
    
        


    def C(self):
        """Emulates the C button on a calculator, clearing the current
        memory."""
        self.current = 0

    def add(self, x, y):
        return x + y
        
    def sub(self, x, y):
        """Returns x - y using addition."""
        increment = 1 if x > y else -1
        count = 0
        while y != x:
            y = self.add(y, increment)
            count = self.add(count, increment)
        return count
                
    def mod(self, x, y):
        """Returns x % y using addition."""
        
        while x > y:
            x = self.sub(x, y)
                    
        if x < 0 and y < 0:
            while x < y:
                x = self.sub(x, y)
                
        if x < 0 and y > 0:
            while x < 0:
                x = self.add(x, y)
        
        if x == y:
            return 0
        
        return x
    
    def floordiv(self, x, y):
        """Returns x // y using addition."""
        #we need to count how many times we have to add x to x before
        #we are greater than y, then subtract one, or return inside
        #the loop would be better
        
        count = 0
        while y < x:
            if x.add(x) == y:
                count = x.sub(1)
        return count
            
        
        pass
    
    def div(self, x, y):
        """Returns x / y using addition."""
        #32 / 10 =
        #(floor, mod) = (3, 2)
        #then we again call div on the mod of this tuple;
        #(3, 2) --> 2 mod y --> (2, 0)
        #our answer is each of the floor divs; 3.2
        
        count = 0
        while x < y:
            join = (x.floordiv(), y.mod())
            join.floordiv()
            
        
        pass
        
    # def mul(self, x, y):
    #     """Returns x * y using addition."""
        
    #     return sum(x for _ in range(y))
        
    #     # x=5, y=3
    #     total = 0
    #     for _ in range(y):
    #         total += x
    #     return total


    
calc = Calculator()
print(calc.floordiv(32, 10))

# calc.input_loop()
# print(calc.current)
# print(calc.sub(100, 10))

# print(calc.current)
# print(calc.sub(100, 10))

"""
5.2 * 3.1 = 16.12

is the same as:
(5 * 3) + ((5 * 1) / 10) + ((2 * 3) / 10) + ((2 * 1) / 100)
"""
