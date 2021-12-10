# Estuardo Sebastián Valle Bances 
# 202001954

#Ejercicio 1 (Clase General)
class PhoneData: 
    def __init__(self, name, number): 
        self.name = name
        self.number = number

class Node: 
    def __init__ (self, nombre,numero, next): 
        self.nombre = nombre
        self.numero = numero
        self.next = next 

class guiaTelefonica: 
    def __init__ (self): 
        self.head = None 
    def ingresarNumero(self, nombre, numero): 
        if self.head == None: 
            nuevo_nodo = Node(nombre, numero, None)
            self.head = nuevo_nodo
            return 
        curr = self.head
        while curr.next: 
            curr = curr.next
        curr.next = Node(nombre, numero, None)

    def print_list(self): 
        n = self.head
        while n != None: 
            
            print(n.nombre + n.numero, end = "\n")
            n = n.next
        print()

lista = guiaTelefonica()
while True: 
    numeroTel = input("Ingrese un numero de Telefono")
    nombreTel = input("Ingrese un nombre ")

    nuevoNodo = Node(nombreTel, numeroTel, None)
    lista.ingresarNumero(nombreTel, numeroTel)
    print("Su lista actual es la siguiente: ")
    lista.print_list() 
    



