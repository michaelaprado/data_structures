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
    def delete_first(self): 
        if(self.head == None):
            print("nothing can be deleted")
        elif(lista.head.next == None):
            self.head = None
        else:
            a = self.head #assing head to a
            self.head = self.head.next 
            a = None
    def count(self):
        i = 0 #declaring i
        a = self.head
        while(a != None):
            i = i+1
            a = a.next
        return i
    def delete_last(self):
        if (self.head == None):
            print("No se puede borrar")
        elif (self.head.next == None):
            self.head = None
        else:
            a = self.head
            while(a.next.next != None):
                a = a.next
            a.next = None 
            return
    def get(self,indexn):
        a = self.head
        i = 0
        while(i < indexn):
            i = i+1
            a = a.next
            if (a == None):
                return
        return a.value
    def find(self, valor):
        a = self.head
        if(a == None):
            return -1
        i = 0
        while(a.value != valor):
            i = i+1
            a = a.next
            if(a == None):
                return -1
        return i
    def addAt(self, indexn, value):
        new_node = Node(value)
        a = self.head
        i = 0
        if (a == None):
            print("no se puede añadir")
            return
        if(indexn == 0):
           new_node.next = a
           self.head = new_node
           return
        while(i < (indexn-1)):
            i = i + 1
            a = a.next
            if(a == None):
                print("no se puede añadir")
                return 
        new_node.next = a.next
        a.next = new_node
    def deleteAt(self, indexn):
        a = self.head
        i = 0
        if(a == None):
            print("no se puede borrar")
            return
        if(indexn == 0):
            self.head = a.next
            return 
        while(i < (indexn-1)):
            i = i+1
            a = a.next
            if (a.next == None):
                print("no se puede borrar")
                return
        a.next = a.next.next
lista = LinkedList()
lista.addAt(0, 6)
lista.print_nodes()



