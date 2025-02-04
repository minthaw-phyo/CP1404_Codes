from score import determine_score


MAIN_MENU ="Menu:\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def get_valid_score():
    while True:
        score = float(input("Enter a score between 0 and 100: "))
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid input. Please enter a score between 0 and 100.")


def show_stars(score):
    print(f"Stars: {'*' * int(score)}")


def main():
    score = 0

    while True:
        print(MAIN_MENU)
        choice = input("Please choose an option: ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Your score is {score}, and your result is: {determine_score(score)}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell! Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()