import random


TASK = 'What number is missing in the progression?'


def conditions():
    start = random.randrange(0, 100)
    step = random.randrange(1, 11)
    miss = random.randrange(0, 9)
    temp = start
    progression = ''
    for i in range(10):
        if i != miss:
            progression += str(temp) + ' '
        else:
            progression += '.. '
            cor_ans = temp
        temp += step
    return f'{progression}', cor_ans
