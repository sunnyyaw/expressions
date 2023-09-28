import random
class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    @classmethod
    def randomInit(cls,max):
        denominator = random.randint(1,max-1)
        numerator = random.randint(1,max*denominator-1)
        return Fraction(numerator,denominator)
    
    @classmethod
    def parse(cls,str):
        if "'" in str:
            parts = str.split("'")  
            numerator = int(parts[0]) * int(parts[1].split("/")[1]) + int(parts[1].split("/")[0])  
            denominator = int(parts[1].split("/")[1])
        elif '/' not in str:  
            numerator = int(str)  
            denominator = 1  
        else:
            parts = str.split("/")
            numerator = int(parts[0]) 
            denominator = int(parts[1])
        return Fraction(numerator,denominator)
    
    def __str__(self):
        if(self.denominator == 0):
            return 'INF'
        self.simplify()
        integer = int(self.numerator / self.denominator)
        numerator = self.numerator % self.denominator
        denominator = self.denominator
        if(numerator == 0):
            return '%d'%(integer)
        elif(integer == 0):
            return '%d/%d'%(numerator,denominator)
        else:
            return '%d\'%d/%d'%(integer,numerator,denominator)
    
    def __add__(self,other):
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        fraction = Fraction(numerator,denominator)
        fraction.simplify()
        return fraction
    
    def __sub__(self,other):
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        fraction = Fraction(numerator,denominator)
        fraction.simplify()
        return fraction
    
    def __mul__(self,other):
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.numerator
        fraction = Fraction(numerator,denominator)
        fraction.simplify()
        return fraction
    
    def __truediv__(self,other):
        denominator = self.denominator * other.numerator
        numerator = self.numerator * other.denominator
        fraction = Fraction(numerator,denominator)
        fraction.simplify()
        return fraction
    
    def __lt__(self,other):
        if(self.denominator == 0):
            return False
        if(self.denominator != 0 and other.denominator == 0):
            return True
        selfnum = self.numerator / self.denominator
        othernum = other.numerator / other.denominator
        return selfnum < othernum
    
    def __eq__(self,other):
        if(self.denominator == 0 or self.denominator != 0 and other.denominator == 0):
            return False
        selfnum = self.numerator / self.denominator
        othernum = other.numerator / other.denominator
        return selfnum == othernum
    
    def __gt__(self,other):
        if(self.denominator == 0):
            return True
        if(self.denominator != 0 and other.denominator == 0):
            return False
        selfnum = self.numerator / self.denominator
        othernum = other.numerator / other.denominator
        return selfnum > othernum
    
    def simplify(self):
        a = abs(self.numerator)
        b = abs(self.denominator)

        if(a == 0 or b == 0):
            return
        if a<b:
            a,b = b,a
        r = a % b
        while(r != 0):
            a,b = b,r
            r = a % b
        gcd = b

        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd
    
    def isProp(self):
        return abs(self.numerator) < abs(self.denominator)
    