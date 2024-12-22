class SimpleLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class PriorityQueueNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class Vector:
    def __init__(self):
        self.size = 0
        self.max = 2
        self.itens = [None] * self.max

    def extend(self):
        newMax = self.max * 2
        newArray = [None] * newMax

        for i in range(self.size):
            newArray[i] = self.itens[i]

        self.itens = newArray
        self.max = newMax

    def push(self, item):
        if self.size == self.max:
            self.extend()
        
        self.itens[self.size] = item

        self.size += 1
    
    def pop(self):

        if self.size == 0:
            print("O vetor está vazio, não é possível remover itens.")
            return
        
        removedItem = self.itens[self.size - 1]
        self.itens[self.size - 1] = None
        self.size -= 1

        return removedItem
    
    def insert(self, item, index):
        
        if index < 0 or index > self.size:
            print("Índice fora do alcance!")
            return
        
        if self.size == self.max:
            print("Vetor cheio")
            return
        
        for i in range(self.size, index ,-1):
            self.itens[i] = self.itens[i - 1]

        self.itens[index] = item

        self.size +=1

    def show(self):
        if self.size == 0:
            print("O vetor está vazio!")
        else:
            print([self.itens[i] for i in range(self.size)])
        return
    
    def last(self):
        if self.size > 0:
            return self.itens[self.size - 1]
        
        print("O vetor está vazio!")
    
    def __len__(self):
        return self.size

class SimpleLinkedList:
    def __init__(self):
        self.start = None

    def push(self, data):
        node = SimpleLinkedListNode(data)

        if not self.start:
            self.start = node
        else:
            current = self.start
            while current.next:
                current = current.next
            current.next = node
    
    def remove(self, node):
        def __remove(node, parent):
            if parent :
                parent.next = node.next
            else :
                self.start = node.next

        current = self.start
        parent = None

        while current:
            if current == node :
                __remove(current, parent)
                return
            
            parent = current
            current = current.next

        print("Nó não encontrado na lista")
    
    def insert(self, data, position):
        node = SimpleLinkedListNode(data)

        if position == 0 :
            node.next = self.start
            self.start = node
            return

        current = self.start
        index = 0
        parent = None

        while current and index < position:
            parent = current
            current = current.next
            index += 1

        if index == position :
            node.next = current
            parent.next = node
        else :
            print("Posição inválida!")
    
    def show(self):
        if not self.start:
            print("A lista está vazia!")
            return

        current = self.start
        itens = Vector()

        while current:
            itens.push(current.data)
            current = current.next

        itens.show()

class StackVector:
    def __init__(self):
        self.stack = Vector()

    def push(self, elemento):
        self.stack.push(elemento)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        
        print("A pilha está vazia!")

    def peek(self):
        if not self.isEmpty():
            return self.stack.last()
        
        print("A pilha está vazia!")

    def clear(self):
        self.stack = Vector()

    def isEmpty(self):
        return len(self.stack) == 0

    def show(self):
        self.stack.show()

class QueueVector:
    def __init__(self):
        self.queue = Vector()

    def push(self, elemento):
        self.queue.push(elemento)

    def pop(self):
        if not self.isEmpty():
            removed_item = self.queue.itens[0]

            for i in range(1, self.queue.size):
                self.queue.itens[i - 1] = self.queue.itens[i]

            self.queue.size -= 1
            self.queue.itens[self.queue.size] = None

            return removed_item
        
        print("A fila está vazia!")

    def front(self):
        if not self.isEmpty():
            return self.queue.itens[0]
        
        print("A fila está vazia!")

    def isEmpty(self):
        return len(self.queue) == 0

    def show(self):
        self.queue.show()

class PriorityQueueLinkedList:
    def __init__(self):
        self.start = None

    def push(self, elemento, prioridade):
        node = PriorityQueueNode(elemento, prioridade)

        if not self.start or self.start.priority > prioridade :  
            node.next = self.start
            self.start = node
        else :
            current = self.start

            while current.next and current.next.priority <= prioridade:
                current = current.next
            
            node.next = current.next
            current.next = node

    def pop(self):
        if not self.isEmpty():
            removed_item = self.start.data
            self.start = self.start.next

            return removed_item
        
        print("A fila está vazia!")

    def front(self):
        if not self.isEmpty():
            return self.start.data
        
        print("A fila está vazia!")

    def isEmpty(self):
        return self.start is None

    def show(self):
        if not self.start:
            print("A fila está vazia!")
        
            return

        current = self.start
        itens = Vector()
        
        while current:
            itens.push((current.data, current.priority))
            current = current.next
        
        itens.show()

def Test():
    def __vector():
        vector = Vector()

        vector.push(10)
        vector.push(20)
        vector.push(30)
        vector.show()
        vector.insert(15, 1)
        vector.show()
        vector.pop()
        vector.show()
        vector.insert(25, 5)
        vector.pop()
        vector.show()
        print("=====================")

    def __simpleLinkedList():
        list = SimpleLinkedList()

        list.push(10)
        list.push(20)
        list.push(30)
        list.show()
        list.insert(15, 1)
        list.show()
        node = list.start.next
        list.remove(node)
        list.show()
        list.insert(5, 0)
        list.show()  
        list.insert(25, 10)  
        print("=====================")

    def __stackVector():
        stackVector = StackVector()

        stackVector.push(10)
        stackVector.push(20)
        stackVector.push(30)
        stackVector.show() 
        print(stackVector.peek())
        stackVector.pop()
        stackVector.show()
        stackVector.clear()
        stackVector.show()
        print("=====================")

    def __queueVector():
        queue = QueueVector()

        queue.push(10)
        queue.push(20)
        queue.push(30)
        queue.show()
        print(queue.front())
        queue.pop()
        queue.show()
        print(queue.front())
        queue.pop()
        queue.pop()
        queue.show()
        queue.pop()
        print("=====================")
    
    def __priorityQueueLinkedList():
        priorityQueue = PriorityQueueLinkedList()

        priorityQueue.push("A", 3)  
        priorityQueue.push("B", 1)  
        priorityQueue.push("C", 2)  
        priorityQueue.push("D", 0)  
        priorityQueue.show() 
        print(priorityQueue.front())
        priorityQueue.pop()
        priorityQueue.show()
        print(priorityQueue.front())
        priorityQueue.pop()
        priorityQueue.pop()
        priorityQueue.show()
        priorityQueue.pop()
        priorityQueue.show()
        priorityQueue.pop()

    __vector()
    __simpleLinkedList()
    __stackVector()
    __queueVector()
    __priorityQueueLinkedList()


Test()