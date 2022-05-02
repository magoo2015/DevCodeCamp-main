#bonus1

# for count in range(1, 7):
    # if count == 1:
        # print("#")
    # elif count == 2:
        # print("##")
    # elif count == 3:
        # print("###")
    # elif count == 4:
        # print("####")
    # elif count == 5:
        # print("#####")
    # elif count == 6:
        # print("######")
    # elif count == 7:
        # print("#######")


#bonus2

# for count in range(1, 8):
    # if count == 1:
        # print(" # # # #")
    # elif count == 2:
        # print("# # # #")
    # elif count == 3:
        # print(" # # # #")
    # elif count == 4:
        # print("# # # #")
    # elif count == 5:
        # print(" # # # #")
    # elif count == 6:
        # print("# # # #")
    # elif count == 7:
        # print(" # # # #")
    # elif count == 8:
        # print("# # # #")

#bonus3
#It works not sure if using "in" was allowed.  

# ask_num = input("Add single digit numbers? ")
# #print(type(ask_num))
# count = 0

# for char in ask_num:
#     if char in ask_num:
#         count += 1
# print(count)

#bonus4
# f_num = int(input("Enter a number: ")) 
# #print(type(f_num))   

# #print(range(f_num, 0, -1))
# fact_num = 1

# for num in range(f_num, 0, -1):
#   fact_num = fact_num * num
# print(fact_num)

#bonus5

import random

number = random.randint(0,100)
print(number)  # used for test.  comment out when actually running
num_of_guesses = 4
hint = range(number -5, number +5, 1)
game_on = True

while game_on:
    user_guess = int(input("Guess a number between 1 and 100. "))
    if user_guess == number:
        print("You guessed right.  You win!")
        game_on = False #user wins, game ends
    elif user_guess != number:
        num_of_guesses -= 1
        print(f"You have {num_of_guesses} left!")
        if num_of_guesses == 1:
            print(f"Here's a clue, the number is between {min(hint)}-{max(hint)}")#How can I print this differently
        elif num_of_guesses == 0:
            print(f"Game over.  The correct number was {number}")
            game_on = False # user loses, game ends
    else:# do i need this or how can I change?
        print(f"You lost.  The correct number was {number}")
        game_on = False
        
#bonus6


# pay_roll = True
# cumulative_total = 0
#look to shortening this
# while pay_roll:
    # total_hours = int(input("Please enter total hours worked this week? \n"))
    # overtime_hours= total_hours - 40
    # pay_rate = 20
    # overtime_pay_rate = 1.5
    # total_overtime_pay = (pay_rate * overtime_pay_rate) * overtime_hours
    # total_week_pay = (40 * pay_rate) + total_overtime_pay 
    # print(total_week_pay)
    # cumulative_total += total_week_pay
    # add_week = input("Would you like to add another week? \n")
    # if add_week.lower() == "yes":
        # pay_roll = True #restart loop to add additionl weeks
    # else:
        # print(f"Here is your total for weeks entered: {cumulative_total}  \n")
        # pay_roll = False # kill loop