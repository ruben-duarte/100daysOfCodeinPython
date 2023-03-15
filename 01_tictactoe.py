# print board

def print_tic_t_t(values):
    print("\n")
    print("\t         |        |")
    print(f"\t    {values[0]}    |   {values[1]}    |    {values[2]}" )
    print("\t_________|________|________")
    print("\t         |        |")
    print(f"\t    {values[3]}    |   {values[4]}    |    {values[5]}" )
    print("\t_________|________|________")
    print("\t         |        |")
    print(f"\t    {values[6]}    |   {values[7]}    |    {values[8]}" )
   # print("\t_________|________|________")
    print("\n")

#print_tic_t_t([1,2,3,4,5,6,7,8,9])

#score_board

def print_scoreboard(score_board):
    print("\n")
    print("\t" + "-"*70)
    print("\t                   Tablero de puntuación TIC TAC TOE                 ")
    print("\t" + "-"*70)

    players = list(score_board.keys())
    print("\t     " , players[0], "\t     ", score_board[players[0]])
    print("\t     " , players[1], "\t     ", score_board[players[1]])
    print("\t" + "-"*70+"\n")


#check if any player has won the game
def check_winner(player_position, current_player):
    soln = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    #check winning combination
    for x in soln:
        if all(y in player_position[current_player] for y in x):
                return True
    return False

#check draw
def check_draw(player_position):
     if len(player_position['X'])+len(player_position['O']) == 9:
            return True
     return False

#single game
def single_game(current_player):
     values = [' ' for x in range(9)]
     player_position = {'X':[], 'O':[], }
     while True:
          print_tic_t_t(values)
          try:
               print("Player  ", current_player, "turn. which box? ",end="")
               move = int(input())
          except ValueError:
               print("Wrong input!! Try again")
               continue
          
          if move < 1 or move > 9:
               print("Please choose  the right number between 1 and 9")
               continue
          
          if values[move-1] != ' ':
               print("The place you have chosen is already filled")
               continue
          #update game status
          #board
          values[move-1] = current_player
          #player position
          player_position[current_player].append(move)

          if check_winner(player_position, current_player):
               print_tic_t_t(values)
               print("Player ", current_player, " Has won the game")
               print("\n")
               return current_player
          
          if check_draw(player_position):
               print_tic_t_t(values)
               print("Game is a draw")
               print("\n")
               return 'D'
          
          #Switch players
          if current_player == 'X' :
               current_player = 'O'
          else:
               current_player = 'X'


if __name__ == '__main__':
     print("player 1 info")
     play1  = input("Enter the name of the player :  ")
     print("\n")
     print("player 2 info")
     play2  = input("Enter the name of the player :  ")
     print("\n")
     current_player = play1

     player_choice = {'X' : "", 'O':""}
     options = ['X','O']
     score_board = {play1: 0 , play2: 0}
     print_scoreboard(score_board)

     while True:
          print("Turn to choose for ", current_player)
          print("""
            Enter  1 for X
            Enter  2 for O
            Enter  3  to quit
          """)

          try:
               choice  = int(input())
          except ValueError:
               print("Wrong input , try again \n")
            
            #conditions for player
          if choice == 1:
               player_choice["X"] = current_player
               if current_player == play1:
                    player_choice["O"] = play2
               else:
                    player_choice["O"] = play1
          elif choice == 2:
               player_choice["O"] = current_player
               if current_player == play1:
                    player_choice["X"] = play2
               else:
                    player_choice["X"] = play1
          elif choice == 3:
               print("Final scores")
               print_scoreboard(score_board)
               break
          else:
               print(" wrong choice , try again \n")
          winner = single_game(options[choice-1])
          if winner != 'D':
               player_won= player_choice[winner]
               score_board[player_won] = score_board[player_won] +1

          print_scoreboard(score_board)
          if current_player == play1:
               current_player == play2
          else:
               current_player = play1



    


     


