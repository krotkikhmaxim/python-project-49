from brain_games import function_set
from brain_games.const import task_gcd
from brain_games.games.gcd import conditions_gcd


def main():
    function_set.logic(conditions_gcd, task_gcd)


if __name__ == '__main__':
    main()
