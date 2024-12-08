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
# Lisakommentaar:
# Praeguses alpha-versioonis ei tööta menu nupud, seega mängu sulgemiseks tuleb see kinni panna Thonnys stopi kasutades.
# Praegused pildid on placeholderid, plaanis on kõik ise luua.
# Praegusele valmisolevale gamemodeile tahame ideaalis lisada ka objektid, mida püüda ei tohi ja elud. Algses plaanis kavatsesime teha 2 gamemodei,
# aga võisime olla veidi liiga ambitsioonikad.
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
#background
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
bambooshoot = pygame.image.load("bambooshoot.png")
bambooshoot = pygame.transform.scale(bambooshoot, (147, 183))
bamboosegment = pygame.image.load("bamboosegment.png")
bamboosegment = pygame.transform.scale(bamboosegment, (170, 170))
evilbamboo = pygame.image.load("evilbambooshoot.png")
evilbamboo = pygame.transform.scale(evilbamboo, (147, 183))


x2 = randint(100,1745)
y2 = 0
rect2 = bamboosegment.get_rect()
rect2.topleft = (x2, y2)

x3 = randint(100,1745)
y3 = 0
rect3 = bambooshoot.get_rect()
rect3.topleft = (x3, y3)

x4 = randint(100,1745)
y4 = 25
rect4 = evilbamboo.get_rect()
rect4.topleft = (x4, y4)


#punktid
punktid=0
elud = 5


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
            elud-=1
            if elud == 0:
                game_paused = True

            
    #pildid
    if game_paused== False:
        mixer.music.unpause()
        screen.blit(pilt, (x,y))
        screen.blit(bamboosegment, (x2,y2))
        screen.blit(bambooshoot, (x3,y3))
        screen.blit(evilbamboo, (x4,y4))

        rect.topleft=(x, y)
        rect2.topleft=(x2, y2)
        rect3.topleft=(x3, y3)
        rect4.topleft=(x4, y4)

        #pildi rectangelid ifid
        y2 += 3
        if y2 >= 897:
            y2 = 0
            x2= randint(100,1745)
        if rect.colliderect(rect2):
            y2 = 0
            x2= randint(100,1745)
            
        y3 += 2.5
        if y3 >= 910:
            y3 = 0
            x3= randint(100,1745)
        if rect.colliderect(rect3):
            y3 = 0
            x3= randint(100,1745)
            
        y4 += 2
        if y4 >= 946:
            y4 = 0
            x4= randint(100,1745)
        if rect.colliderect(rect4):
            y4 = 0
            x4= randint(100,1745)
            

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