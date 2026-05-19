# Demonstrate how to use an IF statement
# Author: Juergen Lier
# 1 May 2026
# Version 1

'''TODO: Create a program that will ask the user whether
they like coffee or not. If they do not like coffee, 
I will try to persuade them to try it.'''

# Checking whether you like Coffee and stores the answer in 
# a variable.
keep_going = ""
while keep_going == "":

    like_coffee = input("Do you like coffee? ")
    # print(like_coffee)

    if like_coffee == "yes":
        print("That is great! I like coffee too!")

    elif like_coffee == "no":
        print("You are missing out. Why not give it a try?")

    # else:
    #     print("Try again.")

    keep_going = input("Press <enter> to continue or any other key to quit")

print("All done.")

# Number demo
num_1 = int(input("Please enter your first number: "))
num_2 = int(input("Please enter your second number: "))

sum = num_1 + num_2

print(f"The answer to both your numbers added together is {sum}.")