import pygame
import time
import copy
from threading import *

healthvalue1=200
healthvalue2=200
pygame.init()
screen=pygame.display.set_mode((1280,1024),pygame.FULLSCREEN)

class player:
    
    def __init__(self,name1,name2):
        
        
        self.name1 = name1
        self.charge1=0
        self.bg=pygame.image.load('Background2.JPG')
        self.attno1=0
        self.name2 = name2
        self.charge2=0
        self.attno2=0
        
        if self.name1 == 'goku':
            self.image1=pygame.image.load('goku/goku.png')
        if self.name2 == 'goku':
            self.image2=pygame.image.load('goku/gokuf.png')
        self.player1rect=pygame.Rect(self.image1.get_rect())
        self.player2rect=pygame.Rect(self.image2.get_rect())

        self.healthbar = pygame.image.load("healthbar.png")
        self.health = pygame.image.load("health.png")
                
    def move(self):
               
        global healthvalue1,healthvalue2
        self.player1pos=[600,512]
        keys1=[False,False,False,False,False]


            
        self.player2pos=[680,512]
        keys2=[False,False,False,False,False]
        
        while 1:
            
            #Putting players on screen
            screen.fill(0)
            screen.blit(self.bg,[0,0])
            screen.blit(self.image1,self.player1pos)
            screen.blit(self.image2,self.player2pos)
            pygame.key.set_repeat(0,0)
            
            #Player1 health bar
            screen.blit(self.healthbar,[20,5])
            for health1 in range(healthvalue1):
                screen.blit(self.health, (health1+23,8))
                
            #Player2 health bar
            screen.blit(self.healthbar,[1000,5])
            for health2 in range(healthvalue2):
                screen.blit(self.health, (health2+1003,8))

            #Player1 charge bar
            screen.blit(self.healthbar,[20,20])
            for charge in range(self.charge1):
                screen.blit(self.health, (charge+23,23))
            #Player2 charge bar
            screen.blit(self.healthbar,[1000,20])
            for charge in range(self.charge2):
                screen.blit(self.health, (charge+1003,23))
            
            #Cheking for key presses and other events
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit(0)

                #Player1
                          
                if pygame.key.get_pressed()[pygame.K_w]:
                    keys1[0]=True
                else:
                    keys1[0]=False
                   
                if pygame.key.get_pressed()[pygame.K_a]:
                    keys1[1]=True
                else:
                    keys1[1]=False
          
                if pygame.key.get_pressed()[pygame.K_s]:
                    keys1[2]=True
                else:
                    keys1[2]=False
               
                if pygame.key.get_pressed()[pygame.K_d]:
                    keys1[3]=True
                else:
                    keys1[3]=False

                if pygame.key.get_pressed()[pygame.K_z] and pygame.key.get_pressed()[pygame.K_w]==False and pygame.key.get_pressed()[pygame.K_a]==False and pygame.key.get_pressed()[pygame.K_s]==False and pygame.key.get_pressed()[pygame.K_d]== False:
                    keys1[4]=True
                else:
                    keys1[4]=False
                    

                #Player2
                if pygame.key.get_pressed()[pygame.K_UP]:
                    keys2[0]=True
                else:
                    keys2[0]=False

                    
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    keys2[1]=True
                else:
                    keys2[1]=False
                    

                    
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    keys2[2]=True
                else:
                    keys2[2]=False
     
                    
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    keys2[3]=True
                else:
                    keys2[3]=False

                if pygame.key.get_pressed()[pygame.K_RSHIFT] and pygame.key.get_pressed()[pygame.K_RIGHT]==False and pygame.key.get_pressed()[pygame.K_DOWN]==False and pygame.key.get_pressed()[pygame.K_LEFT]==False and pygame.key.get_pressed()[pygame.K_UP]== False:
                    keys2[4]=True
                else:
                    keys2[4]=False
                    

                    
                    
            
            #Player1
            if keys1[0] and self.player1pos[1]>0:
                self.player1pos[1]-=5
            if keys1[1] and self.player1pos[0]>0:
                self.player1pos[0]-=5
            if keys1[2] and self.player1pos[1]<1024:
                self.player1pos[1]+=5
            if keys1[3] and self.player1pos[1]<1280:
                self.player1pos[0]+=5
            if keys1[4]:
                self.image1=pygame.image.load('goku/charge.png')
                self.charge1+=1
            else:
                self.image1=pygame.image.load('goku/goku.png')

                
            #Attack code for player1

            if pygame.key.get_pressed()[pygame.K_SPACE] and self.charge1>=1:
                self.att1=pygame.image.load('goku/kamehameha2.png')
                self.charge1-=1
                self.attno1+=1
                att1=attack1(self.player1pos)
                
            while self.attno1>0:
                att1.attmov()
                break

            #Player2
            if keys2[0] and self.player2pos[1]>0:
                self.player2pos[1]-=5
            if keys2[1] and self.player2pos[0]>0:
                self.player2pos[0]-=5
            if keys2[2] and self.player2pos[1]<1426:
                self.player2pos[1]+=5
            if keys2[3] and self.player2pos[1]<1394:
                self.player2pos[0]+=5

            if keys2[4]:
                self.image2=pygame.image.load('goku/charge.png')
                self.charge2+=1
            else:
                self.image2=pygame.image.load('goku/gokuf.png')

                
            #Attack code for player2

            if pygame.key.get_pressed()[pygame.K_RETURN] and self.charge2>=5:
                self.att2=pygame.image.load('goku/kamehameha2.png')
                self.charge2-=5
                self.attno2+=1
                att2=attack2(self.player2pos)
                

            while self.attno2>0:
                att2.attmov()
                break

            


            pygame.display.update()

#object for player class
p1=player('goku','goku')


class attack1():
    
    def __init__(self,player1pos):
        self.att=pygame.image.load('goku/kamehameha2.png')
        self.attrect=pygame.Rect(self.att.get_rect())
        self.attpos1=copy.deepcopy(player1pos)
                                                                                                                                                                                                                                                                
    def attmov(self):
        global healthvalue2
        while True:
            screen.blit(self.att,self.attpos1)
            if self.attrect.colliderect(p1.player2rect):
                healthvalue2-=10
                p1.attno1-=1
                break
            self.attpos1[0]+=15

            if self.attpos1[0]<0:
                
                break
            break

    
class attack2(attack1):
    
    def __init__(self,player2pos):
        self.att=pygame.image.load('goku/kamehameha2.png')
        self.attrect=pygame.Rect(self.att.get_rect())
        self.attpos2=copy.deepcopy(player2pos)
                
    def attmov(self):
        global healthvalue1
        while True:
            screen.blit(self.att,self.attpos2)
            if self.attrect.colliderect(p1.player1rect):
                healthvalue1-=10
                p1.attno2-=1
                break
            self.attpos2[0]-=15

            if self.attpos2[0]<0:
                
                break
            break

          
    
        


    


p1.move()


