# How lists work in Python
# Author: Juergen Lier
# Date: 12 June 2026
# Version 1

# Example list
# A list can contain numbers
my_list = [1, 2, 3, 4, 5] 
print(my_list)

# Can contain strings
zoo_list = ["Zebra", "Elephant", "Lion", "Monkey"]
print(zoo_list)

'''# Can also contain other variables
greeting = "Hello World!"
name = input("Hi what is your name? \n")
num_1 = int(input("First nr: "))
num_2 = int(input("Second nr: "))
sum = num_1 + num_2

random_list = [greeting, name, num_1, num_2, sum]
print(random_list)'''

# Can also contain a mix of data types
mixed_list = [my_list, 10, "Hello", 15.5]
print(mixed_list)

# Check if an item exists
if 10 in my_list:
    print("10 is in the list!")
else: 
    print("10 is not in the list!")

# Function to check if an item exists in a list
def check_item(item, list):
    print(f"Check whether {item} exists in {list}.")
    return item in list

print(check_item(3, my_list))

# Check for a list within a list
item = 3
def check_sublist(sublist, list):
    return all(item in list for item in sublist)

sublist = [2, 4]
print(check_sublist(sublist, my_list))

my_list = [1, 2, 3, 4, 5] 
# Check whether a user input is in the list
def check_user_input_in_list(list):
    try: 
        user_input = float(input("Enter a number to check whether it is in the list or not: "))
        if user_input in list:
            print(f"{user_input} is in the list.")
        else:
            print(f"{user_input} is not in the list.")

    except ValueError:
        print("Please enter a valid integer.")

# Example usage of the user input checking for number
done = ""
while done == "":
    check_user_input_in_list(my_list)
    done = input("Press <enter> to check another number or any other key to quit.")

# Function to find an item in a list of a list
def find_item_sublists(item, list_of_lists):
    for sublist in list_of_lists:
        if item in sublist:
            return True
    return False

# Example usage
length_units = ['mm','cm','m','km']
measurement_units =  ['mg','g','kg','t']
units = [length_units, measurement_units]
print(find_item_sublists('kg', units)) # Output: True
print(find_item_sublists('mile', units)) # output: False

# Check the length of a list
