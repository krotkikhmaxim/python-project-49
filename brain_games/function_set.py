import prompt


WELCOME = 'Welcome to the Brain Games!'

NUMBER_OF_ROUNDS = 3


def play(game):
    print(WELCOME)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{game.DESCRIPTION}')
    for _ in range(NUMBER_OF_ROUNDS):
        question, cor_ans = game.generate_round_conditions()
        print(f'Question: {question}')
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
