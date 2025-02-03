# price = float(input("Enter the price: "))
# gst_include = str(input("GST include (y/n): "))
#
#
# if gst_include == "y":
#     price = price + (price * 0.09)
# print(f"$ ${price}")


# max_number = int(input("Enter a number: "))
#
# for num in range(1,max_number+1):
#     print(num, end=" ")
#
# print()
#
# num=0
# while num < max_number:
#     num+=1
#     print(num,end=" ")


# import random
#
# CHOICE_NUMBER = random.randint(1,10)
#
# user_choice =int(input("Guess the number : "))
#
# while user_choice != CHOICE_NUMBER:
#     user_choice = int(input("Guess the number : "))
#
# print("U choice the right number")

#
# username = input("Enter username: ")
# salary = input("Enter the salary: ")
#
# while username == "" or salary == "" or not salary.isdigit() or float(salary) < 0:
#     print("Error: Username can't be blank, salary must be a positive number.\n")
#     username = input("Enter username: ")
#     salary = input("Enter the salary: ")
#
# print("Username:", username.upper())
# print(f"Salary: ${float(salary):.2f}")



# num_of_ages = int(input("Enter the number of ages :"))
# TOTAL_AGES=0
# for i in range(1,num_of_ages+1):
#     age = int(input("Enter the age "))
#     TOTAL_AGES +=age
#
# average_age = TOTAL_AGES / num_of_ages
# print("Total Ages : ", TOTAL_AGES)d
# print("Average of Ages :", average_age)

#
# age=int(input("Enter the age: "))
#
# while age != -1:
#     age = int(input("Enter the age: "))
#
# print("Finished")



for i in range(1,4):
    for j in range(2,10,3):
        print(i," - " ,j +i)