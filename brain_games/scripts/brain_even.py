#!/usr/bin/env python3
from brain_games import function_set
from brain_games import const
import random


def main():
    function_set.logic(conditions_even, const.task_even)


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
