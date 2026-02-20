import tkinter as tk
from tkinter import messagebox

class TicTacToe:

    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = []

        self.create_board_feature_login()

    def create_board_feature_login(self):
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

        reset_button = tk.Button(
            self.root,
            text="Reiniciar",
            command=self.reset_game
        )
        reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Fin del juego", f"¡Jugador {self.current_player} gana!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Fin del juego", "¡Es un empate!")
                self.reset_game()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Verificar filas
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True

        # Verificar columnas
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True

        # Verificar diagonales
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True

        return False

    def is_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        for row in self.buttons:
            for button in row:
                button.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()