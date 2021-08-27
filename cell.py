class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.connected = False

    def __repr__(self):
        return f'{(self.x, self.y)}'
