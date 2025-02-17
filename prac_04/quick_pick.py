import random

# Constants
NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def generate_quick_pick():
    quick_pick = []

    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)

    return sorted(quick_pick)


def main():
    try:
        num_picks = int(input("How many quick picks? "))
        if num_picks < 1:
            print("Please enter a valid number")
            return

        for _ in range(num_picks):
            print(" ".join(f"{num:2}" for num in generate_quick_pick()))

    except ValueError:
        print("Invalid input. Please enter an integer.")



main()
