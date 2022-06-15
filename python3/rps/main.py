# Rock, Paper, Scissors Game
import random

def play_game():
  print("""
  /*=========================================================
  *            PLAY ROCK, PAPER, SCISSORS!                  *
  * Instruction:                                            *
  * Enter [r] for Rock, [p] for Paper and [s] for scissors! *
  ==========================================================*/
  """)
  
  # boolean while loop flag
  start_game = True

  while start_game:
    # validate player choice
    player_choice = input("[r] Rock, [p] Paper, [s] Scissors?: ")
    if player_choice == "r":
      player_choice_name = "rock"
    elif player_choice == "p":
      player_choice_name = "paper"
    elif player_choice == "s":
      player_choice_name = "scissors"
    else:
      print("Please enter a valid choice, bro!")
      continue

    # randomize cpu choice using choice() from random module
    cpu_options = ["r", "p", "s"]
    cpu_choice = random.choice(cpu_options)
    if cpu_choice == "r":
      cpu_choice_name = "rock"
    if cpu_choice == "p":
      cpu_choice_name = "paper"
    if cpu_choice == "s":
      cpu_choice_name = "scissors"

    # display player and cpu choices
    print(f"\nPlayer ({player_choice_name}) : CPU ({cpu_choice_name})")

    # compare player and cpu choices to determine winner
    if player_choice_name == cpu_choice_name:
      print("It's a tie! Play again!")
      continue
    elif player_choice_name == "rock":
      if cpu_choice_name == "scissors":
        print("Rock smashes scissors! Player wins!")
      else:
        print("Paper covers rock! CPU wins!")
    elif player_choice_name == "paper":
      if cpu_choice_name == "rock":
        print("Paper covers rock! Player wins!")
      else:
        print("Scissors cuts paper! CPU wins!")
    elif player_choice_name == "scissors":
      if cpu_choice_name == "paper":
        print("Scissors cuts paper! Player wins!")
      else:
        print("Rock smashes scissors! CPU wins!")

    # play again prompt after game runs, plus exit from the while loop
    play_again = input("\nDo you want to continue playing? [y] / [n]: ")
    if play_again.lower() == "y":
      pass
    if play_again.lower() == "n":
      break

  print("Thank you for playing. See ya again!")

play_game()