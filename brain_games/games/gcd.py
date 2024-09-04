import random


TASK = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    for i in range(max(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


def conditions():
    num1 = random.randrange(0, 100)
    num2 = random.randrange(0, 100)
    cor_ans = get_gcd(num1, num2)
    return f'{num1} {num2}', cor_ans
