import move_target
import numpy as np
import constants
import my_panel
import math
import constants
import hospital
import person_pool
import random

class Person(object):
    def __init__(self,city,x,y):
        self.city = city
        self.x = x
        self.y = y

        #符合正态分布的移动目标
        self.targetXU = 100*np.random.randn() + x
        self.targetYU = 100*np.random.randn() + y
        self.targetSig = 50
        self.sig = 1
        self.moveTarget = move_target.MoveTarget(0,0)
        self.moveTarget.setArrived(True)

        #各种状态的value
        self.NORMAL = 0
        self.SUSPECTED = 1
        self.SHADOW = 2
        self.CONFIRMED = 3
        self.FREEZE = 4
        self.CURED = 5

        self.state = self.NORMAL

        self.infectedTime = 0
        self.confiredTime = 0


    def wantMove(self):
        value = self.sig*np.random.randn() + constants.U #正态分布区分人群的出行意愿
        if (value > 0):
            return True
        else:
            return False
    
    def getState(self):
        return self.state
    
    def setState(self,state):
        self.state = state
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self,x):
        self.x = x
    
    def setY(self,y):
        self.y = y
    
    def isInfected(self):
        if (self.state >= self.SHADOW):
            return True
        else:
            return False
    
    def beInfected(self):
        self.state = self.SHADOW
        self.infectedTime = my_panel.MyPanel.worldTime
    
    def distance(self,person):
        return math.sqrt(math.pow(self.x - person.getX(),2) + math.pow(self.y - person.getY(),2))

    def freezy(self):
        self.state = self.FREEZE
    
    def moveTo(self,x,y):
        self.x += x
        self.y += y
    
    def action(self):
        #根据target开始移动
        if (self.state == self.FREEZE):
            return
        
        if (self.wantMove() == False):
            return
        
        if(self.moveTarget.isArrived()):
            targetX = self.targetSig*np.random.randn() + self.targetXU
            targetY = self.targetSig*np.random.randn() + self.targetYU
            self.moveTarget = move_target.MoveTarget(int(targetX),int(targetY))
            self.moveTarget.setArrived(False)
        
        dX = self.moveTarget.getX() - self.x
        dY = self.moveTarget.getY() - self.y
        length = math.sqrt(math.pow(dX,2) + math.pow(dY,2))

        if (length < 1):
            self.moveTarget.setArrived(True)
            return
        
        udX = (int)(dX/length)
        if (udX == 0 and dX != 0):
            if(dX>0):
                udX = 1
            else:
                udX = -1
        
        udY = (int)(dY/length)
        if (udY == 0 and dY != 0):
            if(dY>0):
                udY = 1
            else:
                udY = -1
        
        if(self.x>700):
            self.moveTarget.setArrived(True)
        
        self.moveTo(udX,udY)

    def update(self,bed,person):
        SAFE_DIST = 10

        if(self.state >= self.FREEZE):
            return
        
        if(self.state == self.CONFIRMED and my_panel.MyPanel.worldTime - self.confiredTime >= constants.HOSPITAL_RECEIVE_TIME):
            a = bed.pickBed()
            
            if(a == 1):
                print("隔离区没有床位")
            else:
                self.state = self.FREEZE
                self.x = a.getX()
                self.y = a.getY()
                a.setEmpty(False)
            
        if(my_panel.MyPanel.worldTime - self.infectedTime > constants.SHADOW_TIME and self.state == self.SHADOW):
            self.state = self.CONFIRMED
            self.confiredTime = my_panel.MyPanel.worldTime
        
        self.action()

        peoplelist = person

        if(self.state >= self.SHADOW):
            return
        
        for i in peoplelist:
            if(i.getState() == self.NORMAL):
                continue
            r = random.random()
            if(r < constants.BROAD_RATE and self.distance(i) < SAFE_DIST):
                self.beInfected()
                return
        
        






        

