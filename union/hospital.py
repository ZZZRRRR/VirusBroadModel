import constants
import bed
import point

class Hospital(object):
    def __init__(self):
        self.x = 60
        self.y = 110
        self.width = 0
        self.height = 540
        self.p = point.Point(70,120)
        self.beds = list()

        if (constants.BED_COUNT == 0):
            self.width = 0
            self.height = 0
        
        self.column = constants.BED_COUNT/100
        self.width = self.column*6 + self.x

        for i in range(int(self.column)):
            for j in range(10,410,4):
                b = bed.Bed(self.p.getX() + i*6,self.p.getY() + j)
                self.beds.append(b)
        
    def pickBed(self):
        for i in self.beds:
            if(i.isEmpty()):
                return i
        return 1

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
        
        


            