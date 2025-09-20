import os
import time
import random
import platform


def clear_screen() -> None:
    system: str = platform.system()
    if system == "win32":
        os.system("cls")
    else:
        os.system("clear")


def get_answers() -> list[str]:
    with open("answers.txt", "r") as file:
        return [line.strip("\n") for line in file]


def get_ball() -> list[str]:
    with open("circle.txt", "r") as file:
        return file.readlines()


def insert_answer(answer: str) -> str:
    ball: list[str] = get_ball()
    ans_padded = f" ,{answer.center(27)}," + "\n"
    ball[5] = ans_padded
    return "".join(ball)


def shake(count: int) -> None:
    ball = "".join(get_ball())
    down = False
    clear_screen()
    while count > 0:
        count -= 1
        if down:
            print("\n\n")
        down = not down
        print(ball)
        time.sleep(0.25)
        clear_screen()


def main() -> None:
    clear_screen()
    answers = get_answers()

    while 1:
        clear_screen()
        print("Enter your question (q to quit): ")

        question = input()
        if question.lower() == "q":
            break

        shake(random.randint(4, 10))
        answer = answers[random.randint(0, len(answers) - 1)]
        print(f"{question.upper()}\n{insert_answer(answer)}\n")

        keep_going: str = input("Press enter to continue, enter q to quit:")
        if keep_going.lower() in ("q", "quit"):
            break


if __name__ == "__main__":
    main()
