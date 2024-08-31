import random
from brain_games.aux_func import stack_result


TASK_PROGRESSION = 'What number is missing in the progression?'


def func_progression():
    start = random.randrange(0, 100)
    step = random.randrange(1, 11)
    miss = random.randrange(0, 9)
    temp = start
    progression = ''
    for i in range(0, 10):
        if i != miss:
            progression += str(temp) + ' '
        else:
            progression += '.. '
            cor_ans = temp
        temp += step
    return stack_result(f'{progression}', cor_ans)
