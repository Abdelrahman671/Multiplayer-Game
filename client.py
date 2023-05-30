import pygame
import time
import random
from network import Network
from player import Player
pygame.init()

# Colors Config:
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Window Configs:
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

# font to lose msg
font_style = pygame.font.SysFont("bahnschrift", 30)

# final score which players should reach to win
final_score = pygame.font.SysFont("bahnschrift", 20)

# game_score
gameScore = 100

def redrawWindow(win,player1, player2):

    win.fill(black)
    win.blit(final_score.render("Final Score: 100", True, white), [0,0])

    # players score
    players_score(player1.score, 200, 0, "Player1 ")
    players_score(player2.score, 400, 0, "Player2 ")

    # initialize players
    player1.draw(win)
    player2.draw(win)

    pygame.display.update()

def message(msg, color):
    """ In case if the player exceeds boundaries of the window """
    win.fill(black)
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width/3, height/2])
    pygame.display.update()
    time.sleep(3)
    pygame.QUIT

def players_score(score,x,y, player):
    score_style = pygame.font.SysFont("bahnschrift", 18)
    value = score_style.render(str(player) + "Score: " + str(score), True, yellow)
    win.blit(value, [x,y])


def main():
    run = True
    n = Network()
    p1 = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p1)

        valX = p1.getX()
        valY = p1.getY()
        
        # restrict players from window boundaries
        if valX >= width+20 or valX < -30 or valY >= height+30 or valY < -30:
            run = False
            message("You Lost!", red)

  
        if p1.score == gameScore:
                run = False
                p1.msg("Player1 Win!",yellow)
        elif p2.score == gameScore:
                run = False
                p2.msg("Player2 Win!",yellow)
               

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move()
        redrawWindow(win, p1, p2)

main()