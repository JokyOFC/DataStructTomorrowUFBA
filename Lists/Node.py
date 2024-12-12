class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def getValue(self):
        return self.value

    def setValue(self, value):
        self.dado = value
    
    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

class ListaEncadeada:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        atual = self.head

        while(atual.getNext() is not None):
            atual = atual.getNext()
        
        atual.setNext(node)
    
    def __str__(self):
        text = ""

        current = self.head

        while(current is not None):
            text += f"{current.getValue()} -> "
            current = current.getNext()
        
        text += "None"
        return text