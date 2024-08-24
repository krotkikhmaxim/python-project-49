from brain_games import function_set
import random


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    function_set.main()
    function_set.logic(conditions_prime, task)


def conditions_prime(question):
    n = random.randrange(0, 100)
    k = 0
    if n > 1:
        for i in range(1, n + 1):
            if n % i == 0:
                k += 1
        if k > 2:
            cor_ans = 'no'
        else:
            cor_ans = 'yes'
    question.append(f'{n}')
    return cor_ans


if __name__ == '__main__':
    main()
