# # Rock, Paper, Scissors Game
# import random

# play_game = True

# pScore = 0
# cScore = 0
# winner = "Rock, Paper, Scissors!"

# print("/*====================================*/")
# print("/*      ROCK, PAPER, SCISSORS         */")
# print("/*====================================*/")

# while play_game:
#   def play_match():
#     # Get player input
#     try:
#       player_choice = str(input("R [Rock], P [Paper] or S [Scissors]: ").lower())
#     # print(f"Player: {player_choice}")
#     # return player_choice
#     except: 
#       print("Enter a valid string, either Rock, Paper or Scissors!")
#     computer_options = ["rock", "paper", "scissors"]
#     computer_choice = random.choice(computer_options)

#     print(f"Player ({player_choice}) : CPU ({computer_choice})")


# # Exit the game
# print("The winner will be declared soon! See you soon!")

######################################################################################################

# import random

# def play_game():

#   p_score = 0
#   c_score = 0  

#   is_running = 0

#   while is_running < 3:
#     def play_match():
#       try:
#         player_choice = input("Rock[R] , Paper[P], Scissors[S]! Enter ['R', 'P', or 'S']: ").lower()
#       except:
#         if len(player_choice) != 1:
#           print("Enter a single character!")
#         else:
#           print("Input not valid, try again!")

#       cpu_options = ["r", "p", "s"]  
#       cpu_choice = random.choice(cpu_options)

#       print(f"Player({player_choice}) : CPU({cpu_choice})")

#       compare_plays(player_choice, cpu_choice)
    
#     play_match()
#     is_running += 1  

#   def update_score():
#     print(f"Player [{p_score}] : CPU [{c_score}]")

#   def compare_plays(player_choice, cpu_choice):
#     # check for tie
#     if(player_choice == cpu_choice):
#       print("It's a tie!")
#       update_score()
#       return
#     # check for rock
#     elif(player_choice == "r"):
#       if(cpu_choice == "s"):
#         print("Player wins!")
#         p_score+=1
#         update_score()
#         return
#       else:
#         print("Computer wins")
#         c_score+=1
#         update_score()
#         return
#     # check for paper
#     elif(player_choice == "p"):
#       if(cpu_choice == "r"):
#         print("Player wins!")
#         p_score+=1
#         update_score()
#         return
#       else:
#         print("Computer wins")
#         c_score+=1
#         update_score()
#         return
#       # check for scissors
#     elif(player_choice == "s"):
#       if(cpu_choice == "p"):
#         print("Player wins!")
#         p_score+=1
#         update_score()
#         return
#       else:
#         print("Computer wins")
#         c_score+=1
#         update_score()
#         return

#   def declare_winner(p_score, c_score):
#     if(p_score == c_score):
#       print("It's a tie. Nobody wins!")
#     elif(p_score > c_score):
#       print("Player wins the game!")
#     else:
#       print("CPU wins the game!")

#   # while is_running < 3:
    
#   declare_winner(p_score, c_score)

# play_game()

######################################################################################################

# import random

def play_game():
  start_game = True

  while start_game:
    print("Play Rock, Paper, Scissors!")
    print("""Instruction:
      Enter [r] for Rock, [p] for Paper and [s] for scissors!""")

    # loop to ensure game runs 3 times
    for x in range(3):
      # validate player choice
      player_choice = input("[r] Rock, [p] Paper, [s] Scissors? ")
      if player_choice == "r":
        player_choice_name = "Rock"
      elif player_choice == "p":
        player_choice_name = "Paper"
      elif player_choice == "s":
        player_choice_name = "Scissors"
      else:
        player_choice_name = "Enter a valid choice, bro!"

      print(player_choice_name)

    # play again prompt after game runs 3 times, plus exit from the while loop
    play_again = input("Do you want to continue playing? [y] / [n]: ")
    if play_again.lower() == "y":
      pass
    if play_again.lower() == "n":
      break

  print("Thank you for playing. See ya again!")

play_game()