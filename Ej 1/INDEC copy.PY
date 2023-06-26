import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class CIPC(object):
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.columnconfigure(0, weight=1)
        self.__ventana.geometry('420x225')
        self.__ventana.rowconfigure(0, weight=1)
        self.__ventana.title('Calculador IPC')

        mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S), padx=10, pady=10)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        items = ['Vestimenta', 'Alimentos', 'Educacion']
        cantidad_vars = []
        precio_base_vars = []
        precio_actual_vars = []

        for i, item in enumerate(items):
            cantidad_var = StringVar()
            precio_base_var = StringVar()
            precio_actual_var = StringVar()

            cantidad_entry = ttk.Entry(mainframe, width=7, textvariable=cantidad_var).grid(column=2, row=i + 2, sticky=(W, E, N, S))
            precio_base_entry = ttk.Entry(mainframe, width=7, textvariable=precio_base_var).grid(column=3, row=i + 2, sticky=(W, E, N, S))
            precio_actual_entry = ttk.Entry(mainframe, width=7, textvariable=precio_actual_var).grid(column=4, row=i + 2, sticky=(W, E, N, S))

            cantidad_vars.append(cantidad_var)
            precio_base_vars.append(precio_base_var)
            precio_actual_vars.append(precio_actual_var)

            ttk.Label(mainframe, text=item, padding=(5, 5, 5, 5)).grid(column=1, row=i + 2, sticky=(W))

        ttk.Label(mainframe, text='').grid(column=8, row=8)
        self.__resultadoIPC = StringVar()
        self.__resultadoIPC.set("XX.XX")
        ttk.Label(mainframe, text="IPC %").grid(column=1, row=9, sticky=(W))
        ttk.Label(mainframe, text="%").grid(column=3, row=9, sticky=(W))
        ttk.Label(mainframe, textvariable=self.__resultadoIPC).grid(column=2, row=9, sticky=(N, W, E, S))

        ttk.Label(mainframe, text='Item', padding=(5, 5, 5, 5)).grid(column=1, row=1, sticky=(W))
        ttk.Label(mainframe, text='Cantidad', padding=(5, 5, 5, 5)).grid(column=2, row=1, sticky=(E))
        ttk.Label(mainframe, text='Precio Anio Base', padding=(5, 5, 5, 5)).grid(column=3, row=1, sticky=(E))
        ttk.Label(mainframe, text='Precio Anio Actual', padding=(5, 5, 5, 5)).grid(column=4, row=1, sticky=(E))

        ttk.Label(mainframe, text='').grid(column=1, row=len(items) + 2)

        ttk.Button(mainframe, text='Salir', command=exit).grid(column=4, row=len(items) + 3)
        ttk.Button(mainframe, text='Calcular', command=lambda: self.calcular(cantidad_vars, precio_base_vars, precio_actual_vars)).grid(column=2, row=len(items) + 3, sticky=(W, E))

        self.__ventana.mainloop()

    def calcular(self, cantidad_vars, precio_base_vars, precio_actual_vars):
        try:
            CA = sum(int(cantidad_var.get()) * float(precio_actual_var.get()) for cantidad_var, precio_actual_var in zip(cantidad_vars, precio_actual_vars))
            CB = sum(int(cantidad_var.get()) * float(precio_base_var.get()) for cantidad_var, precio_base_var in zip(cantidad_vars, precio_base_vars))
            IPC = (math.floor(CA) * 100) / math.ceil(CB)
            self.__resultadoIPC.set(IPC)
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')

cipc = CIPC()
