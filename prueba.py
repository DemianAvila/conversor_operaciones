
alfabeto=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



nums=['0','1','2','3','4','5','6','7','8','9']

parentesis=('(', ')')

permitidos=['.']

operadores1=['^']
operadores2=['*', '/']
operadores3=['+', '-']






def op_s_op(cadena):
    rectificadora=[]
    num_operadores=[]
    for i in range (len(cadena)):
        if (cadena[0] in operadores1)or(cadena[0] in operadores2):
            """si la cadena empieza con un operador de multiplicacion,
            , division o potencia
            /6, por ejemplo, quiere decir que hay operadores sin opreandos
            por lo tanto, no esta equilibrada"""
            print('falso1'+','.join(cadena))
        elif (cadena[-1] in operadores1)or(cadena[-1] in operadores2) or (cadena[-1] in operadores3):
            """si la cadena termina con un operador de multiplicacion,
            , division ,potencias suma o resta
            6-, por ejemplo, quiere decir que hay operadores sin opreandos
            por lo tanto, no esta equilibrada"""
            print('falso2'+','.join(cadena))
        else:
            if (i==(len(cadena)-1)): pass #omite el primer y ultimo lugar de la lista
            elif (cadena[i] in operadores1)or(cadena[i] in operadores2) or (cadena[i] in operadores3):
                #cada vez que se encuentra un operador, añade un valor
                num_operadores.append(True)
                if (cadena[i-1] in nums) or (cadena[i-1] in alfabeto) or (cadena[i-1] in parentesis):
                    #Si antes del operador...
                    if (cadena[i+1] in nums) or (cadena[i+1] in alfabeto) or (cadena[i+1] in parentesis):
                        #y despues del operador hay un operando
                        #añade un valor a rectificadora
                        rectificadora.append(True)
    #si al final del ciclo, los numeros en rectificadora y en num_operadores es igual, regresa verdadero
    if len(rectificadora)==len(num_operadores):
        print('verd'+','.join(cadena))
    else:
        print('falso3'+','.join(cadena))
        print(f'rect {rectificadora}')
        print(f'op {num_operadores}')

op_s_op(['12','+','w'])

