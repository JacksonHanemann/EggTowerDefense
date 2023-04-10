#from typing import Counter
import pygame
from Enemy import Egg
from Weapon import Cannon
import time

#written by Jackson Hanemann

#Screen dimensions in pixels
WIDTH = 1920
HEIGHT = 1080

#Frames per second
FPS = 60

active = True
clock = pygame.time.Clock()

#BGcolour
BLACK = (0,0,0)

# Timer starts
starttime = time.time()

#initalise pygame
pygame.init()
GameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))


#BACKGROUND
Map = pygame.image.load("Background.PNG")
Map = pygame.transform.scale(Map, (1920,1080))
MapRect = Map.get_rect()

TurningP = [(260,170,'up'),(650,170,'flat'),(650,600,'down'),(1150,600,'flat'),(1150,400,'up'),(1928,400,"flat")]

# Create all eggs
Egg1 = Egg(WIDTH, HEIGHT)
Egg2 = Egg(WIDTH, HEIGHT)
Egg3 = Egg(WIDTH, HEIGHT)
Egg4 = Egg(WIDTH, HEIGHT)
Egg5 = Egg(WIDTH, HEIGHT)

# Egg array
allEggs = [Egg1, Egg2, Egg3, Egg4, Egg5]

myCannon = Cannon(WIDTH, HEIGHT)

spawn = True

while len(allEggs) > 0:
    # Total time elapsed since the timer started
    totaltime = round((time.time() - starttime), 2)

    if totaltime > 2:
        spawn = True
        starttime = time.time()
    
    #clock.tick(FPS)
    for myEgg in allEggs:
        print("Checking egg " + str(allEggs.index(myEgg)))
        if spawn == True:
            print("Spawning")
            myEgg.isAlive = True
            myEgg.hasSpawned = True
            spawn = False
            print("Alive=" + str(myEgg.isAlive) + ", Spawned=" + str(myEgg.hasSpawned))

        if myEgg.isAlive == False:
            continue
    
        
        screen.fill(BLACK)
        screen.blit(Map, MapRect)
        screen.blit(myEgg.eggImage, myEgg.eggRect)

        screen.blit(myCannon.cannonImage, myCannon.cannonRect)
        myEgg.setImage()
        
        myCannon.Fire(myEgg)

        if myCannon.ammoHit == False:
            print("Blit ammo")
            screen.blit(myCannon.ammoImage, myCannon.ammoRect)
        else:
            print("Blit boom")
            myCannon.boomRect.center = myEgg.eggRect.center
            screen.blit(myCannon.boomImage, myCannon.boomRect)
            myCannon.ammoHit = False

        if myEgg.hasSpawned:
            if myEgg.isAlive:
                print("I am alive")
                #screen.blit(myEgg.eggImage, myEgg.eggRect)
            else:
                print("I am dead")
                allEggs.remove(myEgg)
                continue
        else:
            print("I have not spawned yet")
            continue
        
        if myEgg.myDirection == "flat":
            #print("On the flat")
            myEgg.moveX(5)
            if myEgg.eggRect.x > TurningP[myEgg.xonMap][0]:
                myEgg.myDirection = TurningP[myEgg.xonMap][2]
                myEgg.xonMap += 1
        else:
            if myEgg.myDirection == "down":
                if myEgg.eggRect.y > TurningP[myEgg.yonMap][1]:
                    myEgg.yonMap += 1
                    myEgg.myDirection = TurningP[myEgg.yonMap][2]
                else:
                    myEgg.moveY(5)
            if myEgg.myDirection == "up":
                if myEgg.eggRect.y < TurningP[myEgg.yonMap][1]:
                    myEgg.yonMap += 1
                    myEgg.myDirection = TurningP[myEgg.yonMap][2]
                else:
                    myEgg.moveY(-5)
    
    
        pygame.display.update()
    

    

pygame.quit()
