import my_panel
import threading
import person_pool
import constants
import random

if __name__ == "__main__":
    people = person_pool.PersonPool()
    peoplelist = people.getPersonList()

    #从初始传染数量中随机抽取感染者
    for i in range(constants.ORIGINAL_COUNT):
        index = random.randint(0,len(peoplelist) - 1)
        person = peoplelist[index]

        while (person.isInfected()):
            index = random.randint(0,len(peoplelist) - 1)
            person = peoplelist[index]
        
        person.beInfected()

    p = my_panel.MyPanel(peoplelist)
    p.run()


    

        

        
