#!/usr/bin/env python3
from brain_games import function_set
import random
import prompt


def main():
    function_set.main()
    function_set.welcome()
    function_set.logic(conditions_even, predicat_even)


def predicat_even():
    if function_set.n % 2 == 0:
        function_set.cor_ans = 'yes'
    else:
        function_set.cor_ans = 'no'
    return function_set.cor_ans == function_set.ans


def conditions_even():
    function_set.n = random.randrange(0, 100)
    print(f'Question: {function_set.n}')
    function_set.ans = prompt.string('Your answer: ')


if __name__ == '__main__':
    main()
