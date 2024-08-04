import tkinter as tk
import customtkinter 

global xboton
global numeroVariable
xboton = 195
numeroVariable = 2

def agregar_entrada_variable_funcionObjetivo(x,y):
    nueva_barra_entrada = customtkinter.CTkEntry(master=funcionObjetivo,width=26,height=26)
    nueva_barra_entrada.place(x= x,y= y)

    return nueva_barra_entrada

def agregar_texto_variable_funcionObjetivo(x,y,numero):
    nueva_variable = customtkinter.CTkLabel(master=funcionObjetivo,text='X'+str(numero),font=('Bold',16))
    nueva_variable.place(x=x+25,y=y)
    global numeroVariable
    numeroVariable = numero + 1

    return nueva_variable

def agregar_suma_funcionObjetivo(x,y):
    suma = customtkinter.CTkLabel(master=funcionObjetivo,text='+',font=('Bold',16),text_color='#D02323')
    suma.place(x=x+50,y=y)

    return suma

def agregar_variable_funcionObjetivo(x,y,numero):
    if (numero < 11):
        global xboton
        xboton = x + 65
        agregar_entrada_variable_funcionObjetivo(x,y)
        agregar_texto_variable_funcionObjetivo(x,y,numero)
        agregar_suma_funcionObjetivo(x-65,y)
        botonAgregarVariable.place(x=xboton,y=5)
        print(xboton)
    else:
        ventanaAlerta = customtkinter.CTkToplevel()
        ventanaAlerta.title('No puedes agregar mas variables :(')

ventana = customtkinter.CTk()
ventana.configure(fg_color='#FAFBF6')
ventana.title('METODO SIMPLEX')
ventana.geometry('1133x695')
ventana.resizable(width=True,height=True)
#--------------------------------------------------------------Frames------------------------------------------------------------------------------
hoja = customtkinter.CTkFrame(master=ventana,width=1118,height=674,corner_radius=62,fg_color='#FAFBF6',border_width=1.5,border_color='#0099DB')
hoja.place(x=8,y=10)
funcionObjetivo = customtkinter.CTkFrame(master=hoja,width=1075,height=41,fg_color='#FAFBF6',border_width=1.5,border_color='black')
funcionObjetivo.place(x=21,y=80)
restricciones = customtkinter.CTkFrame(master=hoja,width=537.5,height=487,fg_color='#FAFBF6',border_width=1.5,border_color='black')
restricciones.place(x=21,y=132)
estandarizacion = customtkinter.CTkFrame(master=hoja,width=537.5,height=487,fg_color='#FAFBF6',border_width=1.5,border_color='black')
estandarizacion.place(x=560,y=132)
#-------------------------------------------------------------Textos-----------------------------------------------
tituloHoja = customtkinter.CTkLabel(master=hoja,text='MÉTODO SIMPLEX',font=('Bold',20))
tituloHoja.place(x=467,y=12)
tituloFuncionObejito = customtkinter.CTkLabel(master=funcionObjetivo,text='Fob =',font=('Bold',20))
tituloFuncionObejito.place(x=5,y=5)
tituloRestricciones = customtkinter.CTkLabel(master=restricciones,text='Sujeto a:',font=('Bold',16))
tituloRestricciones.place(x=15,y=2)
tituloEstandarizacion = customtkinter.CTkLabel(master=estandarizacion,text='Estandarización:',font=('Bold',16))
tituloEstandarizacion.place(x=15,y=2)
#---------------------------------------------------------------Botones----------------------------------------------------------------------------
botonEstandarizar = customtkinter.CTkButton(master=ventana,width=285,height=33,fg_color='#63C74D',border_color='#63C74D',border_width=1.2,text_color='#FAFBF6',font=('Bold',20),text='Estandarizar')
botonEstandarizar.place(x=147,y=643)
botonResolver = customtkinter.CTkButton(master=ventana,width=285,height=33,fg_color='#63C74D',border_color='#63C74D',border_width=1.2,text_color='#FAFBF6',font=('Bold',20),text='Resolver')
botonResolver.place(x=721,y=643)
botonAgregarRestriccion = customtkinter.CTkButton(master=restricciones,width=157,height=23,fg_color='#FE8C42',border_color='#FE8C42',border_width=1.2,text_color='#FAFBF6',font=('Bold',15),text='Agregar restricción')
botonAgregarRestriccion.place(x=15,y=55)
botonAgregarVariable= customtkinter.CTkButton(master=funcionObjetivo,width=10,height=4,border_spacing=0,fg_color='#63C74D',border_color='#63C74D',border_width=1.2,text_color='#FAFBF6',font=('Bold',22),text='+',command=lambda:agregar_variable_funcionObjetivo(xboton,5,numeroVariable))
botonAgregarVariable.place(x=xboton,y=5)

entradasFuncionObjetivo = []
variablesFuncionObjetivo = []
sumasFuncionObjetivo = []

entradasFuncionObjetivo.append(agregar_entrada_variable_funcionObjetivo(60,5))
entradasFuncionObjetivo.append(agregar_entrada_variable_funcionObjetivo(125,5))
variablesFuncionObjetivo.append(agregar_texto_variable_funcionObjetivo(60,5,1))
variablesFuncionObjetivo.append(agregar_texto_variable_funcionObjetivo(125,5,2))
sumasFuncionObjetivo.append(agregar_suma_funcionObjetivo(60,5))

ventana.mainloop()
