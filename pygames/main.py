import pygame
import math
import random
from pygame import mixer

#just initializing the game..
pygame.init()

#Creating the screen
screen=pygame.display.set_mode((800,600))

#background
background=pygame.image.load("background.png")

#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

#Title and Icon
pygame.display.set_caption("Hunterrrrrr")
icon= pygame.image.load("drippp.png")
pygame.display.set_icon(icon)


#player
playerImg=pygame.image.load("it.png")
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
    enemyImg.append(pygame.image.load("duck.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#Bullet 
#ready=cant see being ready
#fire=bullet shot

BulletImg=pygame.image.load("bullet.png")
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
    over_text=over_font.render("GAME OVER",True, (255,255,255) )
    screen.blit(over_text,(200,250))
    

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



# Game Loop
running=True
while running:
    screen.fill((0,0,0))
#background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#keystroke is event and we are checking it is right or left
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change-=3
            if event.key == pygame.K_RIGHT:
                 playerX_change+=3

            if event.key == pygame.K_UP:
                 playerY_change-=3
            if event.key == pygame.K_DOWN:
                 playerY_change+=3
                 #ya niri bulelt X player X sanga equal huda kina bullet straight? kinaki the playerx 
                 #is constantly changing tala playerX+=playerX + playerX_change gareko xa
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # get x-coordinate of the spaceship
                    bullet_Sound=mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

#checking for boundaries
    playerX+=playerX_change
    playerY+=playerY_change

    if playerX<=-0:
        playerX=-0
    elif playerX>=736:
        playerX =736

    if playerY<=0:
        playerY=0
    elif playerY>=536:
        playerY =536

#enemy ko movement
    for i in range(num_of_enemies):
        #game over
        if enemyY[i] >550:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break
            
            
        enemyX[i]+=enemyX_change[i]

        if enemyX[i]<=0:
            enemyX_change[i]=2
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-2
            enemyY[i]+=enemyY_change[i]
           
    #collision check
        collision= isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            #explosion ko sound
            explosion_Sound=mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY=playerY
            bullet_state="ready"
            score_value+=1
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(50,150)
            
        enemy(enemyX[i],enemyY[i],i)
        
    #bullet movement
    if bulletY <= 0:
            bulletY = playerY
            bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
     
    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()