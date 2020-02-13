from tkinter import *
import hospital
import person_pool

class MyPanel(object):

    worldTime = 0 #模拟现实世界的天数

    def __init__(self,person):
        #初始化界面，tkinter展开画布Canvas
        self.pindex = 0

        self.personlist = person
        self.bed = hospital.Hospital()

        self.root = Tk()
        self.root.title('virus broading model')
        self.root.geometry('1000x1000+500+200')
        self.cv = Canvas(self.root,height = 1000,width = 1000,bg = 'black')
        self.h = hospital.Hospital()
    

    def paint(self):
        #根据person_pool中的人数开始描点，不同的状态代表不同的颜色

        if (self.personlist == None):
            return
        
        #self.personlist[self.pindex].update(self.bed,self.personlist)#突然发现自己写了个很神奇的代码!!

        self.cv.delete(ALL)

        self.cv.create_rectangle(self.h.getX(),self.h.getY(),self.h.getWidth(),self.h.getHeight(),dash = 10,outline = 'red')#绘出医院的虚线矩形
        for i in self.personlist:
            if(i.getState() == 0):
                self.cv.create_oval(i.getX(),i.getY(),i.getX()+5,i.getY()+5,fill = 'white')
            elif(i.getState() == 2):
                self.cv.create_oval(i.getX(),i.getY(),i.getX()+5,i.getY()+5,fill = 'yellow')
            elif(i.getState() == 3 or i.getState() == 4):
                self.cv.create_oval(i.getX(),i.getY(),i.getX()+5,i.getY()+5,fill = 'red')
            else:
                pass
            i.update(self.bed,self.personlist)#更新传染情况
        
        self.pindex += 1
        if (self.pindex >= len(self.personlist) - 1):
            self.pindex = 0
        MyPanel.worldTime += 1
        self.root.after(100,self.paint)#每隔一秒就重新执行paint函数

    def run(self):
        self.paint()
        self.cv.pack()
        self.root.mainloop()

        

        




