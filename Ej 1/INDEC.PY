import math
from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox

class CIPC(object):
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.columnconfigure(0, weight=1)
        self.__ventana.geometry('420x225')
        self.__ventana.rowconfigure(0, weight=1)
        self.__ventana.title('Calculador IPC')

        mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S), padx=10, pady=10)  # Agrega el padding deseado aquí
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
            
        self.__CantidadAl = StringVar()
        self.__CantidadVes = StringVar()
        self.__CantidadEdu = StringVar()
        self.CantidadAlEntry = ttk.Entry(mainframe, width=7, textvariable=self.__CantidadAl)
        self.CantidadAlEntry.grid(column=2, row=2, sticky=(W, E, N, S))
        self.CantidadVesEntry = ttk.Entry(mainframe, width=7, textvariable=self.__CantidadVes)
        self.CantidadVesEntry.grid(column=2, row=3, sticky=(W, E, N, S))
        self.CantidadEduEntry = ttk.Entry(mainframe, width=7, textvariable=self.__CantidadEdu)
        self.CantidadEduEntry.grid(column=2, row=4, sticky=(W, E, N, S))
        
        self.__PrecioBaseAl = StringVar()
        self.__PrecioBaseVes = StringVar()
        self.__PrecioBaseEdu = StringVar()
        self.PrecioBaseAlEntry = ttk.Entry(mainframe, width=7, textvariable=self.__PrecioBaseAl)
        self.PrecioBaseAlEntry.grid(column=3, row=2, sticky=(W, E, N, S))
        self.PrecioBaseVesEntry = ttk.Entry(mainframe, width=7, textvariable=self.__PrecioBaseVes)
        self.PrecioBaseVesEntry.grid(column=3, row=3, sticky=(W, E, N, S))
        self.PrecioBaseEduEntry = ttk.Entry(mainframe, width=7, textvariable=self.__PrecioBaseEdu)
        self.PrecioBaseEduEntry.grid(column=3, row=4, sticky=(W, E, N, S))
        
        self.__PrecioActualAl = StringVar()
        self.__PrecioActualVes = StringVar()
        self.__PrecioActualEdu = StringVar()
        self.PrecioActualAlEntry = ttk.Entry(mainframe, width=7, textvariable=self.__PrecioActualAl)
        self.PrecioActualAlEntry.grid(column=4, row=2, sticky=(W, E, N, S))
        self.PrecioActualVesEntry = ttk.Entry(mainframe, width=7, textvariable=self.__PrecioActualVes)
        self.PrecioActualVesEntry.grid(column=4, row=3, sticky=(W, E, N, S))
        self.PrecioActualEduEntry = ttk.Entry(mainframe, width=7, textvariable=self.__PrecioActualEdu)
        self.PrecioActualEduEntry.grid(column=4, row=4, sticky=(W, E, N, S))
        
        ttk.Label(mainframe, text='').grid(column=8, row=8)
        self.__resultadoIPC = StringVar()
        self.__resultadoIPC.set("XX.XX")
        ttk.Label(mainframe, text="IPC %").grid(column=1, row=9, sticky=(W))
        ttk.Label(mainframe, text="%").grid(column=3, row=9, sticky=(W))
        ttk.Label(mainframe, textvariable=self.__resultadoIPC).grid(column=2, row=9, sticky=(N,W,E,S))
        
        
        ttk.Label(mainframe, text='Item', padding=(5, 5, 5, 5)).grid(column=1, row=1, sticky=(W))
        ttk.Label(mainframe, text='Vestimenta', padding=(5, 5, 5, 5)).grid(column=1, row=2, sticky=(W))
        ttk.Label(mainframe, text='Alimentos', padding=(5, 5, 5, 5)).grid(column=1, row=3, sticky=(W))
        ttk.Label(mainframe, text='Educacion', padding=(5, 5, 5, 5)).grid(column=1, row=4, sticky=(W))
        ttk.Label(mainframe, text='Cantidad', padding=(5, 5, 5, 5)).grid(column=2, row=1, sticky=(E))
        ttk.Label(mainframe, text='Precio Anio Base', padding=(5, 5, 5, 5)).grid(column=3, row=1, sticky=(E))
        ttk.Label(mainframe, text='Precio Anio Actual', padding=(5, 5, 5, 5)).grid(column=4, row=1, sticky=(E))
        
        ttk.Label(mainframe, text='').grid(column=1, row=5)
        
        ttk.Button(mainframe,text='Salir', command=exit).grid(column=4, row=6)
        ttk.Button(mainframe, text='Calcular', command=self.calcular).grid(column=2, row=6, sticky=(W,E))
        self.__ventana.mainloop()

    def calcular(self):
        try:
            CA= (int(self.__CantidadAl.get())*float(self.__PrecioActualAl.get()))+(int(self.__CantidadVes.get())*float(self.__PrecioActualVes.get()))+(int(self.__CantidadEdu.get())*float(self.__PrecioActualEdu.get()))
            CB=(int(self.__CantidadAl.get())*float(self.__PrecioBaseAl.get()))+(int(self.__CantidadVes.get())*float(self.__PrecioBaseVes.get()))+(int(self.__CantidadEdu.get())*float(self.__PrecioBaseEdu.get()))
            IPC=(math.floor(CA)*100)/math.floor(CB)
            self.__resultadoIPC.set(IPC)
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
    
cipc = CIPC()