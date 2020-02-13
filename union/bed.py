import point

class Bed(point.Point):

    def __init__(self,x,y):
        super().__init__(x,y)
        self.isEmptys = True
    
    def isEmpty(self):
        return self.isEmptys
    
    def setEmpty(self,empty):
        self.isEmptys = empty
