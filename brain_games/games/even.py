import random


def conditions_even(question):
    n = random.randrange(0, 100)
    if n % 2 == 0:
        cor_ans = 'yes'
    else:
        cor_ans = 'no'
    question.append(f'{n}')
    return cor_ans
