import prompt


name = ''
cor_ans = ''
ans = ''
n = ''


def main():
    print('Welcome to the Brain Games!')


def welcome():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def logic(conditions, predicat, task):
    global ans
    i = 0
    print(task)
    while i < 3:
        conditions()
        if predicat():
            i += 1
            print('Correct!')
        else:
            break
    if i == 3:
        print(f'Congratulations, {name}"!')
    else:
        print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_ans}'.")
        print(f"Let's try again, {name}!")
