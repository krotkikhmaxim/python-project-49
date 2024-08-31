import random
from brain_games.aux_func import stack_result


TASK_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def func_even():
    num = random.randrange(0, 100)
    if num % 2 == 0:
        cor_ans = 'yes'
    else:
        cor_ans = 'no'
    return stack_result(f'{num}', cor_ans)
