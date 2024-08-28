import random


def conditions_progression(question):
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
    question.append(f'{progression}')
    return cor_ans
