import random

dict = {"r": "Rock", "p": "Paper", "s": "Scissors"}

while True:
    bot_choice = random.choice(tuple(dict.keys())).lower()
    user_choice = input("Choose among (r/p/s) or 'e' for exit : ").lower()

    if (bot_choice == user_choice):
        print(
            f"Draw! you choose {dict[user_choice]} Opponent choose {dict[bot_choice]}")

    elif ((bot_choice == "r" and user_choice == "p") or (bot_choice == "p" and user_choice == "s") or (bot_choice == "s" and user_choice == "r")):
        print(
            f"You win! you choose {dict[user_choice]} Opponent choose {dict[bot_choice]}")

    elif (user_choice == "e"):
        print("Thanks for playing!")
        break

    elif (user_choice not in dict.keys()):
        print("Invalid! choice choose among 'r/s/p' or 'e' for exit")

    else:
        print(
            f"You lose! you choose {dict[user_choice]} Opponent choose {dict[bot_choice]}")