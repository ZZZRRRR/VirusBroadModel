import city
import numpy as np
import person

class PersonPool(object):#利用标准正态分布创造出围绕在（600，500）周围的人群分布图
    def __init__(self):
        self.c = city.City(600,500)
        self.personlist = list()
        for i in range(1000):
            x = (int)(100 * np.random.randn() + self.c.getCenterX())
            y = (int)(100 * np.random.randn() + self.c.getCenterY())
            if (x > 900):
                x = 900
            p = person.Person(self.c,x,y)
            self.personlist.append(p)

    def getPersonList(self):
        return self.personlist
            
            