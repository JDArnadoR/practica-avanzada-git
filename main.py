import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    """
    Clase principal que implementa el juego Tic Tac Toe
    utilizando la librería Tkinter para la interfaz gráfica.
    """

    def __init__(self, root):
        # Guardamos la ventana principal
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="#1e1e2f")  # Color de fondo de la ventana

        # Jugador actual (empieza X)
        self.current_player = "X"

        # Matriz lógica 3x3 que representa el tablero
        self.board = [["" for _ in range(3)] for _ in range(3)]

        # Lista que almacenará los botones del tablero
        self.buttons = []

        # Bandera para saber si el juego terminó
        self.game_over = False

        # Etiqueta del título
        self.title_label = tk.Label(
            root,
            text="TIC TAC TOE",
            font=("Helvetica", 28, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Etiqueta que muestra el turno actual
        self.turn_label = tk.Label(
            root,
            text="Turno: X",
            font=("Helvetica", 16),
            bg="#1e1e2f",
            fg="#00ff99"
        )
        self.turn_label.grid(row=1, column=0, columnspan=3, pady=5)

        # Creamos el tablero visual
        self.create_board()

        # Botón para reiniciar el juego manualmente
        self.reset_button = tk.Button(
            root,
            text="Reiniciar tablero",
            font=("Helvetica", 14, "bold"),
            bg="#ff4d4d",
            fg="white",
            activebackground="#cc0000",
            command=self.reset_game  # Llama a reset_game al hacer clic
        )
        self.reset_button.grid(row=5, column=0, columnspan=3, sticky="nsew", pady=10)

    def create_board(self):
        """
        Crea los botones del tablero 3x3 y los coloca en la ventana.
        """
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
                    # Se usa lambda para pasar la posición del botón
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                # Se coloca el botón en la cuadrícula
                button.grid(row=row+2, column=col, padx=5, pady=5)
                button_row.append(button)

            # Guardamos la fila de botones
            self.buttons.append(button_row)

    def make_move(self, row, col):
        """
        Ejecuta una jugada cuando el usuario presiona un botón.
        """
        # Solo permite jugar si la celda está vacía y el juego no terminó
        if self.board[row][col] == "" and not self.game_over:
            # Actualiza la matriz lógica
            self.board[row][col] = self.current_player

            # Actualiza el botón visual
            self.buttons[row][col].config(
                text=self.current_player,
                fg="#00ff99" if self.current_player == "X" else "#ffcc00"
            )

            # Verifica si hay ganador
            winner = self.check_winner()
            if winner:
                self.highlight_winner(winner)  # Resalta la combinación ganadora
                self.game_over = True
                messagebox.showinfo("Fin del juego", f"¡Jugador {self.current_player} gana!")
            # Verifica si hay empate
            elif self.is_draw():
                self.game_over = True
                messagebox.showinfo("Fin del juego", "¡Es un empate!")
            else:
                # Cambia de jugador si el juego continúa
                self.switch_player()

    def switch_player(self):
        """
        Cambia el turno entre X y O y actualiza la etiqueta visual.
        """
        self.current_player = "O" if self.current_player == "X" else "X"

        self.turn_label.config(
            text=f"Turno: {self.current_player}",
            fg="#00ff99" if self.current_player == "X" else "#ffcc00"
        )

    def check_winner(self):
        """
        Revisa filas, columnas y diagonales para detectar un ganador.
        Devuelve las posiciones ganadoras si existen.
        """
        # Revisar filas
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return [(i, 0), (i, 1), (i, 2)]

        # Revisar columnas
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return [(0, i), (1, i), (2, i)]

        # Revisar diagonal principal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return [(0, 0), (1, 1), (2, 2)]

        # Revisar diagonal secundaria
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return [(0, 2), (1, 1), (2, 0)]

        return None

    def highlight_winner(self, positions):
        """
        Cambia el color de fondo de los botones ganadores.
        """
        for row, col in positions:
            self.buttons[row][col].config(bg="#4CAF50")

    def is_draw(self):
        """
        Verifica si todas las celdas están llenas sin ganador.
        """
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_game(self):
        """
        Reinicia el juego limpiando el tablero y restaurando valores iniciales.
        """
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False

        # Restablece la etiqueta del turno
        self.turn_label.config(text="Turno: X", fg="#00ff99")

        # Limpia todos los botones
        for row in self.buttons:
            for button in row:
                button.config(text="", bg="#2d2d44", fg="white")


# Punto de entrada del programa
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)  # Evita redimensionar la ventana
    game = TicTacToe(root)
    root.mainloop()  # Inicia el bucle principal de la interfaz