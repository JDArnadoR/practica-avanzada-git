import tkinter as tk
from tkinter import messagebox


class TicTacToe:

    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="#1e1e2f")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = []

        self.title_label = tk.Label(
            root,
            text="TIC TAC TOE",
            font=("Helvetica", 28, "bold"),
            bg="#1e1e2f",
            fg="#ffffff"
        )
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.turn_label = tk.Label(
            root,
            text="Turno: X",
            font=("Helvetica", 16),
            bg="#1e1e2f",
            fg="#00d4ff"
        )
        self.turn_label.grid(row=1, column=0, columnspan=3, pady=5)

        self.create_board()

        self.reset_button = tk.Button(
            root,
            text="Reiniciar",
            font=("Helvetica", 14, "bold"),
            bg="#ff4d4d",
            fg="white",
            activebackground="#cc0000",
            command=self.reset_game
        )
        self.reset_button.grid(row=5, column=0, columnspan=3, sticky="nsew", pady=10)

    def create_board(self):
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Helvetica", 32, "bold"),
                    width=4,
                    height=2,
                    bg="#2d2d44",
                    fg="white",
                    activebackground="#3e3e5e",
                    relief="ridge",
                    bd=4,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row+2, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(
                text=self.current_player,
                fg="#00ff99" if self.current_player == "X" else "#ffcc00"
            )

            winner = self.check_winner()
            if winner:
                self.highlight_winner(winner)
                messagebox.showinfo("Fin del juego", f"¡Jugador {self.current_player} gana!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Fin del juego", "¡Es un empate!")
                self.reset_game()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.turn_label.config(
            text=f"Turno: {self.current_player}",
            fg="#00ff99" if self.current_player == "X" else "#ffcc00"
        )

    def check_winner(self):
        # Filas
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return [(i, 0), (i, 1), (i, 2)]

        # Columnas
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return [(0, i), (1, i), (2, i)]

        # Diagonal principal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return [(0, 0), (1, 1), (2, 2)]

        # Diagonal secundaria
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return [(0, 2), (1, 1), (2, 0)]

        return None

    def highlight_winner(self, positions):
        for row, col in positions:
            self.buttons[row][col].config(bg="#4CAF50")

    def is_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.turn_label.config(text="Turno: X", fg="#00d4ff")

        for row in self.buttons:
            for button in row:
                button.config(text="", bg="#2d2d44", fg="white")


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    game = TicTacToe(root)
    root.mainloop()