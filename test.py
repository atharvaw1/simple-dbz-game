import pygame
def highscore(n1,n2,w):
    
    f1=open('Highscore.txt','a+')
    
    f1.write('\n'+n1+'     '+n2+'      '+w)
    f1.flush()
    f1.seek(0)
    score=f1.read()
    return score.split('\n')
    

h=highscore('Atharva','Karthik','Atharva')

pygame.init()
screen=pygame.display.set_mode((1280,1024))
myfont2 = pygame.font.SysFont("Broadway", 50)
y=300
for i in h:
    label4 = myfont2.render(i, 1, (0,15,225))
    screen.blit(label4,(500,y))
    y+=50
pygame.display.update()
