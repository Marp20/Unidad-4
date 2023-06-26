from tkinter import *
from tkinter import ttk, messagebox


class IVA(object):
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Calculador IVA')
        self.__ventana.geometry('320x325+200+200')
        self.__ventana.overrideredirect(True)

        color_row = Frame(self.__ventana, bg="#A1D7FF")
        color_row.place(width=325, height=50)
        ttk.Label(color_row, text="Calculo de Iva", background="#A1D7FF",font='Calibri' ).place(x=110,y=15)  
        
        frame_contenido = Frame(self.__ventana, bd=2, relief=SOLID)
        frame_contenido.place(height=275, width= 320, y=50)
        style=ttk.Style()
        style.configure('BotonC.TButton', background='Black',relief=SOLID, bd=2,foreground='green')
        ttk.Label(frame_contenido, text='Precio sin IVA', font=('Arial',10)).place(x=20, y= 35)
        ttk.Button(frame_contenido, text='Calculo',style='BotonC.TButton', command=self.calculo).place(x=25,y=220,height=30, width=90)  
        style.configure('BotonS.TButton',background='red',relief=SOLID,bd=2,foreground='red')
        ttk.Button(frame_contenido, style='BotonS.TButton',text='Salir',command=exit).place(x=200, y= 220, height=30, width=90)  
        
        style.configure('Label.TButton', background='Black',relief=SOLID, bd=2)
        self.__precio= StringVar()
        self.__precio= ttk.Entry(frame_contenido, style='Label.TButton', width=25, textvariable=self.__precio, justify=CENTER)
        self.__precio.place(x=140, y=35)
        self.__IVA= StringVar()
        ttk.Label(frame_contenido, width= 25, style='Label.TButton',textvariable=self.__IVA).place(x=140, y=140)
        self.__precioconiva= StringVar()
        ttk.Label(frame_contenido, width= 25, style='Label.TButton',textvariable=self.__precioconiva).place(x=140, y=180)
        
        ttk.Label(frame_contenido, text='IVA', font=('Arial',10)).place(x=60, y= 140)
        ttk.Label(frame_contenido, text='Precio con IVA', font=('Arial',10)).place(x=20, y= 180)
        
        
        self.__opcion_iva = StringVar()
        radio1 = ttk.Radiobutton(frame_contenido, text='IVA 25%', variable=self.__opcion_iva, value='0.25')
        radio1.place(x=40, y=80)
        radio2 = ttk.Radiobutton(frame_contenido, text='IVA 10.5%', variable=self.__opcion_iva, value='0.105')
        radio2.place(x=40, y=100)
        
        self.__ventana.mainloop()
    
    def calculo(self):
        try:
            print("Precio:", self.__precio.get())
            print("Opción IVA:", self.__opcion_iva.get())
            
            resultado = (float(self.__precio.get())) * float(self.__opcion_iva.get())
            preciocon = (float(self.__precio.get())) + resultado
            
            print("Resultado:", resultado)
            print("Precio con IVA:", preciocon)
            
            self.__IVA.set(resultado)
            self.__precioconiva.set(preciocon)
        except Exception as e:
            print("Error:", str(e))
            messagebox.showerror(title='Error inesperado', message='Ingrese valores numéricos')
            
iva = IVA()