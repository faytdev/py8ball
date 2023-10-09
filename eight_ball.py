import os
import time
import random


def get_answers() -> list[str]:
    cleaned = []
    with open("answers.txt", "r") as file:
        for line in file.readlines():
            cleaned.append(line.replace("\n", ""))

    return cleaned


def get_base() -> list[str]:
    with open("circle.txt", "r") as file:
        return file.readlines()


def insert_answer(answer: str, ball: list[str]) -> str:
    ans_padded = f" ,{answer.center(27)}," + "\n"
    ball[5] = ans_padded
    return "".join(ball)


def shake(count: int) -> None:
    ball = "".join(get_base())
    down = False
    os.system("cls")
    while count > 0:
        count -= 1
        if down:
            print("\n\n")
        down = not down
        print(ball)
        time.sleep(0.25)
        os.system("cls")


def main() -> None:
    answers = get_answers()
    ball = get_base()

    while 1:
        os.system("cls")
        print("Enter your question: ")
        question = input()

        if question.lower() == "q":
            break

        shake(random.randint(4, 10))

        answer = insert_answer(answers[random.randint(0, len(answers) - 1)], ball)

        print(question.upper() + "\n")
        print(answer)
        print("\n")
        print("Press enter to continue.")

        input()


if __name__ == "__main__":
    main()
