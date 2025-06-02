#add menu ani game over vayesi restart
import pygame,asyncio
import math

import random
from pygame import mixer

import button

#just initializing the game..
pygame.init()


#Creating the screen
screen=pygame.display.set_mode((800,600),pygame.RESIZABLE)

#background
background=pygame.image.load("resources/background.png")

#background sound
mixer.music.load('resources/background.wav')
mixer.music.play(-1)

#Title and Icon
pygame.display.set_caption("Hunterrrrrr")
icon= pygame.image.load("resources/drippp.png")
pygame.display.set_icon(icon)

#buttons
resume_img=pygame.image.load("resources/resume.png").convert_alpha()
resumebtn=button.Button(200,150,resume_img,0.9)

restart_img=pygame.image.load("resources/restart.png").convert_alpha()
restartbtn=button.Button(180,350,restart_img,0.5)


#player
playerImg=pygame.image.load("resources/it.png")
playerX=380
playerY=480
playerX_change =0
playerY_change=0

enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

#ENEMY
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("resources/duck.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#Bullet 
#ready=cant see being ready
#fire=bullet shot

BulletImg=pygame.image.load("resources/bullet.png")
bulletX=0
bulletY=playerY
bulletX_change=0
bulletY_change=5
bullet_state="ready"

#score
score_value=0
font = pygame.font.Font('freesansbold.ttf', 32)

#game over
over_font = pygame.font.Font('freesansbold.ttf', 32)

textX=10
textY=10

def show_score(x,y):
    #typecasting
    score=font.render("Score :" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
    
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    instr_text = over_font.render("Press R to Restart", True, (255, 255, 255))
    screen.blit(instr_text, (100, 300))


def pause_text():
    over_text = over_font.render("Paused", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(BulletImg,(x+16,y+16))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + ( math.pow(enemyY-bulletY,2)))
    return distance < 30

def playerCollision(enemyX,enemyY,playerX,playerY):
    distance = math.sqrt((math.pow(enemyX-playerX,2)) + ( math.pow(enemyY-playerY,2)))
    return distance < 30

async def main():
    global playerX,playerY,enemyX,enemyY, playerX_change, playerY_change, bulletX, bulletY, bullet_state, score_value
    running = True
    paused = False
    game_over = False  # Track if game is lost

    while running:
        screen.fill((0,0,0))
        screen.blit(background,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not paused and not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        playerX_change -= 3
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        playerX_change += 3
                    if event.key == pygame.K_SPACE:
                        if bullet_state == "ready":
                            bullet_Sound = mixer.Sound('resources/laser.wav')
                            bullet_Sound.play()
                            bulletX = playerX
                            fire_bullet(bulletX, bulletY)
                    if event.key == pygame.K_p:
                        paused = True 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                        playerX_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                        playerY_change = 0
            elif paused:
                # Listen for unpause/restart key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False  # Unpause when P is pressed
                    if event.key == pygame.K_r:
                        # Reset game state
                        playerX = 380
                        playerY = 480
                        playerX_change = 0
                        playerY_change = 0
                        bulletX = 0
                        bulletY = playerY
                        bullet_state = "ready"
                        score_value = 0
                        for i in range(num_of_enemies):
                            enemyX[i] = random.randint(0, 736)
                            enemyY[i] = random.randint(50, 150)
                        paused = False
                        game_over = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resumebtn.is_clicked(event.pos):
                        paused = False  
                    if restartbtn.is_clicked(event.pos):
                        playerX = 380
                        playerY = 480
                        playerX_change = 0
                        playerY_change = 0
                        bulletX = 0
                        bulletY = playerY
                        bullet_state = "ready"
                        score_value = 0
                        for i in range(num_of_enemies):
                            enemyX[i] = random.randint(0, 736)
                            enemyY[i] = random.randint(50, 150)
                        paused = False
                        game_over = False
            elif game_over:
                # Listen for restart key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Reset game state
                        playerX = 380
                        playerY = 480
                        playerX_change = 0
                        playerY_change = 0
                        bulletX = 0
                        bulletY = playerY
                        bullet_state = "ready"
                        score_value = 0
                        for i in range(num_of_enemies):
                            enemyX[i] = random.randint(0, 736)
                            enemyY[i] = random.randint(50, 150)
                        paused = False
                        game_over = False

        if not paused and not game_over:
            #checking for boundaries
            playerX += playerX_change
            playerY += playerY_change

            if playerX <= 0:
                playerX = 0
            elif playerX >= 736:
                playerX = 736

            if playerY <= 0:
                playerY = 0
            elif playerY >= 536:
                playerY = 536

            #enemy ko movement
            for i in range(num_of_enemies):
                #game over
                if enemyY[i] > 500:
                    for j in range(num_of_enemies):
                        enemyY[j] = 2000
                    game_over = True  
                    # Set game over state
                    break

                enemyX[i] += enemyX_change[i]

                if enemyX[i] <= 0:
                    enemyX_change[i] = 2
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -2
                    enemyY[i] += enemyY_change[i]

                #collision check
                collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collision:
                    explosion_Sound = mixer.Sound('resources/explosion.wav')
                    explosion_Sound.play()
                    bulletY = playerY
                    bullet_state = "ready"
                    score_value += 1
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(50, 150)
                enemy(enemyX[i], enemyY[i], i)

                collision = playerCollision(enemyX[i], enemyY[i], playerX, playerY)
                if collision:
                    explosion_Sound = mixer.Sound('resources/explosion.wav')
                    explosion_Sound.play()
                    bulletY = playerY
                    bullet_state = "ready"
                    score_value = 0
                    game_over = True 
                    break

            #bullet movement
            if bulletY <= 0:
                bulletY = playerY
                bullet_state = "ready"

            if bullet_state == "fire":
                fire_bullet(bulletX, bulletY)
                bulletY -= bulletY_change

            player(playerX, playerY)
            show_score(textX, textY)
        elif paused:
            pause_text()
            resumebtn.draw(screen) 
            restartbtn.draw(screen)
        elif game_over:
            game_over_text()

        pygame.display.update()
        await asyncio.sleep(0)

asyncio.run(main())