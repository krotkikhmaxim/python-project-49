import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    сount_div = 0
    if num > 1:
        for i in range(1, num + 1):
            if num % i == 0:
                сount_div += 1
        if сount_div > 2:
            return False
        else:
            return True
    else:
        return False


def conditions():
    num = random.randrange(0, 100)
    if is_prime(num):
        cor_ans = 'yes'
    else:
        cor_ans = 'no'
    return f'{num}', cor_ans
