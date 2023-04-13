import pygame

class Cannon:
    imageFile = "Cannon.PNG"
    ammoImageFile = "cannonBall.PNG"
    boomImageFile = "boom.PNG"
    




    def __init__(self, imgWidth, imgHeight):

        self.cannonImage = pygame.image.load(self.imageFile)
        self.cannonRect = self.cannonImage.get_rect()
        self.cannonRect.x = imgWidth/2
        self.cannonRect.y = imgHeight-900
        self.cannonImage = pygame.transform.rotate(self.cannonImage,270)

        self.ammoImage = pygame.image.load(self.ammoImageFile)
        self.ammoRect = self.ammoImage.get_rect()
        #self.ammoRect.x = self.cannonRect.x +self.cannonRect.height/2 - self.ammoRect.width/2
        #self.ammoRect.y = self.cannonRect.bottom
        #self.ammoRect.x = imgWidth/2
        #self.ammoRect.y = imgHeight-900
        self.ammoRect.centerx = self.cannonRect.x +self.cannonRect.height/2 - self.ammoRect.width/2
        self.ammoRect.centery = self.cannonRect.bottom
        self.startX = self.ammoRect.x
        self.startY = self.ammoRect.y

        self.boomImage = pygame.image.load(self.boomImageFile)
        self.boomRect = self.boomImage.get_rect()
        self.ammoHit = False
    

    #def Fire(self, allEggs):
    def Fire(self, egg):
            ammoSpeed = 5
        #for egg in allEggs:
            if egg.isAlive:
                print("Egg is alive")
                '''if self.ammoRect.centerx > egg.eggRect.centerx:
                    #print("Ammox -1")
                    self.ammoRect.centerx  -= ammoSpeed
                else:
                    self.ammoRect.centerx += ammoSpeed
                    #print("Ammox +1")
                if self.ammoRect.centery > egg.eggRect.centery:
                    #print("Ammoy -1")
                    self.ammoRect.centery -= ammoSpeed
                else:
                    #print("Ammoy +1")
                    self.ammoRect.centery += ammoSpeed'''
                self.ammoRect.y += ammoSpeed

                if self.ammoRect.collidelist([egg.eggRect]) >-1:
                    print("Collided in Fire method")
                    #self.ammoRect.centerx = self.startX
                    self.ammoRect.centery = self.startY
                    self.ammoHit = True
                    egg.setStatus(False)
                if self.ammoRect.y >1080:
                     self.ammoRect.centery = self.startY
                

                    
        



     

    