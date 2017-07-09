'''This prgram is an entertaning game for kids based on the game Dragon Ball Z.
It is a multiplayer platform fighting game using pygame and other modules of python.'''

#importing modules
import pygame
import copy
import time

healthvalue1=200
healthvalue2=200

#Class for highscore
def highscore(n1,n2,w):
    
    f1=open('Highscore.txt','a+')
    
    f1.write('\n'+n1+'     '+n2+'      '+w)
    f1.flush()
    f1.seek(0)
    score=f1.read()
    return score.split('\n')
    

#Class for defining players attributes

class player:
    
    def __init__(self,name1,name2):
        
        
        self.name1 = name1
        self.charge1=0
        self.bg=pygame.image.load('Background.JPG')
        self.attno1=0
        self.name2 = name2
        self.charge2=0
        self.attno2=0
        
        #Assigning image variables for player1        
        if self.name1 == 'goku':
            self.image1=pygame.image.load('goku/goku.png')
            self.ch1=pygame.image.load('goku/charge.png')
            self.att1=pygame.image.load('goku/kamehameha2.png')
            self.uatt1=pygame.image.load('goku/hame goku.png')
        elif self.name1=='vegeta':
            self.image1=pygame.image.load('vegeta/vegeta.png')
            self.ch1=pygame.image.load('vegeta/vch.png')
            self.att1=pygame.image.load('vegeta/vab2ch.png')
            self.uatt1=pygame.image.load('vegeta/vff.png')
        elif self.name1=='pikkon':
            self.image1=pygame.image.load('pikkon/pikkon.png')
            self.ch1=pygame.image.load('pikkon/pcharge.png')
            self.att1=pygame.image.load('pikkon/pturnado.png')
            self.uatt1=pygame.image.load('pikkon/pfinish.png')
        elif self.name1=='frieza':
            self.image1=pygame.image.load('frieza/frieza.png')
            self.ch1=pygame.image.load('frieza/frch.png')
            self.att1=pygame.image.load('frieza/dball.png')
            self.uatt1=pygame.image.load('frieza/beam.png')
        elif self.name1 == 'vader':
            self.image1=pygame.image.load('vader/vader.png')
            self.ch1=pygame.image.load('vader/charge.png')
            self.att1=pygame.image.load('vader/saberthrow.png')
            self.uatt1=pygame.image.load('vader/lightning.png')


        #Assigning image variables for player2
        if self.name2 == 'goku':
            self.image2=pygame.image.load('goku/gokuf.png')
            self.ch2=pygame.image.load('goku/chargef.png')
            self.att2=pygame.image.load('goku/kamehameha2.png')
            self.uatt2=pygame.image.load('goku/hame goku f.png')
        elif self.name2 == 'vegeta':
            self.image2=pygame.image.load('vegeta/vegetaf.png')
            self.ch2=pygame.image.load('vegeta/vchf.png')
            self.att2=pygame.image.load('vegeta/vab2ch.png')
            self.uatt2=pygame.image.load('vegeta/vfff.png')

        elif self.name2 == 'pikkon':
            self.image2=pygame.image.load('pikkon/pikkonf.png')
            self.ch2=pygame.image.load('pikkon/pchargef.png')
            self.att2=pygame.image.load('pikkon/pturnado.png')
            self.uatt2=pygame.image.load('pikkon/pfinishf.png')

        elif self.name2 == 'frieza':
            self.image2=pygame.image.load('frieza/friezaf.png')
            self.ch2=pygame.image.load('frieza/frchf.png')
            self.att2=pygame.image.load('frieza/dball.png')
            self.uatt2=pygame.image.load('frieza/beamf.png')
        elif self.name2 == 'vader':
            self.image2=pygame.image.load('vader/vaderf.png')
            self.ch2=pygame.image.load('vader/charge.png')
            self.att2=pygame.image.load('vader/saberthrow.png')
            self.uatt2=pygame.image.load('vader/lightning.png')

            
        self.player1=self.image1
        self.player2=self.image2

        #Getting rectanges of player images
        self.player1rect=pygame.Rect(self.image1.get_rect())
        self.player2rect=pygame.Rect(self.image2.get_rect())

        #Loading images for healthbar and chargebar
        self.healthbar = pygame.image.load("healthbar.png")
        self.health = pygame.image.load("health.png")
        self.chargebar = pygame.image.load("chargebar.png")
        self.mana = pygame.image.load("mana.png")
        self.t=0
        
    def move(self):	#Function to move the charaters
               
        global healthvalue1,healthvalue2,n1,n2
                  
        self.player1pos=[100,512]
        keys1=[False,False,False,False,False,False]

        
            
        self.player2pos=[680,512]
        keys2=[False,False,False,False,False,False]
        temp=0
        
        pygame.mixer.music.play(-1)
        
        while 1:
           
            #Main screen and background 
            screen.blit(self.bg,[0,0])
            screen.blit(self.player1,self.player1pos)
            screen.blit(self.player2,self.player2pos)

            #'Fight' picture displaying  
            self.t+=1
            if self.t<30:
                screen.blit(pygame.image.load('fight.png'),[350,100])
                
            #Putting players on screen
            
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
            screen.blit(self.chargebar,[20,20])
            for charge in range(self.charge1):
                screen.blit(self.mana, (charge+23,23))
            #Player2 charge bar
            screen.blit(self.chargebar,[1000,20])
            for charge in range(self.charge2):
                screen.blit(self.mana, (charge+1003,23))


            
            
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

                if pygame.key.get_pressed()[pygame.K_q] and pygame.key.get_pressed()[pygame.K_w]==False and pygame.key.get_pressed()[pygame.K_a]==False and pygame.key.get_pressed()[pygame.K_s]==False and pygame.key.get_pressed()[pygame.K_d]== False and self.attno1!=1:
                    keys1[4]=True
                else:
                    keys1[4]=False
                    
                if pygame.key.get_pressed()[pygame.K_v] and pygame.key.get_pressed()[pygame.K_w]==False and pygame.key.get_pressed()[pygame.K_a]==False and pygame.key.get_pressed()[pygame.K_s]==False and pygame.key.get_pressed()[pygame.K_d]== False:
                    keys1[5]=True
                else:
                    keys1[5]=False

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

                if pygame.key.get_pressed()[pygame.K_RSHIFT] and pygame.key.get_pressed()[pygame.K_RIGHT]==False and pygame.key.get_pressed()[pygame.K_DOWN]==False and pygame.key.get_pressed()[pygame.K_LEFT]==False and pygame.key.get_pressed()[pygame.K_UP]== False and self.attno1<1:
                    keys2[4]=True
                else:
                    keys2[4]=False
                    
                if pygame.key.get_pressed()[pygame.K_RCTRL] and pygame.key.get_pressed()[pygame.K_w]==False and pygame.key.get_pressed()[pygame.K_a]==False and pygame.key.get_pressed()[pygame.K_s]==False and pygame.key.get_pressed()[pygame.K_d]== False:
                    keys2[5]=True
                else:
                    keys2[5]=False

                    
            #Player1
            if keys1[0] and self.player1pos[1]>0:
                self.player1pos[1]-=5
            if keys1[1] and self.player1pos[0]>0:
                self.player1pos[0]-=5
            if keys1[2] and self.player1pos[1]<1024:
                self.player1pos[1]+=5
            if keys1[3] and self.player1pos[1]<1280:
                self.player1pos[0]+=5

            if keys1[5]:
                if self.charge1>=1 and keys1[4]==False:
                    self.player1=self.uatt1
                    self.charge1-=1
                    if self.player1pos[1]<=self.player2pos[1]+350 and self.player1pos[1]+350>=self.player2pos[1]:
                        healthvalue2-=1
                else:
                    self.player2=self.image2
            if keys1[4]:
                self.player1=self.ch1
                self.charge1+=1
            elif not keys1[5]:
                self.player1=self.image1
                
             

                
            #Ultimate Attack code for player1

            if pygame.key.get_pressed()[pygame.K_SPACE] and self.charge1>=10:
                self.charge1-=10
                self.attno1+=1
                att1=uattack1(self.player1pos,self.att1,self.player2pos)
                
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
            if keys2[5]:
                if self.charge2>=1 and keys2[4]==False:
                    self.player2=self.uatt2
                    if temp <1:
                        temp+=1
                        self.player2pos[0]-=500
                    self.charge2-=1
                    if self.player2pos[1]<=self.player1pos[1]+350 and self.player2pos[1]+350>=self.player1pos[1]:
                        healthvalue1-=1

            if keys2[4]:
                self.player2=self.ch2
                self.charge2+=1
            elif not keys2[5] and self.player2!=self.image2 and self.player2 !=self.ch2 and temp>0:
                for i in range(temp):
                    self.player2pos[0]+=500
                    temp-=1
                    self.player2=self.image2
            elif not keys2[5]:
                self.player2=self.image2
                
                
            #Ultimate Attack code for player2

            if pygame.key.get_pressed()[pygame.K_RETURN] and self.charge2>=10:
                self.charge2-=10
                self.attno2+=1
                att2=uattack2(self.player2pos,self.att2,self.player1pos)
                

            while self.attno2>0:
                att2.attmov()
                break

                

            if healthvalue1<=0:         #Player 2 win block
                pygame.mixer.music.load(open("Extro.wav",'rb'))
                pygame.mixer.music.play(-1)
                screen.fill(0)
                myfont = pygame.font.SysFont("Terminal", 100)
                label = myfont.render("PLAYER2 WINS!!!!!!", 1, (0,15,225))
                label1= myfont.render("MAIN PROGRAMMER :Atharva", 1, (15,225,15))
                label2=myfont.render("GRAPPHIC DESIGNER:karthik", 1, (225,15,225))
                screen.blit(label, (300, 200))
                screen.blit(label1,(200,400))
                screen.blit(label2,(150,600))
                pygame.display.update()
                time.sleep(10)
                h=highscore(n1,n2,n2)#Calling the highscore function
                label3 = myfont.render("Highscore", 1, (0,225,0))
                myfont2 = pygame.font.SysFont("Broadway", 50)
                
                screen.fill(0)
                screen.blit(label3,(500,100))
                y=300
                for i in h:
                    label4 = myfont2.render(i, 1, (0,15,225))
                    screen.blit(label4,(300,y))
                    y+=50
                
                pygame.display.update()
                time.sleep(15)
                pygame.mixer.music.stop()
                break


            elif healthvalue2<=0:       #Player 1 win block
                pygame.mixer.music.load(open("Extro.wav",'rb'))
                pygame.mixer.music.play(-1)
                screen.fill(0)
                myfont = pygame.font.SysFont("Terminal", 100)
                label = myfont.render("PLAYER1 WINS!!!!!!", 1, (255,0,0))
                label1= myfont.render("MAIN PROGRAMMER :Atharva", 1, (15,225,15))
                label2=myfont.render("GRAPPHIC DESIGNER:karthik", 1, (225,15,225))
                screen.blit(label, (300, 200))
                screen.blit(label1,(200,400))
                screen.blit(label2,(150,600))
                pygame.display.update()
                time.sleep(20)
                h=highscore(n1,n2,n1)#Calling the highscore function
                label3 = myfont.render("Highscore", 1, (0,225,0))
                myfont2 = pygame.font.SysFont("Broadway", 50)
                
                screen.fill(0)
                screen.blit(label3,(500,100))
                y=300
                for i in h:
                    label4 = myfont2.render(i, 1, (0,15,225))
                    screen.blit(label4,(300,y))
                    y+=50
                
                pygame.display.update()
                time.sleep(20)
                pygame.mixer.music.stop()
                break


            try:
                pygame.display.update()
                
            except:
                
                break
            




class uattack1():       #Class for ultimate attack of player 1
    
    def __init__(self,player1pos,att,player2pos):
        self.att=att
        self.p2x=player2pos[0]
        self.p2y=player2pos[1]
        self.attpos1=copy.deepcopy(player1pos)
                                                                                                                                                                                                                                              
    def attmov(self):
        global healthvalue2
        while True:
            self.attpos1[0]+=15
            screen.blit(self.att,self.attpos1)
            if self.attpos1[0]>1000:
                p1.attno1-=1
                break
            
            if self.attpos1[0]+390>=self.p2x and self.attpos1[0]+390<=self.p2x+260 and self.attpos1[1]+390>=self.p2y and self.attpos1[1]<=self.p2y+350:
                healthvalue2-=2
                p1.attno1-=1
                break
            

            break

    
class uattack2():       #Class for ultimate attack of player 2
    
    def __init__(self,player2pos,att,player1pos):
        self.att=att
        self.p1x=player1pos[0]
        self.p1y=player1pos[1]
        self.attpos2=copy.deepcopy(player2pos)

    def attmov(self):
        global healthvalue1
        while True:
            self.attpos2[0]-=15
            screen.blit(self.att,self.attpos2)
            if self.attpos2[0]+390>=self.p1x and self.attpos2[0]<=self.p1x+260 and self.attpos2[1]+390>=self.p1y and self.attpos2[1]<=self.p1y+350:
                healthvalue1-=2
                p1.attno2-=1
                break
            if self.attpos2[0]<0:
                
                break
            break


#Main program starts 
n1=raw_input("Enter name of player 1 : ")
n2=raw_input("Enter name of player 2 : ")
pygame.mixer.init()
pygame.mixer.music.load(open("end.wav",'rb'))
pygame.mixer.music.play()

print 'Game will begin in 5.... '
time.sleep(1)
print '4........'
time.sleep(1)
print '3........'
time.sleep(1)
print '2........'
time.sleep(1)
print '1........'
time.sleep(1)

pygame.init()
screen=pygame.display.set_mode((1366,768),pygame.FULLSCREEN)

#Loading images to be displayed
goku=pygame.image.load('goku/gokupr.jpg')
vegeta=pygame.image.load('vegeta/vegetapr.png')
pikkon=pygame.image.load('pikkon/pikkonpr.jpg')
frieza=pygame.image.load('frieza/friezapr.png')
vader=pygame.image.load('vader/vaderfre.jpg')
controls=pygame.image.load('controls.png')

#Font and labels for displaing text
myfont = pygame.font.SysFont("Chiller", 100)
label = myfont.render("Choose your hero",1, (255,0,0))
label1 = myfont.render("PLAYER 1",1, (255,0,0))
labelc = myfont.render("Click to continue.......",1, (0,200,0))

i=0
j=1
k=1


#Loop for contorls page
while k:

    screen.blit(controls,[200,300])
    screen.blit(labelc,[300,20])
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            k=0
    pygame.display.update()

#Loop for character select page
while j:

    screen.fill(0)
    g=screen.blit(goku,[50,200])
    v=screen.blit(vegeta,[700,200])
    p=screen.blit(pikkon,[50,600])
    f=screen.blit(frieza,[700,600])
    r=screen.blit(vader,[600,500])
    screen.blit(label, (400, 0))
    screen.blit(label1, (450, 100))
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if g.collidepoint(pos):
                    if i ==0:
                        name1='goku'
                        i+=1
                        label1 = myfont.render("PLAYER 2", 1, (0,15,255))
                    elif i==1:
                        
                        name2='goku'
                        pygame.mixer.music.load(open("filler.wav",'rb'))
                        #object for player class
                        p1=player(name1,name2)
                        p1.move()
                        j=0
                        pygame.mixer.music.load(open("filler.wav",'rb'))
                        
                elif v.collidepoint(pos):
                    if i ==0:
                        name1='vegeta'
                        i+=1
                        label1 = myfont.render("PLAYER 2", 1, (0,15,255))
                    elif i==1:
                        
                        name2='vegeta'
                        pygame.mixer.music.load(open("filler.wav",'rb'))
                        #object for player class
                        p1=player(name1,name2)
                        p1.move()
                        j=0
                        pygame.mixer.music.load(open("filler.wav",'rb'))
                        
                elif p.collidepoint(pos):
                    if i ==0:
                        name1='pikkon'
                        i+=1
                        label1 = myfont.render("PLAYER 2", 1, (0,15,255))
                    elif i==1:
                        
                        name2='pikkon'
                        pygame.mixer.music.load(open("filler.wav",'rb'))
                        #object for player class
                        p1=player(name1,name2)
                        p1.move()
                        j=0
                        pygame.mixer.music.load(open("filler.wav",'rb'))
                        
                elif f.collidepoint(pos):
                    if i ==0:
                        name1='frieza'
                        i+=1
                        label1 = myfont.render("PLAYER 2", 1, (0,15,255))
                    elif i==1:
                        
                        name2='frieza'
                        pygame.mixer.music.load(open("filler.wav",'rb'))
                        #object for player class
                        p1=player(name1,name2)
                        p1.move()
                        j=0
                        pygame.mixer.music.load(open("filler.wav",'rb'))
                        
                elif r.collidepoint(pos):
                    if i ==0:
                        name1='vader'
                        i+=1
                        label1 = myfont.render("PLAYER 2", 1, (0,15,255))
                        pygame.mixer.music.load(open("Imperial March.mp3",'rb'))
                        pygame.mixer.music.play(-1)
                        time.sleep(5)
                        pygame.mixer.music.load(open("filler.wav",'rb'))
                        

                    elif i==1:
                        
                        name2='vader'
                        pygame.mixer.music.load(open("Imperial March.mp3",'rb'))
                        pygame.mixer.music.play(-1)
                        time.sleep(5)
                        pygame.mixer.music.load(open("filler.wav",'rb'))
                        #object for player class
                        p1=player(name1,name2)
                        p1.move()
                        j=0
                        
                        
                        

exit(0)



    
    

