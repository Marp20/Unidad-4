from tkinter import *
from tkinter import ttk
from functools import partial
from Imaginario import Imaginario as NumeroImaginario



class CalculadoraImaginariaGUI:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Calculadora Imaginaria')

        self.numero1_real = StringVar()
        self.numero1_imaginario = StringVar()
        self.numero2_real = StringVar()
        self.numero2_imaginario = StringVar()
        self.resultado = StringVar()

        frame = ttk.Frame(self.ventana, padding="10")
        frame.grid()

        # Etiquetas
        ttk.Label(frame, text="Número 1:").grid(column=0, row=0, sticky=E)
        ttk.Label(frame, text="Número 2:").grid(column=0, row=1, sticky=E)
        ttk.Label(frame, text="Resultado:").grid(column=0, row=3, sticky=E)

        # Campos de entrada
        ttk.Entry(frame, width=5, textvariable=self.numero1_real).grid(column=1, row=0, sticky=W)
        ttk.Entry(frame, width=5, textvariable=self.numero1_imaginario).grid(column=2, row=0, sticky=W)
        ttk.Entry(frame, width=5, textvariable=self.numero2_real).grid(column=1, row=1, sticky=W)
        ttk.Entry(frame, width=5, textvariable=self.numero2_imaginario).grid(column=2, row=1, sticky=W)

        # Botones de operaciones
        ttk.Button(frame, text='+', command=self.suma).grid(column=0, row=2)
        ttk.Button(frame, text='-', command=self.resta).grid(column=1, row=2)
        ttk.Button(frame, text='*', command=self.multiplicacion).grid(column=2, row=2)
        ttk.Button(frame, text='/', command=self.division).grid(column=3, row=2)

        # Campo de resultado
        ttk.Entry(frame, width=10, textvariable=self.resultado, state='readonly').grid(column=1, row=3, columnspan=3, sticky=W)

        self.ventana.mainloop()

    def obtener_numeros(self):
        num1_real = int(self.numero1_real.get())
        num1_imaginario = int(self.numero1_imaginario.get())
        num2_real = int(self.numero2_real.get())
        num2_imaginario = int(self.numero2_imaginario.get())
        return NumeroImaginario(num1_real, num1_imaginario), NumeroImaginario(num2_real, num2_imaginario)

    def mostrar_resultado(self, resultado):
        self.resultado.set(str(resultado))

    def suma(self):
        num1, num2 = self.obtener_numeros()
        resultado = num1 + num2
        self.mostrar_resultado(resultado)

    def resta(self):
        num1, num2 = self.obtener_numeros()
        resultado = num1 - num2
        self.mostrar_resultado(resultado)

    def multiplicacion(self):
        num1, num2 = self.obtener_numeros()
        resultado = num1 * num2
        self.mostrar_resultado(resultado)

    def division(self):
        num1, num2 = self.obtener_numeros()
        resultado = num1 / num2
        self.mostrar_resultado(resultado)


calculadora = CalculadoraImaginariaGUI()
