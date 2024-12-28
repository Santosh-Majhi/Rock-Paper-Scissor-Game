""" A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""

# import random
# item_list = ["Rock", "Paper", "Scissor"]

# user_choice = input("Enter your move = Rock, Paper, Scissor= ")
# comp_choice = random.choice(item_list)

# if user_choice not in item_list:
#     print("Please choose correct move")
# else:    
#     print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

# if user_choice == comp_choice:
#     print("Both chooses same: = Match Tie")

# elif user_choice == "Rock":
#     if comp_choice == "Paper":
#         print("Paper covers Rock = Computer Win")
#     else:
#         print("Rock smashes Scissor = You win")

# elif user_choice == "Paper":
#     if comp_choice == "Scissor":
#         print("Scissor cuts paper, Computer Win")
#     else:
#         print("Paper covers rock, You win")

# elif user_choice == "Scissor":
#     if comp_choice == "Paper":
#         print("Scissor cuts paper, You win")
#     else:
#         print("Rock smashes scissor, Computer win")





import random

try:
    item_list = ["Rock", "Paper", "Scissor"]

    user_choice = input("Enter your move from (Rock, Paper, Scissor): ").capitalize()

    if user_choice not in item_list:
        raise ValueError("Invalid move! Please choose Rock, Paper, or Scissor.")

    comp_choice = random.choice(item_list)

    print(f"User choice: {user_choice}, Computer choice: {comp_choice}")

    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and comp_choice == "Scissor") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissor" and comp_choice == "Paper"):
        print("Congratulations, you win!")
    else:
        print("Computer wins!")

except ValueError as ve:
    print(f"Input error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")        