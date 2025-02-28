
"""
Word Occurrences
Estimate: 18 minutes
Actual:   15 minutes
"""

import csv

def read_wimbledon_data(filename):
    """Reads the CSV file and returns the data as a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)
        return [row for row in reader]


def process_wimbledon_data(data):
    champion_wins = {}
    countries = set()

    for row in data:
        champion = row[2]
        country = row[1]

        champion_wins[champion] = champion_wins.get(champion, 0) + 1

        countries.add(country)

    return champion_wins, countries


def display_data_results(champion_wins, countries):
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_wins.items()):
        print(f"{champion} {wins}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

def main():

    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champion_wins, countries = process_wimbledon_data(data)
    display_data_results(champion_wins, countries)


if __name__ == '__main__':
    main()