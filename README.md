| 这个作业属于哪个课程 | [计科21级12班 软件工程](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12) |
| ----------------- |--------------- |
| 这个作业要求在哪里| [作业链接](https://edu.cnblogs.com/campus/gdgy/CSGrade21-12/homework/13016) |
| 这个作业的目标 | 结对项目 |

[github链接](https://github.com/sunnyyaw/expressions)

| PSP2.1 | Personal Software Process Stages |预估耗时（分钟）| 实际耗时（分钟）|
| ----------------- |--------------- | ----------------- |--------------- |
| Planning | 计划 | 30 |60 |
| Estimate | 估计这个任务需要多少时间 | 30 | 60 |
| Development| 开发 | 720 | 900 |
| Analysis| 需求分析 (包括学习新技术) | 90 | 120 |
| Design Spec | 生成设计文档 | 30 | 60 |
| Design Review | 设计复审 |30 |30 |
| Coding Standard | 代码规范 (为目前的开发制定合适的规范) | 10 | 10 |
| Design | 具体设计 | 30 | 30 |
| Coding | 具体编码 | 360 | 420 |
| Code Review | 代码复审 | 30 | 30 |
| Test | 测试（自我测试，修改代码，提交修改）| 140 | 200 |
| Reporting | 报告 | 90 | 120 |
| Test Report | 测试报告 | 50 | 80 |
| Size Measurement | 计算工作量 | 20 | 20 |
| Postmortem & Process Improvement Plan | 事后总结, 并提出过程改进计划 | 20 | 20 |
|  | 合计 | 840 | 1080 |

接口的设计与实现：
---
- 总共设计了四个类和一个主函数程序。

- Fraction类定义了分数的两个属性分子和分母，并且重载了分数的加减乘除，并在转化为字符串时将假分数转化为带分数形式。

- Expression类定义了重载了表达式的加减乘除，当两表达式相减为负或者相除为假分数时将两表达式置换。
并且定义了一个将表达式分解为分数串和操作符串的类方法（例如"1: 2 + 3 * 7" 分解为 2 3 7，+ *,表达式前面必须由冒号分隔题目序号）

- ExpressionAssembler类定义了一个类方法，将给定的表达式串和之间的运算符串计算出结果表达式。

- Operand类定义了操作符的优先级，并且重载了它们之间的比较方式。

- main文件里定义了如何接收命令行参数选项，并根据参数随机生成n个拥有3个运算符的小学算术表达式。
并且提供了验证给定答案的正确率的函数。（答案文件和题目文件里的表达式必须有一个序号和冒号"n: "）

关键代码:
---
计算表达式的函数代码:
```python
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
            # 遇到优先级等于或小于队列末尾的运算符时不断弹出操作数和运算符进行计算，直到队列为空或者队列末尾运算符优先级小于将要入队的运算符优先级
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
```
性能改进:
---
可以看出程序的主要耗时集中在软件计算表达式的函数
```
        1474391 function calls in 1.136 seconds

     Ordered by: internal time

     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     10000    0.181    0.000    0.384    0.000 c:\Users\23028\myworkspace\算术表达式\tests\ExpressionAssembler.py:2(build)
     10000    0.122    0.000    0.623    0.000 c:\Users\23028\myworkspace\算术表达式\tests\main.py:8(generateExpressions)
     80000    0.111    0.000    0.191    0.000 D:\python3.7\lib\random.py:174(randrange)
     30000    0.083    0.000    0.290    0.000 c:\Users\23028\myworkspace\算术表达式\tests\Fraction.py:7(randomInit)
     80000    0.075    0.000    0.267    0.000 D:\python3.7\lib\random.py:218(randint)
     40000    0.065    0.000    0.109    0.000 c:\Users\23028\myworkspace\算术表达式\tests\Fraction.py:28(__str__)
     62505    0.065    0.000    0.072    0.000 c:\Users\23028\myworkspace\算术表达式\tests\Fraction.py:95(simplify)
     80000    0.061    0.000    0.081    0.000 D:\python3.7\lib\random.py:224(_randbelow)
     20000    0.042    0.000    0.117    0.000 c:\Users\23028\myworkspace\算术表达式\tests\Operand.py:16(randomInit)
         1    0.026    0.026    1.034    1.034 c:\Users\23028\myworkspace\算术表达式\tests\main.py:19(randomGenerate)
```
单元测试:
---
- 测试函数是否能正确解析分数
```python
      def test_a():
          fraction = Fraction.parse('2\'1/2')
          assert fraction.numerator == 5
          assert fraction.denominator == 2
```
- 测试函数是否能正确计算表达式
```python
  def test_b():
      expressions = []
      operands = []
      numbers,operators = Expression.parse("1:(3 * 5) - (2) ")
      for number in numbers:
          fraction = Fraction.parse(number)
          expressions.append(Expression(fraction,str(fraction)))
      for operator in operators:
          operand = Operand(operator)
          operands.append(operand)
      expressions.reverse()
      operands.reverse()
      expre = ExpressionAssembler.build(expressions,operands)
      assert expre.getValue() == Fraction.parse("13")
```

异常处理说明:
---
- 处理没有正确传入参数的问题
```python
try:
    options,args = getopt.getopt(argv,"n:r:e:a:")
    except:
        print('Error')
    for opt,arg in options:
        if opt in ('-n'):
            n = int(arg)
        elif opt in ('-r'):
            r = int(arg)
        elif opt in ('-e'):
            e = arg
        elif opt in ('-a'):
            a = arg
```