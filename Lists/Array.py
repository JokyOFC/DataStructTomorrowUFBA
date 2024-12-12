class Array:
    def __init__(self, max):
        self.vector = [None] * max
        self.max = max
        self.size = 0

    def push(self, element):
        
        if self.size == self.max:
            print("Array Full")
            return
        
        self.vector[self.size] = element

        self.size += 1

    def pop(self):
       
        if self.size == 0 :
           return
        
        value = self.vector[self.size - 1]

        self.vector[self.size - 1] = None
        
        self.size -= 1
       
        return value
        
    def peek(self):

        if self.size > 0:
            return self.vector[self.size - 1]
    
    def remove(self, index):
        
        if index >= self.size:
            return
        
        if self.size == 0:
            return

        if index == self.size - 1:
            self.size -= 1
            return
        
        for i in range(index + 1, self.size):
            self.vector[i - 1] = self.vector[i]

        self.size -= 1

    def __str__(self):
        
        text = "["
        
        for i in range(self.size):
            text += f"{self.vector[i]}"

            if i != self.size - 1:
                text += ", "

        text += "]"

        return text
    
    def __len__(self):
        return self.size

