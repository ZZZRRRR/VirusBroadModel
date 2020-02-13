class City(object):
    def __init__(self,centerX,centerY):
        self.centerX = centerX
        self.centerY = centerY
    
    def getCenterX(self):
        return self.centerX

    def getCenterY(self):
        return self.centerY

    def setCenterX(self,centerX):
        self.centerX = centerX
    
    def setCenterY(self,centerY):
        self.centerY = centerY
        