from tkinter import *
import time
#Clase tablero crea la app y realiza el tablero
class Tablero():
    #Matriz para las celdas
    matriz=[]
    def __init__(self):
        self.app=Tk()
        self.app.geometry("612x612")
        self.app.resizable(False,False)
        self.app.title("TaTeTi")
        for a in range(3):
            for b in range(3):
                new=Celda(self.app,a,b)
                Tablero.matriz.append(new)

#Clase celda maneja cada celda
class Celda():
    #Variable para saber quien juega x=0 Juega cruz / x=1 Juega circulo
    turn=0
    def __init__(self,app,row,column):
        self.canvas=Canvas(app,width=200,height=200,bg="black")
        self.canvas.bind("<Button-1>",self.xo)
        self.canvas.grid(row=row,column=column)
        self.drawed=0
        self.value="1"
        self.app=app

    def xo(self,event):
        if Celda.turn==0 and self.drawed==0:
            self.canvas.create_polygon(20,40,40,20,180,160,160,180,fill="#9f0e1f")
            self.canvas.create_polygon(180,40,40,180,20,160,160,20,fill="#9f0e1f")
            self.canvas.update_idletasks()
            self.drawed=1
            self.value="X"
            Celda.turn=1

        if Celda.turn==1 and self.drawed==0:
            self.canvas.create_oval(30,30,170,170,outline="#22587a",width=20)
            self.canvas.update_idletasks()
            self.drawed=1
            self.value="O"
            Celda.turn=0
        self.win()

    def win(self):
        m=Tablero.matriz
        #Fila sup
        if m[0].value!="1" and m[0].value==m[1].value==m[2].value:
            time.sleep(0.1)
            Frame(self.app,bg="").grid(row=0,column=0,rowspan=3,columnspan=3,sticky=W+E+N+S)
            Label(self.app,text="GANAN LAS "+m[0].value,font=["",30],bg="black",fg="#908f28").grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
        #Fila med
        if m[3].value!="1" and m[3].value==m[4].value==m[5].value:
            time.sleep(0.1)
            Frame(self.app,bg="").grid(row=0,column=0,rowspan=3,columnspan=3,sticky=W+E+N+S)
            Label(self.app,text="GANAN LAS "+m[3].value,font=["",30],bg="black",fg="#908f28").grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
        #Fila inf
        if m[6].value!="1" and m[6].value==m[7].value==m[8].value:
            time.sleep(0.1)
            Frame(self.app,bg="").grid(row=0,column=0,rowspan=3,columnspan=3,sticky=W+E+N+S)
            Label(self.app,text="GANAN LAS "+m[6].value,font=["",30],bg="black",fg="#908f28").grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
        #Columna izq
        if m[0].value!="1" and m[0].value==m[3].value==m[6].value:
            time.sleep(0.1)
            Frame(self.app,bg="").grid(row=0,column=0,rowspan=3,columnspan=3,sticky=W+E+N+S)
            Label(self.app,text="GANAN LAS "+m[0].value,font=["",30],bg="black",fg="#908f28").grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
        #Columna med
        if m[1].value!="1" and m[1].value==m[4].value==m[7].value:
            time.sleep(0.1)
            Frame(self.app,bg="").grid(row=0,column=0,rowspan=3,columnspan=3,sticky=W+E+N+S)
            Label(self.app,text="GANAN LAS "+m[1].value,font=["",30],bg="black",fg="#908f28").grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
        #Columna der
        if m[2].value!="1" and m[2].value==m[5].value==m[8].value:
            time.sleep(0.1)
            Frame(self.app,bg="").grid(row=0,column=0,rowspan=3,columnspan=3,sticky=W+E+N+S)
            Label(self.app,text="GANAN LAS "+m[2].value,font=["",30],bg="black",fg="#908f28").grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
        #Diagonal principal
        if m[0].value!="1" and m[0].value==m[4].value==m[8].value:
            time.sleep(0.1)
            Frame(self.app,bg="").grid(row=0,column=0,rowspan=3,columnspan=3,sticky=W+E+N+S)
            Label(self.app,text="GANAN LAS "+m[2].value,font=["",30],bg="black",fg="#908f28").grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
        #Diagonal secundaria
        if m[2].value!="1" and m[2].value==m[4].value==m[6].value:
            time.sleep(0.1)
            Frame(self.app,bg="").grid(row=0,column=0,rowspan=3,columnspan=3,sticky=W+E+N+S)
            Label(self.app,text="GANAN LAS "+m[2].value,font=["",50],bg="black",fg="#908f28").grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)
Tablero()
mainloop()
