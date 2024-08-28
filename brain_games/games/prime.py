import random


def conditions_prime(question):
    n = random.randrange(0, 100)
    k = 0
    if n > 1:
        for i in range(1, n + 1):
            if n % i == 0:
                k += 1
        if k > 2:
            cor_ans = 'no'
        else:
            cor_ans = 'yes'
    else:
        cor_ans = 'no'
    question.append(f'{n}')
    return cor_ans
