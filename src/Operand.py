import random
class Operand:
    def __init__(self,operator):
        self.operator = operator
        if operator == '+':
            self.priority = 1
        elif operator == '-':
            self.priority = 1
        elif operator == '*':
            self.priority = 2
        elif operator == '÷':
            self.priority = 2
        else:
            self.priority = 0
    
    @classmethod
    def randomInit(cls):
        num = random.randint(0,3)
        if num == 0:
            operator = '+'
        elif num == 1:
            operator = '-'
        elif num == 2:
            operator = '*'
        elif num == 3:
            operator = '÷'
        return Operand(operator)
    
    def __str__(self):
        return self.operator
    
    def __lt__(self,other):
        return self.priority < other.priority
    
    def __le__(self,other):
        return self.priority <= other.priority
    
    def __eq__(self,other):
        return self.operator == other
    
    def __gt__(self,other):
        return self.priority > other.priority
    
    def __ge__(self,other):
        return self.priority >= other.priority
