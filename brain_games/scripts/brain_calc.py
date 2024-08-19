#!/usr/bin/env python3
from brain_games import function_set
import random
import prompt


task = 'What is the result of the expression?'


def main():
    function_set.main()
    function_set.welcome()
    function_set.logic(conditions_calc, predicat_calc, task)


def conditions_calc():
    z = ['+', '-', '*']
    n = random.randrange(0, 100)
    n2 = random.randrange(0, 100)
    x = random.randrange(0, 3)
    print(f'Question: {n} {z[x]} {n2}')
    if z[x] == '+':
        function_set.cor_ans = n + n2
    elif z[x] == '-':
        function_set.cor_ans = n - n2
    elif z[x] == '*':
        function_set.cor_ans = n * n2
    function_set.ans = prompt.string('Your answer: ')


def predicat_calc():
    function_set.cor_ans
    function_set.ans
    return str(function_set.cor_ans) == str(function_set.ans)


if __name__ == '__main__':
    main()
