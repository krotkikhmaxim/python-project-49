import prompt


def main():
    print('Welcome to the Brain Games!')


def logic(conditions, task):
    question = []
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{task}')
    for i in range(3):
        cor_ans = conditions(question)
        print(f'Question: {question.pop()}')
        ans = prompt.string('Your answer: ')
        if str(cor_ans) == str(ans):
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_ans}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')