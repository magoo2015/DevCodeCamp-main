# Example function:
# def display_name(name):
    # print(name)
    #  this is the logic of the function

# The above function takes in a variable, known as the parameter.
# In this example, that variable is name.
# The function then prints to the console the value that is passed in


# display_name('Mike')
# display_name('Ian')
# display_name('Nevin')

# Above we are now calling the function. This means using the function that we wrote.
# Here we are passing in an actual value. In this case, the value is 'Mike'

# Example 2

# 
# def add_one_to_number(number):
    # number_one = 1
    # add_one = number + number_one
    # return add_one

# The above function takes in a variable, known as the parameter.
# In this example, that variable is number.
# The function then adds one to the parameter and returns the sum


#result = add_one_to_number(30)

# Above we are now calling the function. This means using the function that we wrote.
# Here we are passing in an actual value. In this case, the value is 30
# We create and set a variable equal to the function call becuase the function returns a value

# Problem 1
# Write a function that takes in two numbers
# The logic of the function should add those two numbers together and return a sum
# Capture the returned value in a variable and print it to the console


# def add_numbers(num_1, num_2):
    # add_integers = num_1 + num_2
    # return add_integers
# 
# sum = add_numbers(10, 20)
# print(sum)

# Problem 2
# Write a function that takes in two strings
# The logic of the function should concatenate those two strings together and return the concatenated result
# Capture the returned value in a variable and print it to the console
# 
# string_1 = "I just want to play apex legends"
# string_2 = "I have grown up problems"
# 
# def two_strings(string_1, string_2):
    # return string_1 + string_2
# 
# 
# string3 = two_strings(string_1, string_2)
# print(string3)
# 
# Problem 3
# Write a function that takes in a string
# The logic of the function should print each character of the string one at a time to the console
# HINT: for loop is one way to do this

# my_string ="Lets go Mavericks!"
# 
# def loop_through_string(my_string):
    # for char in my_string:
        # print(char)
# 
# loop_through_string(my_string)

# Problem 4
# Write a function that takes in a string
# The logic of the function should print the string to the console but only if that string has three or more characters in it
# If it is less than three characters, then print to the console 'we need a larger string to print!'

how_many_strings = input("Input string: ")


def mystring(how_many_strings):
    string_count = 0
    for char in how_many_strings:
        string_count += 1
    if string_count >= 3:
        print(how_many_strings)
    else:
         print("We need a larger string to print")

mystring(how_many_strings)
    