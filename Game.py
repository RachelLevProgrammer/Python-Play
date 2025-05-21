import xo_play


class Player:

    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def get_move(self):
        while True:
            try:
                move = int(input(f"{self.name}, הכנס מספר בין 1 ל 9: "))
                if 1 <= move <= 9:
                    return move
                else:
                    print("הכנס מספר בין 1 ל 9")
            except ValueError:
                print("הכנס בבקשה מספר תקין")

# Function to run the game - switch turns, check winning, etc.
def run_game(player1, player2, board):
    current_player = player1
    while True:
        print(board)
        move = current_player.get_move()
        board.make_move(current_player.marker, move)
        if board.is_winner(current_player.marker):
            print(f"wow!!!!!  the winner is: {current_player.marker}")
            break
        if board.is_draw():
            print("תיקו!!!!!!!!!!!!!!!!!!!!! המשחק הסתים!!!!!!")
            break
        current_player = player2 if current_player == player1 else player1

# Example usage:
if __name__ == '__main__':
    board = xo_play.Board()
    print(board)
    player1 = Player(input("Enter player 1 name: "), 'X')
    player2 = Player(input("Enter player 2 name: "), 'O')
    run_game(player1, player2, board)