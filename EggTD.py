#from typing import Counter
import pygame
from Enemy import Egg
from Weapon import Cannon
import time
import sys
import os
from pygame import mixer


# Written by Jackson Hanemann

# Screen dimensions in pixels
WIDTH = 1920
HEIGHT = 1080

# Frames per second
FPS = 60

# Initalise pygame
pygame.init()
GameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))

menuFont = pygame.font.SysFont(None, 36)
smallFont = pygame.font.SysFont(None, 30)

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
        global event

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
                 #options()
                 print("In options")

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
    WHITE = (255,255,255)

    # Timer starts
    starttime = time.time()

    # Set up the font object
    font = pygame.font.Font(None, 48)

    #money system
    cash = 100
    cashIncrement = 15
    weaponCost = 50
    upgradeCost = 50

    #health system
    health = 100
    healthDecrease = -1

    #Buy button text
    buyBut = smallFont.render('NEW CANNON', True, WHITE)

    #upgrade button text
    upgBut =  smallFont.render('UPGRADE CANNON', True, WHITE)


    #BACKGROUND
    Map = pygame.image.load("Background.PNG")
    Map = pygame.transform.scale(Map, (1920,1080))
    MapRect = Map.get_rect()

    TurningP = [(260,170,'up'),(650,170,'flat'),(650,600,'down'),(1150,600,'flat'),(1150,400,'up'),(1928,400,"flat")]

    # Set up rounds 
    roundOne = {'eggCount': 5, 'eggSpeed': 5}
    roundTwo = {'eggCount': 7, 'eggSpeed': 6}
    roundThree = {'eggCount': 10, 'eggSpeed': 7}
    allRounds = [roundOne, roundTwo, roundThree]
    
    allEggs = []

    # Create all eggs
    #for nextRound in allRounds:
    #    numEggs = nextRound['eggCount']
    #    speed = nextRound['eggSpeed']

    #   for eachEgg in range(numEggs):
    #        newEgg = Egg(WIDTH, HEIGHT, speed)
    #       allEggs.append(newEgg)

    myCannon1 = Cannon(WIDTH/2, HEIGHT-900, 'down', 5)
    myCannon2 = Cannon(WIDTH-400, HEIGHT-320, 'up', 5)
    
    allWeapons = [myCannon1, myCannon2]

    spawnFirstEgg = True
    activateFirstWeapon = True
    newWeapon = False
    hasUpgraded = False

    clickBuy = False
    clickUpg = False
    cantUpg = False


    for nextRound in allRounds:
        print("This is round %s" % allRounds.index(nextRound))
        
        #Create eggs for next round
        numEggs = nextRound['eggCount']
        speed = nextRound['eggSpeed']

        for eachEgg in range(numEggs):
            newEgg = Egg(WIDTH, HEIGHT, speed)
            allEggs.append(newEgg)

    #while health > 0:
        
        
        while len(allEggs) > 0 and health > 0:
            mixer.init()
            mixer.music.load('LobbyMusic.mp3')
            mixer.music.stop

            # Draw the background and score to the screen       
            screen.fill(BLACK)
            screen.blit(Map, MapRect)
            cash_text = font.render(f'Cash: ${cash}', True, (0, 0, 0))
            screen.blit(cash_text, (1500, 150))
            health_text = font.render(f'Health: {health}', True, (0, 0, 0))
            screen.blit(health_text, (1500, 200))

            mx, my = pygame.mouse.get_pos()
            button3 = pygame.Rect(WIDTH/1.25, HEIGHT/3.5, 160, 40)
            button4 = pygame.Rect(WIDTH/1.25, HEIGHT/2.5-50, 210, 40)

            if button3.collidepoint(mx, my):
                if click:
                    if cash >= weaponCost:
                        newWeapon = True
                        cash -= weaponCost             
            
            if button4.collidepoint(mx, my):
                if click:
                    if cash >= upgradeCost:
                        hasUpgraded = True
                        cash -= upgradeCost
            
            click = False

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.draw.rect(screen, BLACK, [WIDTH/1.25, HEIGHT/3.5, 160, 40])
            screen.blit(buyBut, (WIDTH/1.25+10, HEIGHT/3.5+10,))

            pygame.draw.rect(screen, BLACK, [WIDTH/1.25, HEIGHT/2.5-50, 210, 40])
            screen.blit(upgBut, (WIDTH/1.25+10, HEIGHT/2.5-40,))

            for myEgg in allEggs:
                # Total time elapsed since the timer started
                totaltime = round((time.time() - starttime), 2)

                # Check if we need to spawn an egg
                if (totaltime > 3 and not myEgg.isAlive) or spawnFirstEgg:
                    myEgg.isAlive = True
                    spawnFirstEgg = False
                    starttime = time.time()

                if not myEgg.isAlive:
                    continue

                # If egg is alive, move it along the path
                myEgg.move(5, TurningP)
                myEgg.setImage()
                screen.blit(myEgg.eggImage, myEgg.eggRect)

                # Is egg safely home?
                if myEgg.eggRect.x > 1928:
                    # Subtract from health
                    health += healthDecrease

                    # Are we still alive?
                    if health < 0:
                        print("GAME OVER!!!")
                        main_menu()

                    # We're Still alive, so remove the egg from the active list
                    allEggs.remove(myEgg)
                    continue

            # Check all weeapons
            for weapon in allWeapons:
                if (activateFirstWeapon or newWeapon) and not weapon.isActive:
                    #print("Activating weapon")
                    weapon.isActive = True
                    activateFirstWeapon = False

                    # If this weapon was bought, subtract from cash
                    if newWeapon:
                        #cash -= weaponCost
                        newWeapon = False

                    
                #if (hasUpgraded) and not weapon.isActive:
                if hasUpgraded and weapon.isActive:
                    weapon.ammoSpeed += 1

                    #if hasUpgraded:
                    #    cash -= upgradeCost             
                    #    hasUpgraded = False

                if not weapon.isActive:
                    continue

                '''for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            main_menu()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            clickBuy = True
                            clickUpg = True

                if button4.collidepoint(mx, my):
                    if clickUpg:
                        weapon.ammoSpeed += 1
                        hasUpgraded = True
                        clickUpg = False
                        if cash < 0:
                            cantUpg = True
                if cantUpg == True:
                    hasUpgraded = False

                if button3.collidepoint(mx, my):
                    if clickBuy:
                        newWeapon = True        
                        clickBuy = False       

                click = False'''

                # Move ammo
                weapon.moveAmmo()

                # Check if ammo hit an egg
                eggHit = weapon.checkHit(allEggs)

                if eggHit == -1:
                    screen.blit(weapon.ammoImage, weapon.ammoRect)
                else:
                    #print("Blit boom")
                    weapon.boomRect.center = allEggs[eggHit].eggRect.center
                    screen.blit(weapon.boomImage, weapon.boomRect)
                    cash += cashIncrement

                    # Remove hit egg
                    allEggs.pop(eggHit)

                screen.blit(weapon.cannonImage, weapon.cannonRect)
            
            if hasUpgraded:
                hasUpgraded = False

            clock.tick(FPS)
            pygame.display.update()


# Display the main menu        
main_menu()
