from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Function to print Tic Tac Toe
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 
# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t        TABLERO DE PUNTOS       ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")

# Function to check if any player has won
def check_win(player_pos, cur_player):
 
    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
 
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False       

# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False   

# Function for a single game of Tic Tac Toe
def single_game(cur_player):
 
    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]
     
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
     
    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)
         
        # Try exception block for MOVE input
        try:
            print("Turno de ", cur_player, ". Cual casilla? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Incorrecto!!! Intente de nuevo")
            continue
 
        # Sanity check for MOVE input
        if move < 1 or move > 9:
            print("Incorrecto!!! Del 1 al 9")
            continue
 
        # Check if the box is not occupied already
        if values[move-1] != ' ':
            print("Ya se uso esa casilla. Intente de nuevo!!")
            continue
 
        # Update game information
 
        # Updating grid status 
        values[move-1] = cur_player
 
        # Updating player positions
        player_pos[cur_player].append(move)
 
        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")     
            print("\n")
            return cur_player
 
        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'
 
        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
            
# Create an instance of the XML-RPC server
server = SimpleXMLRPCServer(('localhost', 8000), allow_none=True)

# Register the functions
server.register_function(print_tic_tac_toe, 'print_tic_tac_toe')
server.register_function(print_scoreboard, 'print_scoreboard')
server.register_function(check_win, 'check_win')
server.register_function(check_draw, 'check_draw')
server.register_function(single_game, 'single_game')

# Run the server
print("Server is listening on port 8000...")
server.serve_forever()
