
# valid_response = False

# while valid_response == False:
     

#     if fav_animal == "Flamingo":
#         print("That's awesome!  They like meat!")
#         valid_response = True
#     elif fav_animal == "Horse":
#         print("Getty up!")
#         valid_response = True
#     elif fav_animal == "Gorilla":
#         print("King Kong aint got nothing on me!")
#         valid_response = True
#     else:
#         print("I guess you don't have a favorite animal!")
    
    
fav_animal = input("What is your favorite animal? ") # user input is a string -- ALWAYS

for char in fav_animal:
    if char == "a":
        break
    if char == "n":
        continue
    print(char + "ab")
    #test