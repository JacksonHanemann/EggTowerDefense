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

    click = False

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
        clock.tick(5)

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


    myCannon1 = Cannon(WIDTH/2, HEIGHT-900, 'down', 5)
    myCannon2 = Cannon(WIDTH-400, HEIGHT-320, 'up', 5)
    
    
    allWeapons = [myCannon1, myCannon2]

    spawn = True


    while len(allEggs) > 0:
        # Draw the background and score to the screen       
        screen.fill(BLACK)
        screen.blit(Map, MapRect)
        cash_text = font.render(f'Cash: ${cash}', True, (0, 0, 0))
        screen.blit(cash_text, (1500, 150))
        health_text = font.render(f'Health: {health}', True, (0, 0, 0))
        screen.blit(health_text, (1500, 200))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        for myEgg in allEggs:
            #print("Checking egg " + str(allEggs.index(myEgg)))

            # Total time elapsed since the timer started
            totaltime = round((time.time() - starttime), 2)
            #print(totaltime)

            # Check if we need to spawn an egg
            if (totaltime > 3 and not myEgg.isAlive) or spawn:
                spawn = False
                myEgg.isAlive = True
                starttime = time.time()

            if myEgg.isAlive == False:
                #print("continuing")
                continue

            # If egg is alive, move it along the path
            myEgg.move(5, TurningP)
            myEgg.setImage()
            screen.blit(myEgg.eggImage, myEgg.eggRect)

            # If egg is safely home, remove it from the list of active eggs and substract from player health
            if myEgg.eggRect.x > 1928:
                health += healthDecrease
                allEggs.remove(myEgg)
                continue

        # Check all weeapons
        for weapon in allWeapons:
            # Move ammo
            weapon.moveAmmo()

            # Check if ammo hit an egg and if it did, capture which egg was hit
            eggHit = weapon.checkHit(allEggs)

            #if weapon.ammoHit == False:
            if eggHit == -1:
                #print("Blit ammo")
                screen.blit(weapon.ammoImage, weapon.ammoRect)
            else:
                print("Blit boom")
                weapon.boomRect.center = allEggs[eggHit].eggRect.center
                screen.blit(weapon.boomImage, weapon.boomRect)
                #weapon.ammoHit = False
                cash += cashIncrement

                # Remove hit egg
                allEggs.pop(eggHit)

            screen.blit(weapon.cannonImage, weapon.cannonRect)

        clock.tick(FPS)
        pygame.display.update()


            
        

        

        

    #pygame.quit()
main_menu()

