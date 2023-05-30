import pygame
from food import Food
import random
import time

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3 # velocity
        self.score = 0 # players score
        self.food = Food(400, 200, 10, 10, (0, 255, 0))
        

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

        self.food.draw(win)
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getScore(self):
        return self.score
    
    def setScore(self, score):
        self.score = score

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        # Check if the player has collided with the food object
        
        if self.x < (self.food.x-10) and self.y < (self.food.y-10):
            self.score += 10
            self.updateFood()
            print("food has been eaten!")
            
            # Notify the server that the food has been eaten
            # The server can then send a message to all clients to update the gamestate

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
    
    def updateFood(self):
        x = random.randint(0, 400)
        y = random.randint(0, 300)
        self.food = Food(x, y, 10, 10, (0, 255, 0)) 

    def score(x,y):
        # font to score
        score_style = pygame.font.SysFont("bahnschrift", 30)
        
        value = score_style.render("Your Score: " + str(self.score), True, yellow)
        win.blit(value, [x, y])
    
    def msg(self, msg,color):
    
        pygame.init()

        width = 500
        height = 400

        win = pygame.display.set_mode((width, height))
        
        win.fill((0,0,0))

        font_style = pygame.font.SysFont("bahnschrift", 30)

        mesg = font_style.render(msg, True, color)

        win.blit(mesg, [width/3, height/2])

        pygame.display.update()

        time.sleep(5)

        pygame.QUIT


    


        