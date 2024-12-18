class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.first = None
        self.end = None

    def Enqueue(self, value):

        node = Node(value)
        
        if(self.end is None):
            self.first = node
            self.end = node
            return

        self.end.next = node
        self.end = node

    def Dequeue(self):
        
        if(self.first is None):
            return
        
        data = self.first.data
        self.first = self.first.next

        if(self.first is None):
            self.end = None

        return data
    
    
    def __str__(self):

        text = ""

        if self.first is None:
            text = "A fila está vazia"
            return

        text += f"First: {self.first} \nLast: {self.end} \n"

        current = self.first

        while current is not None:
            text += f"{current.data} -> "
            current = current.next
        
        text += "None"

        return text
    


# CRIA FILA
queue = Queue()

queue.Enqueue(1)
queue.Enqueue(2)
queue.Enqueue(3)

print(queue)