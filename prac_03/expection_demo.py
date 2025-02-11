"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? - when the user enter the string instead of integer to the numerator or denominator
2. When will a ZeroDivisionError occur?the user enter 0 instead of natural numbers to  denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError? yes by checking the condition for the value of denominator

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#code with changes
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
