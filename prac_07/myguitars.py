from guitar import Guitar


FILENAME = "guitars.csv"


def load_guitars(filename):
    guitars=[]
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0].strip()
        year = int(parts[1].strip())
        cost = float(parts[2].strip())
        guitars.append(Guitar(name, year, cost))
    return guitars


def main():
    guitars = load_guitars(FILENAME)

    print("These are the guitars")
    for guitar in guitars:
        print(guitar)
    add_new_guitars(guitars)

    guitars.sort()
    print("\nSorted guitars:")
    display_guitars(guitars)



def save_guitars(filename, guitars):
    """Write the list of Guitar objects to the CSV file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def display_guitars(guitars):
    """Display a list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")

def add_new_guitars(guitars):
    """Allow the user to enter new guitars."""
    print("\nAdd your own guitars!")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))


if __name__ == "__main__":
    main()