from brain_games import function_set
import random
import prompt


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    function_set.main()
    function_set.welcome()
    function_set.logic(conditions_prime, predicat_prime, task)


def conditions_prime():
    n = random.randrange(0, 100)
    print(f'Question: {n}')
    k = 0
    if n > 1:
        for i in range(1, n + 1):
            if n % i == 0:
                k += 1
        if k > 2:
            function_set.cor_ans = 'no'
        else:
            function_set.cor_ans = 'yes'
    function_set.ans = prompt.string('Your answer: ')


def predicat_prime():
    function_set.cor_ans
    function_set.ans
    return str(function_set.cor_ans) == str(function_set.ans)


if __name__ == '__main__':
    main()
