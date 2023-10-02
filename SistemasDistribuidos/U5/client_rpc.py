import xmlrpc.client

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

# ... (previous code)

def main():
    # Create a client proxy to connect to the server
    server = xmlrpc.client.ServerProxy("http://localhost:8000")

    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")

    # Initialize the game state
    cur_player = player1
    player_choice = {'X': "", 'O': ""}
    options = ['X', 'O']
    score_board = {player1: 0, player2: 0}
    values = [' '] * 9  # Initialize the Tic-Tac-Toe board

    while True:
        print_tic_tac_toe(values)

        print(f"Turn to choose for {cur_player}")
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print("Final Scores")
            scores = server.print_scoreboard()
            for player, score in scores.items():
                print(f"{player}: {score}")
            break

        else:
            print("Wrong Choice!!!! Try Again\n")

        # Play a single game
        while True:
            print_tic_tac_toe(values)
            print(f"Turno de {cur_player}. Cual casilla? : ", end="")
            try:
                move = int(input())
            except ValueError:
                print("Incorrecto!!! Intente de nuevo")
                continue

            if move < 1 or move > 9:
                print("Incorrecto!!! Del 1 al 9")
                continue

            if values[move - 1] != ' ':
                print("Ya se uso esa casilla. Intente de nuevo!!")
                continue

            values[move - 1] = cur_player

            # Function call for checking win
            if server.check_win({'X': [i + 1 for i, val in enumerate(values) if val == 'X'], 'O': [i + 1 for i, val in enumerate(values) if val == 'O']}, cur_player):
                print_tic_tac_toe(values)
                print("Player ", cur_player, " has won the game!!")
                print("\n")
                winner = cur_player
                break

            # Function call for checking draw game
            if server.check_draw({'X': [i + 1 for i, val in enumerate(values) if val == 'X'], 'O': [i + 1 for i, val in enumerate(values) if val == 'O']}):
                print_tic_tac_toe(values)
                print("Game Drawn")
                print("\n")
                winner = 'D'
                break

            # Switch player moves
            if cur_player == 'X':
                cur_player = 'O'
            else:
                cur_player = 'X'

        # Update the scoreboard
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] += 1

        print("Current Scores:")
        for player, score in score_board.items():
            print(f"{player}: {score}")

        # Switch player who chooses X or O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1

if __name__ == "__main__":
    main()
