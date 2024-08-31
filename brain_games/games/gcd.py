import random
from brain_games.aux_func import stack_result


TASK_GCD = 'Find the greatest common divisor of given numbers.'


def func_gcd():
    num1 = random.randrange(0, 100)
    num2 = random.randrange(0, 100)
    for i in range(max(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            cor_ans = i
            break
    return stack_result(f'{num1} {num2}', cor_ans)
