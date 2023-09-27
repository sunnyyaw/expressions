import sys
import getopt
from Fraction import Fraction
from Expression import Expression
from Operand import Operand
from ExpressionAssembler import ExpressionAssembler

def generateExpressions(operandNum,maxNum):
    expressions = []
    operands = []
    propFrac1 = Fraction.randomInit(maxNum)
    expressions.append(Expression(propFrac1,str(propFrac1)))
    for i in range(operandNum):
        propFrac = Fraction.randomInit(maxNum)
        expressions.append(Expression(propFrac,str(propFrac)))
        operands.append(Operand.randomInit())
    return expressions,operands

def randomGenerate(n,maxNum):
    results = []
    for i in range(n):
        expressions,operands = generateExpressions(2,maxNum)
        results.append(ExpressionAssembler.build(expressions,operands))
    return results

def storeExercises(results):
    with open("Exercises.txt","w") as f:
        i = 0
        for result in results:
            f.write(str(i)+': ' + str(result)+' = \n')
            i+=1
    print('store Exercises successfully')

def storeAnswers(results):
    with open("Answers.txt","w") as f:
        i = 0
        for result in results:
            f.write(str(i)+': '+str(result.getValue())+'\n')
            i+=1
    print('store answers successfully')

def verifyAnswers(exercisesPath,answersPath):
    wrongs = []
    rights = []
    with open(exercisesPath,"r")as fe,open(answersPath,"r") as fa:
        exercises = fe.readlines()
        answers = fa.readlines()
        i = 0
        for exercise,answer in zip(exercises,answers):
            numbers,operators = Expression.parse(exercise)
            numbers2,operators2 = Expression.parse(answer)
            expressions = []
            expressions2 = []
            operands = []
            operands2 = []
            for number in numbers:
                fraction = Fraction.parse(number)
                expressions.append(Expression(fraction,str(fraction)))
            for number2 in numbers2:
                fraction = Fraction.parse(number2)
                expressions2.append(Expression(fraction,str(fraction)))
            for operator in operators:
                operand = Operand(operator)
                operands.append(operand)
            for operator2 in operators2:
                operand2 = Operand(operator2)
                operands2.append(operand2)
            expressions.reverse()
            expressions2.reverse()
            operands.reverse()
            operands2.reverse()
            expre = ExpressionAssembler.build(expressions,operands)
            answ = ExpressionAssembler.build(expressions2,operands2)
            if expre.getValue() == answ.getValue():
                rights.append(i)
            else:
                wrongs.append(i)
            i+=1
    print('Correct:'+str(rights))
    print('Worng:'+str(wrongs))

def main():
    argv = sys.argv[1:]
    n = 10
    r = 3
    e = None
    a = None
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
    
    results = randomGenerate(n,r)
    for result in results:
        print(str(result)+' = '+str(result.getValue()))
    storeExercises(results)
    storeAnswers(results)
    if(e is not None and a is not None):
        verifyAnswers(e,a)

if __name__ == "__main__":
    main()