class Stack:
    def __init__(self, lista):
        self.pila=list(lista)

    def is_empty(self):
        if (len(self.pila))==0:
            return True
        else:
            return False

    def to_string(self):
        if self.is_empty()==True:
            return 'Pila vacia'
        else:
            return self.pila

    def pop (self):
        if self.is_empty():
            print('No se puede borrar nada, la pila esta vacia')
        else:
            self.pila.pop()

    def push (self, dato):
        self.pila.append(dato)

    def clear_stack(self):
        if self.is_empty()==True:
            print('No se puede limpiar, pila vacia')
        else:
            self.pila=[]

    def get_elem (self,index):
        if self.is_empty()==True:
            return 'Pila vacia'

        elif index>=len(self.pila):
            return 'Elemento inexistente'

        else:
            return self.pila[index]

    def size (self):
        if self.is_empty()==True:
            return 0
        else:
            return len(self.pila)

    def top (self):
        if self.is_empty()==True:
            return 'Pila vacia'
        else:
            return self.pila[-1]



"""
a=[5,4,7,8,9,7]
b= []
pila=Stack(a)
print(pila.is_empty())
pila1=Stack(b)
print(pila1.is_empty())
print (pila.to_string())
print(pila1.to_string())
pila.pop()
pila1.pop()
print (pila.to_string())
print(pila1.to_string())
pila.push(3)
pila1.push('a')
print (pila.to_string())
print(pila1.to_string())
pila.pop()
pila1.pop()
print (pila.to_string())
print(pila1.to_string())
pila.clear_stack()
pila1.clear_stack()
print (pila.to_string())
print(pila1.to_string())
pila=Stack(a)
print (pila.to_string())
print (pila.get_elem(0))
print (pila.get_elem(5))
print (pila.get_elem(6))
print (pila.size())
print (pila.top())
"""
