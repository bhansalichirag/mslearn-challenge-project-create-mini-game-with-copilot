import random

def play_game():
    options = ["rock", "paper", "scissors"]
    player_score = 0
    rounds_played = 0

    while True:
        computer_choice = random.choice(options)
        player_choice = input("Enter your choice (rock/paper/scissors): ")

        print("Computer chose:", computer_choice)
        print("Player chose:", player_choice)

        if player_choice not in options:
            print("Invalid choice. Please try again.")
            continue

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("Player wins!")
            player_score += 1
        else:
            print("Computer wins!")

        rounds_played += 1

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print("Player score:", player_score)
    print("Rounds played:", rounds_played)

play_game()
