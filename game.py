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
from random import randint, choice
from pygame import mixer
import button
pygame.init()
mixer.init()
screen_width= 1920
screen_height= 1080
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Game")

def salvesta_highscore(p):
    try:
        with open('score.txt', 'r+', encoding='utf-8') as f:
            score = f.readline() 
            if score:
                score = int(score.strip()) 
                if score < p:  
                    f.seek(0)  
                    f.write(str(p)) 
                    f.truncate() 
            else: 
                f.write(str(p))
    except FileNotFoundError:
        with open('score.txt', 'w', encoding='utf-8') as f:
            f.write(str(p))
            
def loe_highscore():
    with open('score.txt', 'r', encoding='utf-8') as f:
        score = f.readline()
        score = int(score.strip())
        return score

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    imgrect = img.get_rect()
    imgrect.center = (x//2, y//2)
    screen.blit(img,(x,y))

#variables
game_paused=False
menu_state ="main"

#font
font= pygame.font.SysFont("arialblack",55)
font2= pygame.font.SysFont("arialblack",35)

#color
text_col= (0,0,0)
pink= (255,192,203)

#load img
resume_img = pygame.image.load("button_resume.png").convert_alpha()
quit_img = pygame.image.load("button_quit.png").convert_alpha()
#button
resume_button = button.Button(10,10, resume_img, 1)
quit_button = button.Button(10,110, quit_img, 1)
   
#taustamuusika
mixer.music.load('HOME.mp3')
mixer.music.set_volume(0.05)
mixer.music.play(-1)
#background
pilt2 = pygame.image.load("background.jpg")
pilt2 = pygame.transform.scale(pilt2, (1920, 1080))
pilt3 = pygame.image.load("background2.jpg")
pilt3 = pygame.transform.scale(pilt3, (1920, 1080))

#player
samm=25
pilt = pygame.image.load("player.png")
pilt = pygame.transform.scale(pilt, (340, 340))
pilt_shift = pygame.image.load("player_shift.png")
pilt_shift = pygame.transform.scale(pilt_shift, (340, 340))

x = 775
y = 796

rect = pilt.get_rect()
rect.topleft = (x, y)

#objektid
bambooshoot = pygame.image.load("bambooshoot.png")
bambooshoot = pygame.transform.scale(bambooshoot, (120, 120))
bamboosegment = pygame.image.load("bamboosegment.png")
bamboosegment = pygame.transform.scale(bamboosegment, (120, 120))

harmful_images = [
    pygame.image.load("kott.png").convert_alpha(),
    pygame.image.load("kivi.png").convert_alpha(),
    pygame.image.load("straw.png").convert_alpha(),
    pygame.image.load("kork.png").convert_alpha()
]
harmful_images = [pygame.transform.scale(img, (int(120 * 0.75), int(120 * 0.75))) for img in harmful_images]

current_harmful_image = choice(harmful_images)

x2 = randint(100,1745)
y2 = -120
rect2 = bamboosegment.get_rect()
rect2.topleft = (x2, y2)

x3 = randint(100,1745)
y3 = -120
rect3 = bambooshoot.get_rect()
rect3.topleft = (x3, y3)

x4 = randint(100, 1745)
y4 = -120
rect4 = current_harmful_image.get_rect()
rect4.topleft = (x4, y4)


#punktid
punktid=0
elud = 5


#loop
pygame.key.set_repeat(1,10)
run=True
while run:
    screen.blit(pilt2, (0,0))
    #paused
    if game_paused== True:
        if menu_state == "main":
            screen.blit(pilt3, (0,0))
            if elud == 0:
                salvesta_highscore(punktid)
                draw_text("Mäng läbi, elud otsas!", font2,text_col,700,470)
                draw_text(f"Sinu punktid: {punktid}", font2,text_col,700,500)
                draw_text(f"Parim tulemus: {loe_highscore()}", font2,text_col,700,530)
            if resume_button.draw(screen):
                game_paused=False
            if quit_button.draw(screen):
                run=False
    else:
        draw_text("Press SPACE to pause", font2,text_col,5,5)
        draw_text(f"score: {punktid}", font2,pink,5,35)
        draw_text(f"elud: {elud}", font2,pink,5,65)
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
        
        keys = pygame.key.get_pressed()
        normal_speed = samm // 6  
        shift_speed = int(normal_speed * 3)  

        step = shift_speed if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else normal_speed

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x >= 5:
            x -= step
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x <= 1596:
            x += step

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            screen.blit(pilt_shift, (x, y))  
        else:
            screen.blit(pilt, (x, y)) 

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x >= 5:
            x -= step
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x <= 1596:
            x += step

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            screen.blit(pilt_shift, (x, y))  
        else:
            screen.blit(pilt, (x, y)) 


        screen.blit(bamboosegment, (x2,y2))
        screen.blit(bambooshoot, (x3,y3))
        screen.blit(current_harmful_image, (x4, y4))

        rect.topleft=(x, y)
        rect2.topleft=(x2, y2)
        rect3.topleft=(x3, y3)
        rect4.topleft =(x4, y4)

        #pildi rectangelid ifid
        # Bamboosegment 
        y2 += 3
        if y2 >= 1080:  
            y2 = -120  
            x2 = randint(100, 1745)
        if rect.colliderect(rect2):  
            y2 = -120  
            x2 = randint(100, 1745)

        # Bambooshoot
        y3 += 2.5
        if y3 >= 1080:  
            y3 = -120  
            x3 = randint(100, 1745)
        if rect.colliderect(rect3):  
            y3 = -120  
            x3 = randint(100, 1745)

        # Harmful object 
        y4 += 1  
        rect4.topleft = (x4, y4)  

        if y4 >= 1080:  
            y4 = -120*0.75  
            x4 = randint(100*0.75, 1835)
            current_harmful_image = choice(harmful_images)  
            rect4 = current_harmful_image.get_rect()  
            rect4.topleft = (x4, y4)

        if rect.colliderect(rect4): 
            elud -= 1  

            if elud == 0: 
                game_paused = True

            y4 = -120*0.75  
            x4 = randint(100*0.75, 1835)
            current_harmful_image = choice(harmful_images)  
            rect4 = current_harmful_image.get_rect()  
            rect4.topleft = (x4, y4)
            

    else:
        mixer.music.pause() 
    #nupud ja asjad
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                game_paused = True


            
    pygame.display.update()


pygame.quit()