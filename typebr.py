import pygame as py 
      
HEIGHT=800
WIDTH=400

screen=py.display.set_mode((HEIGHT,WIDTH),py.FULLSCREEN)
name=py.display.set_caption("jumpy")


class Game:
    def __init__(self) -> None:
        self.run=True
    
    def draw(self):
        rect.center=screen.get_rect().center
        rect=py.Rect(rect.center,200,200)
        rect1=py.draw.rect(screen,(0,255,255),rect)
        
        py.display.flip()

game=Game()
while game.run:
    for event in py.event.get():
        if event.type == py.QUIT:
            game.run=False
        if event.type==py.VIDEORESIZE:
            pass
    game.draw()