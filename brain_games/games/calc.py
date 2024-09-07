import random


DESCRIPTION = 'What is the result of the expression?'


def generate_round_conditions():
    operators = ['+', '-', '*']
    num1 = random.randrange(0, 100)
    num2 = random.randrange(0, 100)
    index_oper = random.randrange(0, 3)
    if operators[index_oper] == '+':
        cor_ans = num1 + num2
    elif operators[index_oper] == '-':
        cor_ans = num1 - num2
    elif operators[index_oper] == '*':
        cor_ans = num1 * num2
    return f'{num1} {operators[index_oper]} {num2}', cor_ans
