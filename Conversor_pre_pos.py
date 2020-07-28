from Equilibrio_parentesis import *
from Stacks import *
from Pre_pos import *

print('Conversor de operaciones infijas a prefijas o posfijas')
print('Operadores y simbolos validos:')
print('() \t +  \t - \t / \t * \t ^ \t 0.0')
print ('0-9 \t a-z \t A-Z')
print ('Numeros y terminos algebraicos, varios terminos algebraicos juntos, o terminos algebraicos a lado de un parentesis, se toman como mutiplicacion')

pos_pre=0
bandera=False
while (bandera==False) and ((pos_pre!=1) or (pos_pre!=2)):
    pos_pre= int(input('\n¿Desea converir a posfijas o prefijas?\n1.-Prefijas\t2.-Posfijas\n'))
    try:
        if pos_pre==1 or pos_pre==2:
            bandera=True
        else:
            print('Opcion equivocada')
            bandera=False
    except:
        print('Opcion equivocada')


operacion=input('Inserte operacion:\n')
filtro=separador(operacion)
while (validador_operaciones(operacion)== False) or (equilibrio_parentesis(operacion)==False) or (op_s_op(filtro)==False) or (no_empty_par(filtro)==False):
    if validador_operaciones(operacion)== False:
        print('Se ha introducido un simbolo invalido, revise su operacion')
    elif equilibrio_parentesis(operacion)==False:
        print('Incorrecta distribucion de parentesis, revise su operacion')
    elif op_s_op(filtro)==False:
        print('Incorrecta distribucion de operandos, revise su operacion')
    elif no_empty_par(filtro)==False:
        print('Se detectaron parentesis vacios, revise su operacion')
    operacion=input('Inserte operacion:\n')
    filtro=separador(operacion)


if pos_pre==1:
    print(prefija(filtro))
elif pos_pre==2:
    print(posfija(filtro))
