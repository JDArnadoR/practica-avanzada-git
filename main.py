import tkinter as tk
from tkinter import messagebox


def procesar_texto():
    texto = entrada.get().strip()
    
    if not texto:
        messagebox.showwarning("Advertencia", "Por favor, escribe algo.")
        return
    
    resultado.set(f"Hola, {texto} 👋")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación Básica con Tkinter")
ventana.geometry("400x200")
ventana.resizable(False, False)

# Variable para el resultado
resultado = tk.StringVar()

# Widgets
titulo = tk.Label(ventana, text="Ingresa tu nombre:", font=("Arial", 12))
titulo.pack(pady=10)

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

boton = tk.Button(ventana, text="Saludar", command=procesar_texto)
boton.pack(pady=10)

label_resultado = tk.Label(ventana, textvariable=resultado, font=("Arial", 12), fg="blue")
label_resultado.pack(pady=5)

# Ejecutar aplicación
ventana.mainloop()