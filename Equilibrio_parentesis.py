from Stacks import *



alfabeto=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



nums=['0','1','2','3','4','5','6','7','8','9']

parentesis=['(', ')']

permitidos=['.']

operadores1=['^']
operadores2=['*', '/']
operadores3=['+', '-']



#verifica el equilibrio de los parentesis en una operacion

def equilibrio_parentesis (cadena):
    b=[]
    pila=Stack(b)

    for i in cadena:
        if i=='(':
            pila.push(i)

        elif i==')':
            if pila.is_empty()==True:
                return False
            else:
                pila.pop()

    if pila.is_empty()==True:
        return True
    else:
        return False

"""
print(equilibrio_parentesis('((35456))()'))
"""

#verifica que el usuario ho haya metido simbolos ajenos a los permitidos en aritmetica o algebra
def validador_operaciones(op):
    simbolos_validos=[]
    for i in op:
        for j in alfabeto:
            if i==j:
                simbolos_validos.append(True)


    for i in op:
        for j in nums:
            if i==str(j):
                simbolos_validos.append(True)

    for i in op:
        for j in parentesis:
            if i==j:
                simbolos_validos.append(True)

    for i in op:
        for j in permitidos:
            if i==j:
                simbolos_validos.append(True)

    for i in op:
        for j in operadores1:
            if i==j:
                simbolos_validos.append(True)

    for i in op:
        for j in operadores2:
            if i==j:
                simbolos_validos.append(True)

    for i in op:
        for j in operadores3:
            if i==j:
                simbolos_validos.append(True)

    if (len(simbolos_validos))==len(op):
        return True
    else:
        return False

#----------------------Separador de operadores y operandos---------------#
#regresa una lista con los elementos separados

def separador (op):
    separados=[]
    operandos_operadores=[]
    #separa caracteres en una lista
    for i in op:
        separados.append(i)
    #agrupa los numeros de dos o mas digitos en una sola cadena
    operando = ''
    for j in range (len(separados)):
        if (separados[j] in nums)or(separados[j] in permitidos):
            if j==(len(separados)-1):
                operando=str(operando)+str(separados[j])
                operandos_operadores.append(operando)
            else:
                operando=str(operando)+str(separados[j])
        elif (separados[j] not in nums):
            if operando!='':
                operandos_operadores.append(operando)
                operandos_operadores.append(separados[j])
                operando = ''
            elif operando=='':
                operandos_operadores.append(separados[j])


    #Numeros y terminos algebraicos juntos se toman como multiplicacion
    lista_fin=[]
    for k in range (len(operandos_operadores)):
        if k+1<len(operandos_operadores):
            if (operandos_operadores[k][0] in nums) or (operandos_operadores[k][0] in permitidos):
                if operandos_operadores[k+1][0] in alfabeto:
                    lista_fin.append(operandos_operadores[k])
                    lista_fin.append('*')
                else:
                    lista_fin.append(operandos_operadores[k])

            elif operandos_operadores[k][0] in alfabeto:
                if (operandos_operadores[k+1][0] in nums) or (operandos_operadores[k+1][0] in permitidos):
                    lista_fin.append(operandos_operadores[k])
                    lista_fin.append('*')
                elif operandos_operadores[k+1][0] in alfabeto:
                    lista_fin.append(operandos_operadores[k])
                    lista_fin.append('*')
                else:
                    lista_fin.append(operandos_operadores[k])

            else:
                lista_fin.append(operandos_operadores[k])

        elif k+1==len(operandos_operadores):
            lista_fin.append(operandos_operadores[-1])
    return lista_fin


#-----------------------detecta si hay un operador sin operando---------
#-----------genera un error-----------------
#-----------------------op_s_op--------------
#-----'operador sin operando'-------------------

"""
toma la lista anterior y si cada operador tiene un operando
a la izquiera y a la derecha
regresa true, si no, false

on operando puede ser un parentesis de entrada o de salida,
una letra o un numero
"""

def op_s_op(cadena):
    rectificadora=[]
    num_operadores=[]
    for i in range (len(cadena)):
        if (cadena[0] in operadores1)or(cadena[0] in operadores2):
            """si la cadena empieza con un operador de multiplicacion,
            , division o potencia
            /6, por ejemplo, quiere decir que hay operadores sin opreandos
            por lo tanto, no esta equilibrada"""
            return False
        elif (cadena[-1] in operadores1)or(cadena[-1] in operadores2) or (cadena[-1] in operadores3):
            """si la cadena termina con un operador de multiplicacion,
            , division ,potencias suma o resta
            6-, por ejemplo, quiere decir que hay operadores sin opreandos
            por lo tanto, no esta equilibrada"""
            return False
        else:
            if (i==0) or (i==(len(cadena)-1)): pass #omite el primer y ultimo lugar de la lista
            elif (cadena[i] in operadores1)or(cadena[i] in operadores2) or (cadena[i] in operadores3):
                #cada vez que se encuentra un operador, añade un valor
                num_operadores.append(True)
                if (cadena[i-1][0] in nums) or (cadena[i-1] in alfabeto) or (cadena[i-1] in parentesis):
                    #Si antes del operador...
                    if (cadena[i+1][0] in nums) or (cadena[i+1] in alfabeto) or (cadena[i+1] in parentesis):
                        #y despues del operador hay un operando
                        #añade un valor a rectificadora
                        rectificadora.append(True)
    #si al final del ciclo, los numeros en rectificadora y en num_operadores es igual, regresa verdadero
    if len(rectificadora)==len(num_operadores):
        return True
    else:
        return False


#----------------verificar que no hay parentesis vacios-----------------
def no_empty_par(cadena):
    if equilibrio_parentesis(cadena)==True:
        for i in range (len(cadena)):
            if i<(len(cadena)-1):
                if (cadena[i]=='(') and (cadena[i+1]==')'):
                    return False
        return True
    else: return False
