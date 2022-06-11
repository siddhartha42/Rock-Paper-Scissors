from random import randint
moves = ["rock", "paper", "scissors"]
while True:
  computer = moves[randint(0,2)]
  player = input("choose rock paper scissors or end the game\n").lower()
  if player == "end the game":
    print("the game has ended\n")
    break
  elif player == computer:
    print("draw, computer chose the same,", computer, '\n')
  elif player == "rock":
    if computer == "paper":
     print("you loose! computer chose", computer, '\n', "you chose", player,'\n')
    elif computer == "scissors":
       print("you win! you chose", player,'\n', "computer chose", computer,'\n')
  elif player == "paper":
   if  computer == "scissors":
       print("you loose! computer chose", computer, '\n', "you chose", player,'\n')
   elif computer== "rock":
       print("you win! you chose", player,'\n', "computer chose", computer,'\n')
  elif player== "scissors":
   if computer== "rock":
        print("you loose! computer chose", computer, '\n', "you chose", player, '\n')
   elif computer == "paper":
      print("you win! you chose", player,'\n',"computer chose", computer,'\n')
  else:
    print("check your spelling",'\n')
