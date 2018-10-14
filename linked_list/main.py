class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self): #init se llama constructor
        self.head = None
    def add(self,value): #self es la referencia a la instancia
        if self.head == None: 
            self.head = Node(value)
        else:
            a = self.head
            while (a.next != None):
                a = a.next
            a.next = Node(value)
    def print_nodes(self):
        a = self.head # "=" significa apunta a si es un objeto
        while (a != None):
           print(a.value)
           a = a.next
    def add_at_first(self, value):
        nodo1 = Node(value)
        nodo1.next = self.head
        self.head = nodo1

lista = LinkedList()
lista.add(1)
lista.add(2)
lista.add(3)
lista.add_at_first(4)
lista.print_nodes()

