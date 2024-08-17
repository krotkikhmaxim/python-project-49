import prompt
import random


def main():
    print('Welcome to the Brain Games!')


name = ''


def welcome():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def logic_brain_even():
    i = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i < 3:
        n = random.randrange(0, 100)
        print(f'Question: {n}')
        answer = prompt.string('Your answer: ')
        if n % 2 == 0 and answer == 'yes' or n % 2 != 0 and answer == 'no':
            i += 1
            print('Correct!')
        else:
            break
    if i == 3:        
        print(f'Congratulations, {name}"!')
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        print(f"Let's try again, {name}!")

