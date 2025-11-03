from Player import Player
from xo_play import Board


def print_example_board():
    print("\nכך ממוספר הלוח – כדי שתדעו איפה לבחור מספר:")
    example = [str(i) for i in range(1, 10)]
    for i in range(0, 9, 3):
        print(" | ".join(example[i:i + 3]))
        if i < 6:
            print("- + - + -")
    print()


def run_game(player1, player2):
    board = Board()
    current_player = player1

    while True:
        print(board)
        move = current_player.get_move()
        if board.make_move(current_player.marker, move):
            if board.is_winner(current_player.marker):
                print(board)
                print(f"🎉 כל הכבוד {current_player.name}! אתה המנצח ({current_player.marker}) 🎉")
                break
            if board.is_draw():
                print(board)
                print("תיקו! המשחק הסתיים!")
                break
            current_player = player2 if current_player == player1 else player1


if __name__ == '__main__':
    print("ברוך הבא למשחק איקס-עיגול!")
    print_example_board()
    player1 = Player(input("הכנס שם לשחקן 1: "), 'X')
    player2 = Player(input("הכנס שם לשחקן 2: "), 'O')
    run_game(player1, player2)
