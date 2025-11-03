class Board:
    def __init__(self):
        self.PlatBoard = ['*'] * 9

    def __str__(self):
        rows = [self.PlatBoard[i:i + 3] for i in range(0, 9, 3)]
        board_str = ""
        for i, row in enumerate(rows):
            board_str += " | ".join(row) + "\n"
            if i < 2:
                board_str += "- + - + -\n"
        return board_str

    def make_move(self, marker, place):
        if self.PlatBoard[place] == '*':
            self.PlatBoard[place] = marker
            return True
        else:
            print("המקום כבר תפוס, נסה שוב.")
            return False

    def is_winner(self, marker):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # שורות
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # עמודות
            (0, 4, 8), (2, 4, 6)              # אלכסונים
        ]
        for condition in win_conditions:
            if all(self.PlatBoard[i] == marker for i in condition):
                return True
        return False

    def is_draw(self):
        return '*' not in self.PlatBoard
