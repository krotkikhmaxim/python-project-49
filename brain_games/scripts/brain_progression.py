from brain_games import function_set
import random
import prompt


task = 'What number is missing in the progression?'


def main():
    function_set.main()
    function_set.welcome()
    function_set.logic(conditions_progression, predicat_progression, task)


def conditions_progression():
    start = random.randrange(0, 100)
    step = random.randrange(1, 11)
    miss = random.randrange(0, 9)
    temp = start
    progression = ''
    for i in range(0, 10):
        if i != miss:
            progression += ' ' + str(temp)
        else:
            progression += ' ..'
            function_set.cor_ans = temp
        temp += step
    print(f'Question: {progression}')
    function_set.ans = prompt.string('Your answer: ')


def predicat_progression():
    function_set.cor_ans
    function_set.ans
    return str(function_set.cor_ans) == str(function_set.ans)


if __name__ == '__main__':
    main()
