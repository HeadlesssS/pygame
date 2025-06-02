import pygame
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("button")
font = pygame.font.SysFont("Georgia",40,bold=True)

start_img =pygame.image.load("pygames/start_btn.png")
end_img =pygame.image.load("pygames/exit_btn.png")

while True:
    for events in pygame.event.get():
        if events.type ==pygame.QUIT:
            pygame.quit()
    screen.blit(start_img,(300,100))
    screen.blit(end_img,(300,400))
    pygame.display.update()

