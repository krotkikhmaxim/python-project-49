import random
from brain_games.aux_func import stack_result


TASK_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def func_prime():
    num = random.randrange(0, 100)
    сount_div = 0
    if num > 1:
        for i in range(1, num + 1):
            if num % i == 0:
                сount_div += 1
        if сount_div > 2:
            cor_ans = 'no'
        else:
            cor_ans = 'yes'
    else:
        cor_ans = 'no'
    return stack_result(f'{num}', cor_ans)
