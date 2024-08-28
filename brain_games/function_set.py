import prompt
from brain_games import const


def logic(conditions, task):
    question = []
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{task}')
    for i in range(const.iterations):
        cor_ans = conditions(question)
        print(f'Question: {question.pop()}')
        ans = prompt.string('Your answer: ')
        if str(cor_ans) == str(ans):
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(.", end='')
            print(f" Correct answer was '{cor_ans}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
