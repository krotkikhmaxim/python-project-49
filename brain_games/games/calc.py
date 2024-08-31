import random
from brain_games.aux_func import stack_result


TASK_CALC = 'What is the result of the expression?'


def func_calc():
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
    return stack_result(f'{num1} {operators[index_oper]} {num2}', cor_ans)
