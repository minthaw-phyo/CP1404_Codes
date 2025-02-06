

MINIMUM_LENGTH = 4

def main():
    password = validate_password(MINIMUM_LENGTH)
    printing_asterisks(password)


def validate_password(minimum_length):
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


def printing_asterisks(sequence):
    print('*' * len(sequence))


if __name__ == "__main__":
    main()