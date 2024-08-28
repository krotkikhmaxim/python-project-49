import random


def conditions_gcd(question):
    n1 = random.randrange(0, 100)
    n2 = random.randrange(0, 100)
    for i in range(max(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            cor_ans = i
            break
    question.append(f'{n1} {n2}')
    return cor_ans
