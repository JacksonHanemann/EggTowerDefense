import pygame

class Egg:
    
    eggImgLeft = pygame.image.load("EGG.PNG")
    eggImgRight = pygame.image.load("EGG2.PNG")
    eggImages = [eggImgLeft, eggImgRight]

    def __init__(self, imgWidth, imgHeight, speed):
        self.eggImage = self.eggImages[0]
        self.eggRect = self.eggImage.get_rect()
        self.eggRect.x = imgWidth/2-1000
        self.eggRect.y = imgHeight/2-60
        self.isAlive = False
        self.hasSpawned = False
        self.myDirection = 'flat'
        self.myCounter = 0
        self.imgNumber = 0
        self.xonMap = 0
        self.yonMap = 0
        self.eggSpeed = speed

    def setImage(self):   
        self.imgNumber = self.myCounter//20
        if self.myCounter > 38:
            self.myCounter = 0
        else:
            self.myCounter += 1

        self.eggImage = self.eggImages[self.imgNumber]

    #def setStatus(self, status):
    #    self.isAlive = status

    def move(self, speed, TurningP):
        if self.myDirection == "flat":
            #print("On the flat")
            self.moveX(5)
            if self.eggRect.x > TurningP[self.xonMap][0]:
                self.myDirection = TurningP[self.xonMap][2]
                self.xonMap += 1
        else:
            if self.myDirection == "down":
                if self.eggRect.y > TurningP[self.yonMap][1]:
                    self.yonMap += 1
                    self.myDirection = TurningP[self.yonMap][2]
                else:
                    self.moveY(5)
            if self.myDirection == "up":
                if self.eggRect.y < TurningP[self.yonMap][1]:
                    self.yonMap += 1
                    self.myDirection = TurningP[self.yonMap][2]
                else:
                    self.moveY(-5)

    
    def moveX(self, speed):
        self.eggRect.x += speed
    
    def moveY(self, speed):
        self.eggRect.y += speed


     

    