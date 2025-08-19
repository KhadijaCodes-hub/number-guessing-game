import random

print("To quit the game type: 'exit'")
top_of_range=input("Type a number : ") 

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than 0.")
        quit()
else:
    print("Please type a number.") 
    quit()       

random_number = random.randint(0,top_of_range)

attempt=0

while True:
    attempt += 1
    user_guess = input("Guess a number : ")
    if user_guess!="exit":
        if user_guess.isdigit():
            user_guess=int(user_guess)
        else:
            print("Please type a number next time.")
            continue    

        if user_guess==random_number:
            print("Congratulations! You guessed it right.")
            break
        elif user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")
    else:
        quit()                

print(f"You got it in {attempt} attempts.")
    
