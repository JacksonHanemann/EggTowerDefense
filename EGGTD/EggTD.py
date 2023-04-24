#from typing import Counter
import pygame
from Enemy import Egg
from Weapon import Cannon
import time
import sys
import os
from pygame import mixer


#written by Jackson Hanemann

#Screen dimensions in pixels
WIDTH = 1920
HEIGHT = 1080

#Frames per second
FPS = 60

#initalise pygame
pygame.init()
GameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))

menuFont = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 

def main_menu():
    mixer.init()
    mixer.music.load('LobbyMusic.mp3')
    mixer.music.play()

    while True:
        
 
        screen.fill((0,0,0))
        draw_text('main menu', menuFont, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(860, 100, 200, 50)
        button_2 = pygame.Rect(860, 200, 200, 50)
        
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                 options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        cash_text = menuFont.render(f'Start Game', True, (255, 255, 255))
        screen.blit(cash_text, (860, 120))

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        clock.tick(60)

def game():  

    #BGcolour
    BLACK = (0,0,0)

    # Timer starts
    starttime = time.time()

    # Set up the font object
    font = pygame.font.Font(None, 48)

    #money system
    cash = 100
    cashIncrement = 15

    #health system+
    health = 100
    healthDecrease = -1


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
                
        
        #clock.tick(FPS)
        for myEgg in allEggs:

            # Draw the score to the screen
            

            # Total time elapsed since the timer started
            totaltime = round((time.time() - starttime), 2)

            if totaltime > 3:
                spawn = True
                starttime = time.time()
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
            cash_text = font.render(f'Cash: ${cash}', True, (0, 0, 0))
            screen.blit(cash_text, (1500, 150))
            health_text = font.render(f'Health: {health}', True, (0, 0, 0))
            screen.blit(health_text, (1500, 200))


            
            if myCannon.ammoHit == False:
                print("Blit ammo")
                screen.blit(myCannon.ammoImage, myCannon.ammoRect)
            else:
                print("Blit boom")
                myCannon.boomRect.center = myEgg.eggRect.center
                screen.blit(myCannon.boomImage, myCannon.boomRect)
                myCannon.ammoHit = False
                cash += cashIncrement

            screen.blit(myCannon.cannonImage, myCannon.cannonRect)
            myEgg.setImage()
            
            myCannon.Fire(myEgg)


            if myEgg.hasSpawned:
                if myEgg.isAlive:
                    print("I am alive")
                    screen.blit(myEgg.eggImage, myEgg.eggRect)
                else:
                    print("I am dead")
                    allEggs.remove(myEgg)
                    continue
            else:
                print("I have not spawned yet")
                continue        


            if myEgg.eggRect.x > 1928:
                health += healthDecrease
                allEggs.remove(myEgg)
                continue
                

            if myEgg.myDirection == "flat":
                #print("On the flat")
                myEgg.moveX(50)
                if myEgg.eggRect.x > TurningP[myEgg.xonMap][0]:
                    myEgg.myDirection = TurningP[myEgg.xonMap][2]
                    myEgg.xonMap += 1
            else:
                if myEgg.myDirection == "down":
                    if myEgg.eggRect.y > TurningP[myEgg.yonMap][1]:
                        myEgg.yonMap += 1
                        myEgg.myDirection = TurningP[myEgg.yonMap][2]
                    else:
                        myEgg.moveY(50)
                if myEgg.myDirection == "up":
                    if myEgg.eggRect.y < TurningP[myEgg.yonMap][1]:
                        myEgg.yonMap += 1
                        myEgg.myDirection = TurningP[myEgg.yonMap][2]
                    else:
                        myEgg.moveY(-50)
        
            pygame.display.update()
            
        

        

        

    #pygame.quit()
main_menu()

