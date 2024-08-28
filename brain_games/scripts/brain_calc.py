#!/usr/bin/env python3
from brain_games import function_set
from brain_games import const
import random


def main():
    function_set.logic(conditions_calc, const.task_calc)


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
