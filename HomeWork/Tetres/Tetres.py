import Array

class Tetres:
    def __init__(self, quantity, height):
        self.quantity = quantity
        self.height = height
        self.size = 0
        self.points = 0
        self.tower = Array.Array(height)

    def incrementPoints(self) :
        self.points += 10

    def push(self, block):
        
        if isinstance(block, str) and len(block) != 3:
            return
        
        if self.size > self.height :
            return
        
        

        return
    
    def scorePoint(self):

        return

    def __str__(self):
        pass
