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
        self.size = 0

    def Enqueue(self, value):

        node = Node(value)
        
        self.size += 1

        if(self.end is None):
            self.first = node
            self.end = node
            return

        self.end.next = node
        self.end = node

    def Dequeue(self):
        
        if(self.first is None):
            return
        
        self.size -= 1
        
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

        text += f"First: {self.first} \nLast: {self.end} \nSize: {self.size}\n"

        current = self.first

        while current is not None:
            text += f"{current.data} -> "
            current = current.next
        
        text += "None"

        return text
    
class ClashRoyale:

    def __init__(self):
        self.cards = 0
        self.rounds = 0
        self.deck = Queue()
        self.enemyDeck = Queue()

    def createDeck(self):

        quantityCards = int(input("Quantity of Your Cards: "))

        self.cards = quantityCards

        if(quantityCards == 0 or isinstance(quantityCards, str)):
            return

        count = 0

        while(count != self.cards):
            value = int(input("Life of this card: "))
            self.deck.Enqueue(value)
            count += 1

        rounds = int(input("Quantity of Enemy Cards: "))

        self.rounds = rounds

        if(rounds == 0 or isinstance(rounds, str)):
            return

        count = 0

        while(count != self.rounds):
            value = int(input("Quantity of this enemy card: "))
            self.enemyDeck.Enqueue(value)
            count += 1
        

    def play(self):
        
        self.createDeck()

        count = self.rounds

        while(count != 0):
            
            count -= 1

            if(self.deck.first.data >= self.enemyDeck.first.data):
                # MATEI
                lived = self.deck.Dequeue()
                self.deck.Enqueue(lived)
            else:
                # MORRI
                self.deck.Dequeue()
                self.enemyDeck.Dequeue()
            

    def showCardsLeft(self):
        return self.deck.size - self.rounds
    
    def showDecks(self):
        print(f"Your deck: \n{self.deck} \n\nEnemy deck: \n{self.enemyDeck}")



join = ClashRoyale()

join.play()
print(join.showCardsLeft())

