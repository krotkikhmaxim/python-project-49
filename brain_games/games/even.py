import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round_conditions():
    num = random.randrange(0, 100)
    if num % 2 == 0:
        cor_ans = 'yes'
    else:
        cor_ans = 'no'
    return f'{num}', cor_ans
