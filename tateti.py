from tkinter import *
from tkinter import messagebox

#Funcion para cambiar la imagen de un label
def changeimage(label,path):
    image=PhotoImage(file=path)
    label.configure(image=image)
    label.image=image

#Ventana principal
class Container(Tk):
    def __init__(self,**kwargs):
        super(Container,self).__init__(**kwargs)
        img=Image("photo",file="X.png") #Imagen para icono
        self.call('wm','iconphoto',self._w,img) #Icono de la ventana
        self.geometry("540x540+%i+%i"%(self.winfo_screenwidth()/2-277,self.winfo_screenheight()/2-277)) #Tamaño y posición inicial
        self.update_idletasks() #Actualiza la posición de la ventana
        self.title("TaTeTi") #Tìtulo
        self.configure(bg="#0d292f") #Fondo de la lìneas
        self.minsize(540,540) #Tamaño mìnimo
        #Configurar las filas y columnas para que se ajusten al tamaño de la ventana
        for row in range(3):
            self.rowconfigure(row,weight=1)
        for column in range(3):
            self.columnconfigure(column,weight=1)

        self.tablero()
    #Crea un tablero e iniciar turno
    def tablero(self):
        self.matriz=[] #Matriz para las celdas
        self.turn=0 #Variable para saber quien juega / 0 Juega cruz / 1 Juega circulo /
        #Crear tablero
        for row in range(3):
            for column in range(3):
                new=Celda()
                new.grid(row=row,column=column,sticky="wens",pady=1,padx=1)
                self.matriz.append(new)

class Celda(Label):
    def __init__(self,**kwargs):
        super(Celda,self).__init__(**kwargs)
        self.configure(bg="black") #Fondo negro
        changeimage(self,"None.png") #Imagen inicial en negro
        self.bind("<Button-1>",self.xo) #Enlaza el click izquierdo al evento de control
        self.drawed=0 #Controla si la casilla esta dibujada
        self.value=0 #Valor X u O

    #Evento de control
    def xo(self,event):
        if self.master.turn == 0 and self.drawed == 0: #En turno de las X y se aprieta en casilla sin dibujar
            changeimage(self,"X.png") #Cambiar imagen
            self.drawed=1 #La casilla pasa a estar dibujada
            self.value="X" #Cambia su valor
            self.master.turn=1 #Cambia a el turno de las O
            self.win() #Comprobar victoria
        if self.master.turn == 1 and self.drawed == 0: #En turno de las O y se aprieta en casilla sin dibujar
            changeimage(self,"O.png") #Cambiar imagen
            self.drawed=1 #La casilla pasa a estar dibujada
            self.value="O" #Cambia su valor
            self.master.turn=0 #Cambia a el turno de las X
            self.win() #Comprobar victoria

    #Controla si gana alguien
    def win(self):
        m=self.master.matriz
        #Fila sup
        if m[0].value!=0 and m[0].value == m[1].value == m[2].value:
            self.end(m[0].value)
        #Fila med
        if m[3].value!=0 and m[3].value == m[4].value == m[5].value:
            self.end(m[3].value)
        #Fila inf
        if m[6].value!=0 and m[6].value == m[7].value == m[8].value:
            self.end(m[6].value)
        #Columna izq
        if m[0].value!=0 and m[0].value == m[3].value == m[6].value:
            self.end(m[0].value)
        #Columna med
        if m[1].value!=0 and m[1].value == m[4].value == m[7].value:
            self.end(m[1].value)
        #Columna der
        if m[2].value!=0 and m[2].value == m[5].value == m[8].value:
            self.end(m[2].value)
        #Diagonal principal
        if m[0].value!=0 and m[0].value == m[4].value == m[8].value:
            self.end(m[0].value)
        #Diagonal secundaria
        if m[2].value!=0 and m[2].value == m[4].value == m[6].value:
            self.end(m[2].value)
        #Empate
        if m[0].drawed==m[1].drawed==m[2].drawed==m[3].drawed==m[4].drawed==m[5].drawed==m[6].drawed==m[7].drawed==m[8].drawed==1:
            self.end("draw")

    #Genera los mensajes cuando se termina la partida
    def end(self,winner):
        if winner=="draw":
            message=messagebox.askokcancel("EMPATE","¡EMPATE!\n¿Volver a jugar?")
        else:
            message=messagebox.askokcancel("GANAN LAS "+winner,"¡GANAN LAS "+winner+"!\n¿Volver a jugar?")
        if message: #Destruir todo y crear nuevo tablero
            for celda in self.master.matriz:
                celda.destroy()
            self.master.tablero()
        else: #Salir
            self.master.quit()

Container()
mainloop()
