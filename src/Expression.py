import re
class Expression:
    def __init__(self,value,expression):
        self.value = value
        self.expression = expression
    
    @classmethod
    def parse(cls,str):  
        str = str.split(":",1)[1]
        # 使用正则表达式查找匹配的数字和运算符  
        pattern = r"(\d+/\d+)|(\d+(?:\'\d+/\d+)?)|([\+\-\*\÷\(\)])"  
        matches = re.findall(pattern, str)  
        
        # 将匹配的数字和运算符分别存储到列表中  
        numbers = []  
        operators = []  
        for match in matches:  
            if match[0]:  
                numbers.append(match[0])
            if match[1]:
                numbers.append(match[1])
            if match[2]:  
                operators.append(match[2])  
        
        return numbers, operators

    def __str__(self):
        return self.expression
    
    def __add__(self,other):
        value = self.value + other.value
        expression = self.expression + ' + ' + other.expression
        return Expression(value,expression)
    
    def __sub__(self,other):
        if(self.value > other.value):
            expression = self.expression + ' - ' + other.expression
            value = self.value - other.value
        else:
            expression = '(' + other.expression + ')' +' - ' + '(' + self.expression + ')'
            value = other.value - self.value
        return Expression(value,expression)
    
    def __mul__(self,other):
        value = self.value * other.value
        expression = self.expression + ' * ' + other.expression
        return Expression(value,expression)
    
    def __truediv__(self,other):
        value = self.value / other.value
        if(not value.isProp()):
            value = other.value / self.value
            expression = '(' + other.expression + ')' +' ÷ ' + '(' + self.expression + ')'
        else: 
            expression = self.expression + ' ÷ ' + other.expression
        return Expression(value,expression)
    
    def getValue(self):
        return self.value
