import random

def choice():
    
    player_choice = (input("Enter choice:")).lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice}
    return choices

def check(player, computer):
    options = ["rock", "paper", "scissors"]
    if player not in options:
        return "Invalid, Try typing rock, paper, scissors"
    
    print(f"You {player} vs Computer {computer}")
    if player == computer:
        return "Tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes Scissors! You WIN!"
        elif computer == "paper":
            return "Paper covers Rock! You LOSE!"
        else:
            return "Invalid, Try typing rock"
    elif player == "paper" :
        if computer == "rock":
            return "Paper covers Rock! You WIN!"
        elif computer == "scissors":
            return "Scissors cuts Paper! You LOSE!"
        else:
            return "Invalid, Try typing paper"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts Paper! You WIN!"
        elif computer == "rock":
            return "Rock smashes Scissors! You LOSE!"
        else:
            return "Invalid, Try typing scissors"
            
choices = choice()
result = check(choices["player"], choices["computer"])
print(result)
    
