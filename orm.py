import tkinter as tk
import random
import math
import json


personas=[]


class Persona:
    def __init__(self):
        self.posx=random.randint(0,768)
        self.posy=random.randint(0,768)
        self.largo=10
        self.direccion=random.randint(0,360)
        self.color=self.colorRandom()
        self.objeto=""
        
    #crear colores aleatorios    
    def colorRandom(self):
         r=random.randint(0,255)
         g=random.randint(0,255)
         b=random.randint(0,255)
         hexadecimal="#{:02x}{:02x}{:02x}".format(r,g,b)
         return hexadecimal
    
    def dibujar (self):
        self.objeto=lienzo.create_rectangle(
            self.posx-self.largo/2,
            self.posy-self.largo/2,
            self.posx+self.largo/2,
            self.posy+self.largo/2,
            fill=self.color
        )

    def mover(self):
        lienzo.move(
             self.objeto,
             math.cos(self.direccion),
             math.sin(self.direccion)
             )
        self.paredes()
        #actualizar posicion del objeto
        self.posx+=math.cos(self.direccion)
        self.posy+=math.sin(self.direccion)


    #rebotar paredes de la ventana
    def paredes(self):
         if self.posx < 0 or self.posx>768 or self.posy<0 or self.posy>768:
              self.direccion+=math.pi

    def creaDiccionario(self):
        return {
            'posicionX':self.posx,
            'posicionY':self.posy,
            'largo':self.largo,
            'direccion':self.direccion,
            'color':self.color,
            'numeroPersona':self.objeto
        }
        



def guardarEstado():
    print("guardado")
    datosJugadores = [persona.creaDiccionario() for persona in personas]
    cadena=json.dumps(datosJugadores)
    with open("jugadores.json",'w') as archivo:
        archivo.write(cadena)

raiz=tk.Tk()

lienzo=tk.Canvas(raiz,width=768,height=768)
lienzo.pack()

boton=tk.Button(raiz,text="guardar",command=guardarEstado)
boton.pack()

#cargar personas desde el json guardado anterior
try:
    carga=open("jugadores.json",'r')
    cargador=carga.read()
    cargadorLista=json.loads(cargador)
    for elemento in cargadorLista:
        persona=Persona()
        persona.__dict__.update(elemento)
        personas.append(persona)
except:
     print("error")


#introduzco personas en la colección
if len(personas)==0:
    numeroPersonas=25
    for i in range (0, numeroPersonas):
        personas.append(Persona())


#para cada persona en colección las muestro en pantalla
for persona in personas:
    persona.dibujar()


#bucle para mover cada persona en colección
def bucle():
        for persona in personas:
            persona.mover()
        raiz.after(10,bucle)

bucle()



persona=Persona()
persona.dibujar()
raiz.mainloop()