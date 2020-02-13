class MoveTarget(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.arrived = False
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setY(self,y):
        self.y = y
    
    def setX(self,x):
        self.x = x
    
    def isArrived(self):
        return self.arrived
    
    def setArrived(self,arrived):
        self.arrived = arrived

        
    