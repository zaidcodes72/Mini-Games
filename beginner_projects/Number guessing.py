import random

bot_choice = random.randint(1, 99)

while True:
    try:
        user_choice = int(input("Guess the number b/w (1,99) : "))
        if (user_choice != bot_choice):
            if (user_choice > bot_choice):
                print(f"you choose greater number choose again!")
           

            elif (user_choice < bot_choice):
                print(f"you choose lower number choose again!")

        elif (user_choice == bot_choice):
            print(f"Perfect the number you guessed is correct! Number is {bot_choice}")
            break
        
    except ValueError:
        print ("Please enter the valid number")

    
