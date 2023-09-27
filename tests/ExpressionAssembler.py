class ExpressionAssembler:
    @classmethod
    def build(cls, expressions, operators):  
        expres = []  
        operands = []   
        if len(operators)>0 and operators[-1] == '(':
            operators.pop()
            expre = ExpressionAssembler.build(expressions,operators)
            expres.append(expre)
        else:
            expres.append(expressions.pop()) 
        while len(operators) > 0 : 
            operator = operators.pop()

            if operator == ')':
                break
            
            while len(operands) > 0 and operator <= operands[-1]:  
                operand = operands.pop()  
                expression2 = expres.pop()  
                expression1 = expres.pop()  
                if str(operand) == '+':  
                    expression = expression1 + expression2  
                elif str(operand) == '-':  
                    expression = expression1 - expression2  
                elif str(operand) == '*':  
                    expression = expression1 * expression2  
                elif str(operand) == '÷':  
                    expression = expression1 / expression2  
                expres.append(expression)  
            operands.append(operator)  
            if len(operators)>0 and operators[-1] == '(':
                operators.pop()
                expre = ExpressionAssembler.build(expressions,operators)
                expres.append(expre)
            else:
                expres.append(expressions.pop()) 
        while len(operands) > 0:  
            operand = operands.pop()  
            expression2 = expres.pop()  
            expression1 = expres.pop()  
            if str(operand) == '+':  
                expression = expression1 + expression2  
            elif str(operand) == '-':  
                expression = expression1 - expression2  
            elif str(operand) == '*':  
                expression = expression1 * expression2  
            elif str(operand) == '÷':  
                expression = expression1 / expression2  
            expres.append(expression)  
        return expres.pop()