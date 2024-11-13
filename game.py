################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt
# Teema: Videomäng
#
#
# Autorid: Victoria Grau, Hedvig Annast
#
# mõningane eeskuju: Fruit-catcher tüüpi mängud, platformerid
#
# Lisakommentaar (nt käivitusjuhend):
#
##################################################


import pygame, sys
from random import randint
from pygame import mixer
import button
pygame.init()
mixer.init()
screen_width= 1920
screen_height= 1080
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Game")


#variables
game_paused=False
menu_state ="main"

#font
font= pygame.font.SysFont("arialblack",40)
font2= pygame.font.SysFont("arialblack",20)

#color
text_col= (255,255,255)
pink= (255,192,203)

#load img
resume_img = pygame.image.load("button_resume.png").convert_alpha()
quit_img = pygame.image.load("button_quit.png").convert_alpha()
#button
resume_button = button.Button(10,10, resume_img, 1)
quit_button = button.Button(10,110, quit_img, 1)


def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))
    
#taustamuusika
mixer.music.load('HOME.mp3')
mixer.music.set_volume(0.05)
mixer.music.play()
#backgorund
pilt2 = pygame.image.load("background.jpg")
pilt2 = pygame.transform.scale(pilt2, (1920, 1080))
pilt3 = pygame.image.load("background2.jpg")
pilt3 = pygame.transform.scale(pilt3, (1920, 1080))

#player
samm=25
pilt = pygame.image.load("player.png")
pilt = pygame.transform.scale(pilt, (305, 324))

x = 775
y = 796

rect = pilt.get_rect()
rect.topleft = (x, y)

#fruits
apple = pygame.image.load("apple.png")
apple = pygame.transform.scale(apple, (147, 183))
mango = pygame.image.load("mango.png")
mango = pygame.transform.scale(mango, (170, 170))
banana = pygame.image.load("banana.png")
banana = pygame.transform.scale(banana, (180, 150))
peach = pygame.image.load("peach.png")
peach =  pygame.transform.scale(peach, (200, 230))
maasikas = pygame.image.load("maasikas.png")
maasikas =  pygame.transform.scale(maasikas, (170, 170))

#apple
x2 = randint(0,1845)
y2 = 0
rect2 = apple.get_rect()
rect2.topleft = (x2, y2)
#mango
x3 = randint(0,1845)
y3 = 0
rect3 = mango.get_rect()
rect3.topleft = (x3, y3)
#banana
x4 = randint(0,1845)
y4 = 25
rect4 = banana.get_rect()
rect4.topleft = (x4, y4)
#peach
x5 = randint(0,1845)
y5 = 0
rect5 = peach.get_rect()
rect5.topleft = (x5, y5)
#maasikas
x6 = randint(0,1845)
y6 = 0
rect6 = maasikas.get_rect()
rect6.topleft = (x6, y6)


#punktid
punktid=0



#loop
pygame.key.set_repeat(1,10)
run=True
while run:
    screen.blit(pilt2, (0,0))
    #paused?
    if game_paused== True:
        if menu_state == "main":
            screen.blit(pilt3, (0,0))
            
            if resume_button.draw(screen):
                game_paused=False
            if quit_button.draw(screen):
                run=False
    else:
        draw_text("Press SPACE to pause", font2,text_col,5,5)
        draw_text(f"score: {punktid}", font2,pink,5,25)
        if rect.colliderect(rect2):
            punktid+=1
        elif rect.colliderect(rect3):
            punktid+=1
        elif rect.colliderect(rect4):
            punktid+=1
        elif rect.colliderect(rect5):
            punktid+=1
        elif rect.colliderect(rect6):
            punktid+=1
            
    #pildid
    if game_paused== False:
        mixer.music.unpause()
        screen.blit(pilt, (x,y))
        screen.blit(apple, (x2,y2))
        screen.blit(mango, (x3,y3))
        screen.blit(banana, (x4,y4))
        screen.blit(maasikas, (x5,y5))
        screen.blit(peach, (x6,y6))
        rect.topleft=(x, y)
        rect2.topleft=(x2, y2)
        rect3.topleft=(x3, y3)
        rect4.topleft=(x4, y4)
        rect5.topleft=(x5, y5)
        rect6.topleft=(x6, y6)
        #pildi rectangelid ifid
        y2 += 3
        if y2 >= 897:
            y2 = 0
            x2= randint(0,1845)
        if rect.colliderect(rect2):
            y2 = 0
            x2= randint(0,1845)
            
        y3 += 2
        if y3 >= 910:
            y3 = 0
            x3= randint(0,1845)
        if rect.colliderect(rect3):
            y3 = 0
            x3= randint(0,1845)
            
        y4 += 3.5
        if y4 >= 946:
            y4 = 0
            x4= randint(0,1845)
        if rect.colliderect(rect4):
            y4 = 0
            x4= randint(0,1845)
            
        y5 += 2.5
        if y5 >= 910:
            y5 = 0
            x5= randint(0,1845)
        if rect.colliderect(rect5):
            y5 = 0
            x5= randint(0,1845)
            
        y6 += 2.75
        if y6 >= 870:
            y6 = 0
            x6= randint(0,1845)
        if rect.colliderect(rect6):
            y6 = 0
            x6= randint(0,1845)
    else:
        mixer.music.pause() 
    #nupud ja asjad
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.KEYDOWN:
            if i.key==pygame.K_SPACE:
                game_paused=True
            elif i.key == pygame.K_LEFT and x>=5:
                x = x - samm
            elif i.key == pygame.K_RIGHT and x<=1596:
                x = x + samm
            
    pygame.display.update()


pygame.quit()