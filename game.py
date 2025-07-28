import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("type rock/paper/scissors or Q to quit game:").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # 0 for rock, 1 for paper, 2 for scissors
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}")
    
    if user_input == 'rock' and computer_pick == 'scissors':
        print("You win!")
        user_wins += 1
        
    elif user_input == 'paper' and computer_pick == 'rock':
        print("You win!")
        user_wins += 1
        
    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You win!")
        user_wins += 1
    
    else:
        print("You lose!")
        computer_wins += 1
        
print(f"You won {user_wins} times and the computer won {computer_wins} times.")
print("Thanks for playing!")
print("Goodbye!")
    