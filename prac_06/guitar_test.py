from prac_06.guitar import Guitar
import datetime

current_year = datetime.date.today().year

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 1000.00)


expected_age_guitar1 = current_year - guitar1.year
expected_age_guitar2 = current_year - guitar2.year

expected_vintage_guitar1 = True
expected_vintage_guitar2 = False


print(f"{guitar1.name} get_age() - Expected {expected_age_guitar1}. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected {expected_age_guitar2}. Got {guitar2.get_age()}")

print(f"{guitar1.name} is_vintage() - Expected {expected_vintage_guitar1}. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected {expected_vintage_guitar2}. Got {guitar2.is_vintage()}")


