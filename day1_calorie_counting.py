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

    print(f"max: {max(elves)}")
    elves.sort(reverse=True)
    print(f"top 3: {elves[0] + elves[1] + elves[2]} (sum)")


main()
