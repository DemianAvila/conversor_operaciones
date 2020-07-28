from Equilibrio_parentesis import *
from Stacks import *

def posfija (cadena):
    pila=Stack([])
    arreglo=[]
    for a in cadena:
        if a ==parentesis[0]:
            #un parentesis de apertura entra a la pila
            pila.push(a)

        elif (a in alfabeto) or (a[0] in nums):
            #un numero o variable entran directo al arreglo
            arreglo.append(a)

        elif a==parentesis[1]:
            """cuando aparece un parentesis de cierre,
            saca cada operador de la pila y
            aniadelo al arreglo hasta que aparezca un
            parentesis de apertura"""
            while pila.top()!='(' :
                arreglo.append(pila.top())
                pila.pop()
            pila.pop()

        elif a in operadores1:
            #el operador de mas alta precedencia se aniade a la pila
            pila.push(a)

        elif a in operadores2:
            #si es de mas alta precedencia que el ultimo de la pila se agrega
            if (pila.top() in operadores3):
                pila.push(a)
            #si es de mas baja precedencia, que el ultimo de la pila, saca a todos los anteriores y metelos al arreglo
            elif (pila.top() in operadores1):
                while (pila.top() in operadores1):
                    arreglo.append(pila.top())
                    pila.pop()
                pila.push(a)
            #si son de la misma precedencia, saca al anterior, metelo al arrego y mete al operador en la pila
            elif (pila.top() in operadores2):
                arreglo.append(pila.top())
                pila.pop()
                pila.push(a)

            elif (pila.is_empty()) or (pila.top()=='('):
                pila.push(a)

        elif a in operadores3:
            #si son de menor precedencia, saca a los anteriores y metelos al arreglo, añade el operador a la pila
            if (pila.top() in operadores1) or (pila.top() in operadores2):
                while (pila.top() in operadores1) or (pila.top() in operadores2):
                    arreglo.append(pila.top())
                    pila.pop()
                pila.push(a)
            #si son de la misma precedencia, saca al anterior, metelo al arrego y mete al operador en la pila
            elif (pila.top() in operadores3):
                arreglo.append(pila.top())
                pila.pop()
                pila.push(a)

            elif (pila.is_empty())or (pila.top()=='('):
                pila.push(a)


    #si al final, se ha terminado de recorrer el arreglo, y la pila no esta vacia, ve agregando
    #todos operadores con protocolo lifo al arreglo
    if pila.is_empty()==False:
        while pila.is_empty()==False:
            arreglo.append(pila.top())
            pila.pop()

    return arreglo


def prefija (cadena_invertible):
    cadena=[]
    for i in range (-1, ((len(cadena_invertible)*(-1))-1), -1):
        cadena.append(cadena_invertible[i])

    pila=Stack([])
    arreglo=[]
    for a in cadena:
        if a ==parentesis[1]:
            #un parentesis de apertura entra a la pila
            pila.push(a)

        elif (a in alfabeto) or (a[0] in nums):
            #un numero o variable entran directo al arreglo
            arreglo.append(a)

        elif a==parentesis[0]:
            """cuando aparece un parentesis de cierre,
            saca cada operador de la pila y
            aniadelo al arreglo hasta que aparezca un
            parentesis de apertura"""
            while pila.top()!=')' :
                arreglo.append(pila.top())
                pila.pop()
            pila.pop()

        elif a in operadores1:
            #el operador de mas alta precedencia se aniade a la pila
            pila.push(a)

        elif a in operadores2:
            #si es de mas alta precedencia que el ultimo de la pila se agrega
            if (pila.top() in operadores3):
                pila.push(a)
            #si es de mas baja precedencia, que el ultimo de la pila, saca a todos los anteriores y metelos al arreglo
            elif (pila.top() in operadores1):
                while (pila.top() in operadores1):
                    arreglo.append(pila.top())
                    pila.pop()
                pila.push(a)
            #si son de la misma precedencia, saca al anterior, metelo al arrego y mete al operador en la pila
            elif (pila.top() in operadores2):
                arreglo.append(pila.top())
                pila.pop()
                pila.push(a)

            elif (pila.is_empty()) or (pila.top()==')'):
                pila.push(a)

        elif a in operadores3:
            #si son de menor precedencia, saca a los anteriores y metelos al arreglo, añade el operador a la pila
            if (pila.top() in operadores1) or (pila.top() in operadores2):
                while (pila.top() in operadores1) or (pila.top() in operadores2):
                    arreglo.append(pila.top())
                    pila.pop()
                pila.push(a)
            #si son de la misma precedencia, saca al anterior, metelo al arrego y mete al operador en la pila
            elif (pila.top() in operadores3):
                arreglo.append(pila.top())
                pila.pop()
                pila.push(a)

            elif (pila.is_empty())or (pila.top()==')'):
                pila.push(a)


    #si al final, se ha terminado de recorrer el arreglo, y la pila no esta vacia, ve agregando
    #todos operadores con protocolo lifo al arreglo
    if pila.is_empty()==False:
        while pila.is_empty()==False:
            arreglo.append(pila.top())
            pila.pop()

    arreglo_inv=[]

    for j in range (-1, (((len(arreglo))*(-1))-1), -1):
        arreglo_inv.append(arreglo[j])

    return arreglo_inv
