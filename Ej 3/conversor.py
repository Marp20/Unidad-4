from tkinter import *
from tkinter import ttk, messagebox


class Conversor(object):
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Conversor de moneda')
        self.__ventana.geometry('420x225+200+200')
        
        mainframe= ttk.Frame(self.__ventana, relief='sunken', borderwidth=5, height='115', width='310').place(x=0,y=0)
        
        self.__moneda = StringVar()
        self.__moneda = ttk.Entry(mainframe, width=10)
        self.__moneda.place(x=125,y=25)
        self.__moneda.bind('<KeyRelease>', self.calculo)
        ttk.Label(mainframe, text='dolares',font=('Calibri', 11)).place(x=200, y= 28)
        ttk.Label(mainframe, text='es equivalente a',font=('Calibri', 11)).place(x=20,y=50)
        self.__resultado= StringVar()
        ttk.Label(mainframe,textvariable=self.__resultado, font=('Calibri', 11)).place(x=130, y= 50)
        ttk.Label(mainframe, text='pesos', font=('Calibri', 11)).place(x=200, y= 50)
        
        ttk.Button(mainframe, text='Salir', command=exit).place(x=200, y=80)
        
        self.__ventana.mainloop()
    
    def calculo(self, event):
        try:
            key = event.char
            if key.isdigit() or (key == '' and self.__moneda.get()):
                resultado = int(self.__moneda.get()) * 144
                self.__resultado.set(resultado)
        except:
            None
        
conv = Conversor()
