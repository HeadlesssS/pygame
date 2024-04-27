import pygame
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("button")
font = pygame.font.SysFont("Georgia",40,bold=True)

start_img =pygame.image.load("start_btn.png")
start_img =pygame.image.load("start_btn.png")

while True:
    for events in pygame.event.get():
        if events.type ==pygame.QUIT:
            pygame.quit()
        
    pygame.display.update()

