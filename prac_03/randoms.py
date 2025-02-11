import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))



# What did you see on line 1? - using random.randint to get an integer between 5 and 20
# What was the smallest number you could have seen, what was the largest? smallest 5 and largest 20


# What did you see on line 2? using random.randint to get an integer between 3 and 10 with step size of 2
# What was the smallest number you could have seen, what was the largest? smallest 3 and largest 9
# Could line 2 have produced a 4? no cause of the step 2 so the possible answers are like 3, 5, 7, 9
#
# What did you see on line 3? using random.uniform to get a float between 2.5 and 5.5
# What was the smallest number you could have seen, what was the largest? smallest 2.5 and largest 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1,100))