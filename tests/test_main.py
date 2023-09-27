import pytest
from Fraction import Fraction
from Expression import Expression
from ExpressionAssembler import ExpressionAssembler
from Operand import Operand
def test_a():
    fraction = Fraction.parse('2\'1/2')
    assert fraction.numerator == 5
    assert fraction.denominator == 2

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
if __name__ == "__main__":
    pytest.main()
