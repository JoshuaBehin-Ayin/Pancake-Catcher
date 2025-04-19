import random
import pygame
from pygame.locals import * 
pygame.init()

class Pancakes(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
      
        self.image = pygame.image.load("illustration-pancakes-dish-on-white-260nw-117508222 (1).png").convert_alpha()
        self.rect = self.image.get_rect() 

        
        self.rect.left = random.randrange(0,screen.get_width()-self.rect.width)
        self.rect.top = 0
        self.dir_x = 0
        self.dir_y = 1
        self.speed = random.randrange(2,5)
        
        
    

     
    def update(self):
        global score
        global lives
        self.rect.move_ip(self.speed*self.dir_x, self.speed*self.dir_y)
        
        if self.rect.bottom >= screen.get_height():
            self.rect.left = random.randrange(0,screen.get_width()-self.rect.width)
            self.rect.top = 0
            lives-=1

        if img_rect.colliderect(self.rect):
            self.rect.left = random.randrange(0,screen.get_width()-self.rect.width)
            self.rect.top = 0
            score+=1
          
        
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        
        self.image = pygame.image.load("727-7276345_maple-syrup-png-picture-canadian-maple-syrup-clipart (1).png").convert_alpha()
        self.rect = self.image.get_rect() 

        
        
        
            
        self.rect.left = random.randrange(0,screen.get_width()-self.rect.width)
        self.rect.bottom = random.randrange(470,480)

        

      
class FryingPan(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   
      
        
            
        
            
        



screen = pygame.display.set_mode((640, 480))

score=0
lives=5
img=pygame.image.load("close-frying-pan-wooden-handle-260nw-263535851.png").convert_alpha()

img_rect=img.get_rect()
img_rect.left = 260
img_rect.bottom = 480

pancake1=Pancakes()
pancake2=Pancakes()
pancake3=Pancakes()
pancake4=Pancakes()


pancake_group=pygame.sprite.Group(pancake1,pancake2,pancake3,pancake4)
syrup=PowerUp()
#for i in range(1000):
  #if i%100==0:
    #block=Block((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
gameOver = pygame.Surface(screen.get_size()).convert()
gameOver.fill((0, 0, 0))
powerUp_group=pygame.sprite.Group(syrup)
background = pygame.Surface(screen.get_size()).convert()
background.fill((0, 0, 255))
screen.blit(background, (0,0))
screen.blit(img, img_rect)
clock = pygame.time.Clock()
keep_going = True

while keep_going:
    
        

    clock.tick(30)
    pygame.event.pump() 
    keys = pygame.key.get_pressed()
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
        
    if keys[K_RIGHT] and img_rect.right<640:
        img_rect.right+=20
        
    elif keys[K_LEFT] and img_rect.left>0:
        img_rect.right-=20
        
    
    
    
    #pygame.sprite.spritecollide(img_rect, powerUp_group, True)
    

        
        
    my_font = pygame.font.SysFont("comicsansms", 30) 


    
    


    label1 = my_font.render(f"Score: {score}", True, (0,0,0))
    label2 = my_font.render(f"Lives: {lives}", True, (0,0,0))
    
   
    
    
    screen.blit(background, (0,0))
    screen.blit(label1, (540, 10))
    screen.blit(label2, (0, 10))
    pancake_group.clear(screen, background)

    powerUp_group.clear(screen, background)
      
    pancake_group.update()
    
    powerUp_group.draw(screen)
    pancake_group.draw(screen)
    
    screen.blit(img, img_rect)
    if lives<1:
        my_font1 = pygame.font.SysFont("comicsansms", 70) 
        label3 = my_font1.render("Game Over", True, (255,0,0))
        screen.blit(gameOver, (0,0))
        screen.blit(label3, (190, 220))
        
    pygame.display.flip()

    pygame.display.update()