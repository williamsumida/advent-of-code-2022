class Elf:
    def __init__(self, calories: list[int]) -> None:
        self.calories = calories
        self.total_calories = sum(self.calories)


def read_file() -> list[str]:
    with open("day1_input.txt") as f:
        lines = f.readlines()

    return lines


def main():
    input = read_file()
    calories: list[int] = []
    elves = []
    for text in input:
        if text == "\n":
            elves.append(sum(calories))
            calories = []
        else:
            calories.append(int(text.replace("\n", "")))

    print(max(elves))


main()
