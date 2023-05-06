import pygame

class Cannon:
    imageFile = "Cannon.PNG"
    ammoImageFile = "cannonBall.PNG"
    boomImageFile = "boom.PNG"
    




    def __init__(self, xLoc, yLoc, direction, speed):
        # Set up the weapon
        self.cannonImage = pygame.image.load(self.imageFile)
        self.cannonRect = self.cannonImage.get_rect()
        self.cannonRect.x = xLoc
        self.cannonRect.y = yLoc
        self.direction = direction

        if self.direction == 'up':
             rotation = 90
        if self.direction == 'down':
            rotation = 270
        self.cannonImage = pygame.transform.rotate(self.cannonImage,rotation)

        # Set up the ammo
        self.ammoImage = pygame.image.load(self.ammoImageFile)
        self.ammoRect = self.ammoImage.get_rect()
        self.ammoRect.x = self.cannonRect.x +self.cannonRect.height/2 - self.ammoRect.width/2
        self.ammoRect.y = self.cannonRect.bottom
        self.startX = self.ammoRect.x
        self.startY = self.ammoRect.y
        self.ammoSpeed = speed


        # Set up collision 
        self.boomImage = pygame.image.load(self.boomImageFile)
        self.boomRect = self.boomImage.get_rect()
        #self.ammoHit = False
    

    def moveAmmo(self):
        if self.direction == 'up':
            self.ammoRect.y -= self.ammoSpeed
        else: self.ammoRect.y += self.ammoSpeed
            
        if self.direction == 'down':
            if self.ammoRect.y > 1080:
                self.ammoRect.y = self.startY
        elif self.ammoRect.y < 0:
                self.ammoRect.y = self.startY

    def checkHit(self, eggList):
        eggRects = []
        for egg in eggList:
             eggRects.append(egg.eggRect)
        collidedWithEgg = self.ammoRect.collidelist(eggRects)

        if collidedWithEgg > -1:
            print("Collided in Fire method")
            # Start a new round of ammo
            self.ammoRect.y = self.startY
            #self.ammoHit = True
        return collidedWithEgg
