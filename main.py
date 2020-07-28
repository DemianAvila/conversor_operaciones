from tkinter import *
from Equilibrio_parentesis import *
from Pre_pos import *
from Stacks import *

ventana= Tk()

err=Label(ventana)
err1=Label(ventana)
err2=Label(ventana)
err3=Label(ventana)
resultado_pre=Label(ventana)


#winfo_exist() retorna valor de informacion si la etiqueta existe o no
#la solucion para borrar un widget es declarardo de forma universal y destruirlo antes de que se ejecute el
#grid, de igual manera, se debe declarar como variable global
"""-----------------------------------instrucciones------------------------------"""
instrucciones=Label(ventana, text="Conversor de operaciones infijas a prefijas o posfijas")
ins1=Label(ventana, text="Operadores y simbolos validos:", fg="red")
ins2=Label(ventana, text="() \t +  \t - \t / \t * \t ^ \t 0.0")
ins3=Label(ventana, text="0-9 \t a-z \t A-Z")
ins4=Label(ventana, text="Numeros y terminos algebraicos, varios terminos algebraicos juntos, o terminos algebraicos a lado de un parentesis, se toman como mutiplicacion")
entrada=Entry(ventana, width=100)
"""-----------------------------------fin instrucciones-------------------------------"""

"""----------------------------------colocacion en pantalla instrucciones----------------------------------"""
instrucciones.grid(row=0, column=0)
ins1.grid(row=1, column=0)
ins2.grid(row=2, column=0)
ins3.grid(row=3, column=0)
ins4.grid(row=4, column=0)
entrada.grid(row=5, column=0)
"""----------------------------------fin colocacion en pantalla instrucciones----------------------------------"""

"""-----------------------------------inicio funcion prefija-------------------------------"""
def pre():
    prueba=Label(ventana, text=entrada.get())
    prueba.grid(row=8, column=0)
    contador_err=0
    if validador_operaciones(entrada.get())== False:
        global err
        err.destroy()
        err=Label(ventana, text="Se ha introducido un simbolo invalido, revise su operacion", fg="red")
        err.grid(row=9, column=0)
        contador_err+=1
    elif equilibrio_parentesis(entrada.get())==False:
        global err1
        err1.destroy()
        err1=Label(ventana, text="Incorrecta distribucion de parentesis, revise su operacion", fg="red")
        err1.grid(row=9, column=0)
        contador_err+=1
    elif op_s_op(entrada.get())==False:
        global err2
        err2.destroy()
        err2=Label(ventana, text="Incorrecta distribucion de operandos, revise su operacion", fg="red")
        err2.grid(row=9, column=0)
        contador_err+=1
    elif no_empty_par(entrada.get())==False:
        global err3
        err3.destroy()
        err3=Label(ventana, text="Se detectaron parentesis vacios, revise su operacion", fg="red")
        err3.grid(row=9, column=0)
        contador_err+=1

    if contador_err==0:
        global resultado_pre
        resultado_pre.destroy()
        resultado_pre=Label(ventana, text=prefija(entrada.get()))
        resultado_pre.grid(row=9, column=0)
"""-----------------------------------fin funcion prefija-------------------------------"""
"""-----------------------------------inicio funcion posfija-------------------------------"""
def pos():
    prueba=Label(ventana, text=entrada.get())
    prueba.grid(row=8, column=0)
    contador_err=0
    if validador_operaciones(entrada.get())== False:
        global err
        err.destroy()
        err=Label(ventana, text="Se ha introducido un simbolo invalido, revise su operacion", fg="red")
        err.grid(row=9, column=0)
        contador_err+=1
    elif equilibrio_parentesis(entrada.get())==False:
        global err1
        err1.destroy()
        err1=Label(ventana, text="Incorrecta distribucion de parentesis, revise su operacion", fg="red")
        err1.grid(row=9, column=0)
        contador_err+=1
    elif op_s_op(entrada.get())==False:
        global err2
        err2.destroy()
        err2=Label(ventana, text="Incorrecta distribucion de operandos, revise su operacion", fg="red")
        err2.grid(row=9, column=0)
        contador_err+=1
    elif no_empty_par(entrada.get())==False:
        global err3
        err3.destroy()
        err3=Label(ventana, text="Se detectaron parentesis vacios, revise su operacion", fg="red")
        err3.grid(row=9, column=0)
        contador_err+=1

    if contador_err==0:
        global resultado_pre
        resultado_pre.destroy()
        resultado_pre=Label(ventana, text=posfija(entrada.get()))
        resultado_pre.grid(row=9, column=0)
"""-----------------------------------fin funcion posfija-------------------------------"""


"""-------------------------------estableciendo botones-----------------------------"""
boton_pre=Button(ventana, text="Convertir a prefija", command=pre)
boton_pos=Button(ventana, text="Convertir a posfija", command=pos)
"""--------------------------------fin botones-----------------------------------------"""

"""-------------------------colocando botones en pantalla-------------------------------"""
boton_pos.grid(row=6, column=0)
boton_pre.grid(row=7, column=0)
"""-------------------------colocando botones en pantalla-------------------------------"""

ventana.mainloop()
