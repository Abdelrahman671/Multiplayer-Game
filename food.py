import pygame

class Food():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), 5)
        #(win, self.color, self.rect)