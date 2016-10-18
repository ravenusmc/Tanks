import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
yellow = (200,200,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')

clock = pygame.time.Clock()

block_size = 10
FPS = 30

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

##Functions
def pause():
    
    paused = True
    message_to_screen("Paused", black, -100, "large")
    message_to_screen("Press c to continue or q to quit", black, 25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #gameDisplay.fill(white)

        clock.tick(10)

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])
    
def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - block_size))
    randAppleY = round(random.randrange(0, display_height - block_size))

    return randAppleX,randAppleY

def game_intro():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks", green, -100, "large")
        message_to_screen("The objective is to shoot and destroy",
                          black,
                          10,
                          "small")
        message_to_screen("The enemy tank before they destroy you.",
                          black,
                          50,
                          "small")
        message_to_screen("The more enemies you destroy the harder they get!",
                          black,
                          100,
                          "small")
        pygame.draw.rect(gameDisplay, green, (150,500,100,50))
        pygame.draw.rect(gameDisplay, yellow, (350,500,100,50))
        pygame.draw.rect(gameDisplay, red, (550,500,100,50))
        
        pygame.display.update()
        clock.tick(15)

    
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()
    
def message_to_screen(msg, color, y_displace=0, size= "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

    
#main game function
def gameLoop():

    gameExit = False
    gameOver = False

    while not gameExit:

        if gameOver == True:
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Press C to play agian or Q to Quit", black, 50, size="medium")
            pygame.display.update()

        while gameOver == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameEXIT = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                    pause()

    
    
        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(FPS)
        
    pygame.quit()
    quit()

game_intro()
gameLoop()

            
        

