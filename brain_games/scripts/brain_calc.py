#!/usr/bin/env python3
from brain_games import function_set
import random


task = 'What is the result of the expression?'


def main():
    function_set.main()
    function_set.logic(conditions_calc, task)


def conditions_calc(question):
    z = ['+', '-', '*']
    n = random.randrange(0, 100)
    n2 = random.randrange(0, 100)
    x = random.randrange(0, 3)
    if z[x] == '+':
        cor_ans = n + n2
    elif z[x] == '-':
        cor_ans = n - n2
    elif z[x] == '*':
        cor_ans = n * n2
    question.append(f'{n} {z[x]} {n2}')
    return cor_ans


if __name__ == '__main__':
    main()
