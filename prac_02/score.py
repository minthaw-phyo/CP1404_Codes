"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    print(determine_score(score))
    random_score=random.randint(1,100)
    print(determine_score(random_score))

def determine_score(score):
    if score <0  or score >100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()


