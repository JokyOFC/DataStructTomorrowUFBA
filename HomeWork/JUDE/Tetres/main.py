class Array:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def append(self, value):
        if self.size < self.capacity:
            self.data[self.size] = value
            self.size += 1
        else:
            raise OverflowError("Array is full")

    def pop(self):
        if self.size > 0:
            value = self.data[self.size - 1]
            self.data[self.size - 1] = None
            self.size -= 1
            return value
        return None

    def peek(self):
        if self.size > 0:
            return self.data[self.size - 1]
        return None

    def __len__(self):
        return self.size

def Tetres(quantity, height, block):
    def perfectMatch(block1, block2):
        return all(b1 != b2 for b1, b2 in zip(block1, block2))
    
    tower = Array(height)
    score = 0

    if isinstance(block, str) and len(block) != 3:
        return
        
    for block in block:
        if len(tower) > 0 and perfectMatch(tower.peek(), block):        
            tower.pop()
            score += 10
        else:
            try:
                tower.append(block)
            except OverflowError:
                return "game over"

        if len(tower) > height:
            return "game over"

    return score
    

first_line = input().split()
N, M = int(first_line[0]), int(first_line[1])

blocks = [input().strip() for _ in range(N)]

print(Tetres(N, M, blocks))
