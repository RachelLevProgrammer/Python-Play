class Board:
    def __init__(self):
        self.PlatBoard = ['*'] * 9

    def __str__(self):
        rows = [self.PlatBoard[i:i + 3] for i in range(0, 9, 3)]
        board_str = ""
        for row in rows:
            board_str += " | ".join(row) + "\n"
            if row != rows[-1]:
                board_str += "-+-" * 2 + "-\n"
        return board_str

    def make_move(self, player, place):
        if self.PlatBoard[place] == '*':
            print("המקום פנוי")
            self.PlatBoard[place] = player.marker  # עדכון כאן למרקר של השחקן
        else:
            print("המקום מלא")

    def is_winner(self, marker):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]
        for condition in win_conditions:
            if all(self.PlatBoard[i] == marker for i in condition):
                print(f"wow!!!!! the winner is: {marker}")
                return True
        return False

    def is_draw(self):
        return '*' not in self.PlatBoard
