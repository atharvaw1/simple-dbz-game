import pygame
import time
import copy
from threading import *


pygame.init()
screen=pygame.display.set_mode((1280,1024))

class player1:

    def __init__(self,name1,name2):
        
        self.name1 = name1
        self.charge1=0
        self.bg=pygame.image.load('Background2.JPG')
        self.attno1=0
        self.name2 = name2
        self.charge2=0
        self.attno2=0
                
    def move(self):
        
        if self.name1 == 'goku':
            self.image1=pygame.image.load('Goku.png')
        self.player1pos=[600,512]
        keys1=[False,False,False,False,False]

        if self.name2 == 'goku':
            self.image2=pygame.image.load('Goku.png')
        self.player2pos=[680,512]
        keys2=[False,False,False,False,False]
        
        while 1:
            
            screen.fill(0)
            screen.blit(self.bg,[0,0])
            screen.blit(self.image1,self.player1pos)
            screen.blit(self.image2,self.player2pos)
            pygame.key.set_repeat(0,0)
            
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
                self.image1=pygame.image.load('gokucharge.png')
                self.charge1+=1
            else:
                self.image1=pygame.image.load('Goku.png')

                
                

            if pygame.key.get_pressed()[pygame.K_SPACE] and self.charge1>=1:
                self.att1=pygame.image.load('kamehameha2.TIFF')
                self.charge1-=1
                self.attno1+=1
                att1=attack1(self.player1pos,self.player2pos)
                
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
                self.image2=pygame.image.load('gokucharge.png')
                self.charge2+=1
            else:
                self.image2=pygame.image.load('Goku.png')

                


            if pygame.key.get_pressed()[pygame.K_RETURN] and self.charge2>=5:
                self.att2=pygame.image.load('kamehameha2.TIFF')
                self.charge2-=5
                self.attno2+=1
                att2=attack2(self.player1pos,self.player2pos)
                

            while self.attno2>0:
                att2.attmov()
                break

            


            pygame.display.update()




class attack1():
    
    def __init__(self,player1pos,player2pos):
        self.att=pygame.image.load('kamehameha2.TIFF')
        self.attpos1=copy.deepcopy(player1pos)
        self.player2pos=player2pos
    def attmov(self):
        while True:
            screen.blit(self.att,self.attpos1)
            if self.attpos1==self.player2pos:
                print 'hit'            
            self.attpos1[0]+=15

            if self.attpos1[0]<0:
                
                break
            break

    
class attack2(attack1):
    
    def __init__(self,player1pos,player2pos):
        self.att=pygame.image.load('kamehameha2.TIFF')
        self.attpos2=copy.deepcopy(player2pos)
        attack1.__init__(self,player1pos,player2pos)
        self.player1pos=player1pos
        
    def attmov(self):
        while True:
            screen.blit(self.att,self.attpos2)
            if self.attpos2==self.player1pos:
                print 'hit'
            self.attpos2[0]-=15

            if self.attpos2[0]<0 or self.attpos2[0]==self.attpos1[0]:
                
                break
            break

          
    
        


    

p1=player1('goku','goku')
p1.move()


