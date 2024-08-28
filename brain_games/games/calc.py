import random


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
