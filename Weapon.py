import pygame

class Cannon:
    imageFile = "Cannon.PNG"
    ammoImageFile = "cannonBall.PNG"
    boomImageFile = "boom.PNG"
    




    def __init__(self, xLoc, yLoc, direction):

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

        
    

        self.ammoImage = pygame.image.load(self.ammoImageFile)
        self.ammoRect = self.ammoImage.get_rect()
        self.ammoRect.centerx = self.cannonRect.x +self.cannonRect.height/2 - self.ammoRect.width/2
        self.ammoRect.centery = self.cannonRect.bottom
        self.startX = self.ammoRect.x
        self.startY = self.ammoRect.y
        self.ammoSpeed = 5

        self.boomImage = pygame.image.load(self.boomImageFile)
        self.boomRect = self.boomImage.get_rect()
        self.ammoHit = False
    

    #def Fire(self, allEggs):
    def Fire(self, egg):

            if egg.isAlive:

                if self.ammoRect.collidelist([egg.eggRect]) >-1:
                    self.ammoRect.centery = self.startY
                    self.ammoHit = True
                    egg.setStatus(False)

                    
                if self.direction == 'down':
                    if self.ammoRect.y >1080:
                        self.ammoRect.centery = self.startY
                elif self.ammoRect.y <0:
                     self.ammoRect.centery = self.startY
                    
                     
                

                    
        



     

    