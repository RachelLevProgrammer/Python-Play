import tkinter as tk
from tkinter import simpledialog, messagebox


class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("איקס עיגול 🕹️")

        # שמות שחקנים
        self.player1_name = simpledialog.askstring("שחקן 1", "הכנס שם לשחקן 1 (X):") or "שחקן 1"
        self.player2_name = simpledialog.askstring("שחקן 2", "הכנס שם לשחקן 2 (O):") or "שחקן 2"

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.create_board()
        self.status_label = tk.Label(self.window, text=f"תור: {self.get_current_player_name()}", font=("Arial", 14))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

        self.window.mainloop()

    def get_current_player_name(self):
        return self.player1_name if self.current_player == "X" else self.player2_name

    def create_board(self):
        for i in range(9):
            button = tk.Button(
                self.window,
                text="",
                font=("Arial", 30, "bold"),
                width=5,
                height=2,
                command=lambda i=i: self.make_move(i)
            )
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            color = "red" if self.current_player == "X" else "blue"
            self.buttons[index].config(text=self.current_player, fg=color)

            winner = self.check_winner()
            if winner:
                self.highlight_winner(winner)
                messagebox.showinfo("ניצחון!", f"השחקן {self.get_current_player_name()} ניצח!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("תיקו", "המשחק הסתיים בתיקו!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"תור: {self.get_current_player_name()}")
        else:
            messagebox.showwarning("שגיאה", "המקום כבר תפוס!")

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return (a, b, c)
        return None

    def highlight_winner(self, winner_positions):
        for i in winner_positions:
            self.buttons[i].config(bg="yellow")

    def reset_board(self):
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="", bg="SystemButtonFace")
        self.current_player = "X"
        self.status_label.config(text=f"תור: {self.get_current_player_name()}")


if __name__ == "__main__":
    TicTacToeGUI()
