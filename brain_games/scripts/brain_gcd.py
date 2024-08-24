from brain_games import function_set
import random


task = 'Find the greatest common divisor of given numbers.'


def main():
    function_set.main()
    function_set.logic(conditions_gcd, task)


def conditions_gcd(question):
    n1 = random.randrange(0, 100)
    n2 = random.randrange(0, 100)
    for i in range(max(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            cor_ans = i
            break
    question.append(f'{n1} {n2}')
    return cor_ans


if __name__ == '__main__':
    main()
