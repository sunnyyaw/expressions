class ExpressionAssembler:
    @classmethod
    def build(cls, expressions, operators):  
        expres = []  
        operands = []   
        # 遇到括号递归计算表达式
        if len(operators)>0 and operators[-1] == '(':
            operators.pop()
            expre = ExpressionAssembler.build(expressions,operators)
            expres.append(expre)
        else:
            expres.append(expressions.pop()) 
        # 维护一个单调队列，队列中运算符的优先级总是升序排列
        while len(operators) > 0 : 
            operator = operators.pop()
            if operator == ')':
                break
            # 遇到优先级等于或小于队列末尾的运算符时不断弹出操作数和运算符进行计算，
            # 直到队列为空或者队列末尾运算符优先级小于将要入队的运算符优先级
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
        #当运算符全部入队时不断弹出运算符和操作数进行计算直到运算符为空
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
        #返回最终留在表达式列表的结果表达式
        return expres.pop()