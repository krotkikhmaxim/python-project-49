from brain_games import function_set
import random
import prompt


task = 'Find the greatest common divisor of given numbers.'


def main():
    function_set.main()
    function_set.welcome()
    function_set.logic(conditions_gcd, predicat_gcd, task)


def conditions_gcd():
    n1 = random.randrange(0, 100)
    n2 = random.randrange(0, 100)
    print(f'Question: {n1} {n2}')
    for i in range(max(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            function_set.cor_ans = i
            break
    function_set.ans = prompt.string('Your answer: ')


def predicat_gcd():
    function_set.cor_ans
    function_set.ans
    return str(function_set.cor_ans) == str(function_set.ans)


if __name__ == '__main__':
    main()
