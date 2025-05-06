
from tkinter import *
import math
from abc import ABC, abstractmethod

# --------- Clases y interfaz ---------

class Coloreado(ABC):
    @abstractmethod
    def colorear(self):
        pass

class Figura(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado

    def get_area(self):
        return self.lado ** 2

    def get_perimetro(self):
        return 4 * self.lado

    def colorear(self):
        return f"El cuadrado de color {self.color}."

class Circulo(Figura, Coloreado):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def get_area(self):
        return math.pi * self.radio ** 2

    def get_perimetro(self):
        return 2 * math.pi * self.radio

    def colorear(self):
        return f"El círculo de color {self.color}."


# --------- Funciones para la interfaz ---------

def calcular_cuadrado():
    try:
        color = entry_color.get()
        lado = float(entry_lado.get())
        cuadrado = Cuadrado(color, lado)
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, f"{cuadrado.colorear()}\n")
        resultado_text.insert(tk.END, f"Área: {cuadrado.get_area():.2f}\n")
        resultado_text.insert(tk.END, f"Perímetro: {cuadrado.get_perimetro():.2f}\n")
    except ValueError:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "¡Valores inválidos!")

def calcular_circulo():
    try:
        color = entry_color.get()
        radio = float(entry_radio.get())
        circulo = Circulo(color, radio)
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, f"{circulo.colorear()}\n")
        resultado_text.insert(tk.END, f"Área: {circulo.get_area():.2f}\n")
        resultado_text.insert(tk.END, f"Perímetro: {circulo.get_perimetro():.2f}\n")
    except ValueError:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "¡Valores inválidos!")

# --------- Crear ventana ---------

ventana= Tk()
ventana.title("Calculadora de Figuras")
ventana.geometry("500x400")
ventana.mainloop()

# --------- Componentes ---------

# Input para color
tk.Label(ventana, text="Color:").grid(row=0, column=0, padx=10, pady=5)
entry_color = tk.Entry(ventana)
entry_color.grid(row=0, column=1, padx=10, pady=5)

# Input para lado del cuadrado
tk.Label(ventana, text="Lado del cuadrado:").grid(row=1, column=0, padx=10, pady=5)
entry_lado = tk.Entry(ventana)
entry_lado.grid(row=1, column=1, padx=10, pady=5)

# Input para radio del círculo
