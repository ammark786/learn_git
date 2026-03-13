"""Entry point - uses calculator and utils. Good for rebase/merge practice."""

from calculator import add, subtract, multiply, divide
from utils import greet, format_number


def main() -> None:
    print(greet("Git Learner"))
    print("3 + 5 =", format_number(add(3, 5)))
    print("10 - 4 =", format_number(subtract(10, 4)))
    print("3 * 7 =", format_number(multiply(3, 7)))


if __name__ == "__main__":
    main()
