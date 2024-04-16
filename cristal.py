class Cristal:
    def __init__(self, x, y, width, height, path, kind): 
        self.x = x
        self.y = y
        self.root_y = y
        self.width = width
        self.height = height
        self.path = path
        self.kind = kind
        self.is_collected = False
    
    def get_X(self):
        return self.x
    
    def set_x(self, x):
        self.x = x
    
    def get_y(self):
        return self.y
    
    def set_y(self, y):
        self.y = y
    
    def move(self, steps, new_y):
        if self.y >= new_y:
            self.y += steps
        else:
            self.y -= steps
    

