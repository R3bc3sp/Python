from Tkinter import *

class Ventana(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Viajes de senderismo")
        self.geometry("400x550")
        self.marginLeft = 20
        self.marginLeftET = 125
        self.marginTopRB = 75
        self.marginTopCB = self.marginTopRB+150
        self.marginTopET = self.marginTopCB+175
        self.widthET = 40
        self.textStyle = "Courier 10 bold"
        self.createWidgets()
    
    def createWidgets(self):
        label_titulo = Label(self, font="Courier 22 bold", text="Viajes de Senderismo").place(x=20, y=20)
        
        opcion = StringVar()
        opcion.set('excursion1')  # No funciona
        opcion1 = Radiobutton(self, text="Excursion 1", font=self.textStyle, value='excursion1', variable=opcion).place(x=self.marginLeft, y=self.marginTopRB)
        opcion2 = Radiobutton(self, text="Excursion 2", font=self.textStyle, value='excursion2', variable=opcion).place(x=self.marginLeft, y=self.marginTopRB+30)
        opcion3 = Radiobutton(self, text="Excursion 3", font=self.textStyle, value='excursion3', variable=opcion).place(x=self.marginLeft, y=self.marginTopRB+60)
        opcion4 = Radiobutton(self, text="Excursion 4", font=self.textStyle, value='excursion4', variable=opcion).place(x=self.marginLeft, y=self.marginTopRB+90)
        
        checkvar1 = StringVar()
        checkvar2 = StringVar()
        checkvar3 = StringVar()
        checkvar4 = StringVar()
        checkvar5 = StringVar()
        
        check1 = Checkbutton(self, text="Linterna", font=self.textStyle, variable=checkvar1, onvalue="linterna", offvalue="").place(x=self.marginLeft, y=self.marginTopCB)
        check2 = Checkbutton(self, text="GPS", font=self.textStyle, variable=checkvar2, onvalue="gps", offvalue="").place(x=self.marginLeft, y=self.marginTopCB+30)
        check3 = Checkbutton(self, text="Mapa", font=self.textStyle, variable=checkvar3, onvalue="mapa", offvalue="").place(x=self.marginLeft, y=self.marginTopCB+60)
        check4 = Checkbutton(self, text="Cantimplora", font=self.textStyle, variable=checkvar3, onvalue="cantimplora", offvalue="").place(x=self.marginLeft, y=self.marginTopCB+90)
        check5 = Checkbutton(self, text="Crema Solar", font=self.textStyle, variable=checkvar3, onvalue="crema_solar", offvalue="").place(x=self.marginLeft, y=self.marginTopCB+120)
        
        sNombre = StringVar()
        sApellidos = StringVar()
        sDireccion = StringVar()
        sTelefono = StringVar()
        
        label_nombre = Label(self, text="Nombre", font=self.textStyle).place(x=self.marginLeft, y=self.marginTopET)
        label_apellidos = Label(self, text="Apellidos", font=self.textStyle).place(x=self.marginLeft, y=self.marginTopET+30)
        label_direccion = Label(self, text="Direccion", font=self.textStyle).place(x=self.marginLeft, y=self.marginTopET+60)
        label_telefono = Label(self, text="Telefono", font=self.textStyle).place(x=self.marginLeft, y=self.marginTopET+90)
        caja_nombre = Entry(self, textvariable=sNombre, width=self.widthET).place(x=self.marginLeftET, y=self.marginTopET)
        caja_apellidos = Entry(self, textvariable=sApellidos, width=self.widthET).place(x=self.marginLeftET, y=self.marginTopET+30)
        caja_direccion = Entry(self, textvariable=sNombre, width=self.widthET).place(x=self.marginLeftET, y=self.marginTopET+60)
        caja_telefono = Entry(self, textvariable=sApellidos, width=self.widthET).place(x=self.marginLeftET, y=self.marginTopET+90)
    
ventana = Ventana()
ventana.mainloop()