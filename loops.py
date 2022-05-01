# #For Loops Task1
# for i in range(5):
#     print("Hello")

# #For Loops Task2
# for num in range(11):
#     print(num)

#For Loops Task3
# for num in range(10, -1, -1):
#     print(num)

#For Loops Task4
# run_count = int(input("Enter run count: "))

# for r_count in range(run_count):
#     print("devCodeCamp")

#For Loops Task4

# team = "Packers"

# for char in team:
#     print(char)

#FizzBuzz Challenge

for num in range(0, 101):
    if num % 3 == 0 and num % 5 == 0: # Moved this condition to the top to prevent premature triggers.
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
        

#while loop task1

# loop = 0

# while loop < 5:
#     print("hello")
#     loop += 1

#while loop task2

# password = "12345"
# user_validated = False

# while user_validated == False:
#     pwd = input("What is your pwd")
#     if pwd == password:
#         print("User_Validated")
#         user_validated = True
    