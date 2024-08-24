#!/usr/bin/env python3
from brain_games import function_set
import random


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    function_set.main()
    function_set.logic(conditions_even, task)


def conditions_even(question):
    n = random.randrange(0, 100)
    if n % 2 == 0:
        cor_ans = 'yes'
    else:
        cor_ans = 'no'
    question.append(f'{n}')
    return cor_ans


if __name__ == '__main__':
    main()
