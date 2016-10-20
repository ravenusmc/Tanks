import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
light_green = (0,155,0)
green = (0,255,0)
yellow = (200,200,0)
light_yellow = (255,255,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')

clock = pygame.time.Clock()

#Tank Variables

tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5

block_size = 10
FPS = 30

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

##Functions
def tank(x,y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x-27, y-2),
                        (x-26, y-5),
                       (x-25, y-8),
                       (x-23, y-12),
                       (x-20, y-14),
                       (x-18, y-15),
                       (x-15, y-17),
                       (x-13, y-19),
                       (x-11, y-21)
                       ]


    pygame.draw.circle(gameDisplay, black, (x,y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight ))

    pygame.draw.line(gameDisplay, black, (x,y), possibleTurrets[turPos], turretWidth)

    
    #Drawing the wheels
    pygame.draw.circle(gameDisplay, black, (x-15, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x-10, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x-5, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x+5, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x+10, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x+15, y+20), wheelWidth)
    

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

def barrier(xlocation, randomHeight):
    pygame.draw.rect(gameDisplay, black, [xlocation, display_height-randomHeight, 50, randomHeight])

    
def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])
    
def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - block_size))
    randAppleY = round(random.randrange(0, display_height - block_size))

    return randAppleX,randAppleY

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size ='small'):
        textSurf, textRect = text_objects(msg,color,size)
        textRect.center = ((buttonx + (buttonwidth/2)), buttony+(buttonheight/2))
        gameDisplay.blit(textSurf, textRect)

def game_controls():
    
    gcont = True

    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.fill(white)
        message_to_screen("Controls", green, -100, "large")
        message_to_screen("Fire: Spacebar",
                          black,
                          -30,
                          "small")
        message_to_screen("Move turret Up and Down arrows",
                          black,
                          10,
                          "small")
        message_to_screen("Move Tank: Left and Right Arrows",
                          black,
                          50,
                          "small")
        message_to_screen("Pause: p",
                  black,
                  90,
                  "small")

        button("Play", 150,500,100,50, green, light_green, action="play" )
        button("Main Menu",350,500,100,50, yellow, light_yellow, action="main")
        button("Quit", 550,500,100,50, red, light_red, action="quit")
        
        pygame.display.update()
        clock.tick(15)

def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "controls":
                game_controls()
            if action == "play":
                gameLoop()
            if action == "main":
                game_intro()
            
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))
    text_to_button(text, black, x, y, width, height)
        

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

        button("Play", 150,500,100,50, green, light_green, action="play" )
        button("Controls",350,500,100,50, yellow, light_yellow, action="controls")
        button("Quit", 550,500,100,50, red, light_red, action="quit")
        
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
    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0

    currentTurPos = 0
    changeTur = 0

    xlocation = (display_width / 2) + random.randint(-0.2 * display_width, 0.2 * display_width)
    randomHeight = random.randrange(display_height * 0.1, display_height * 0.6)

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
                    tankMove = -5
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5
                elif event.key == pygame.K_UP:
                    changeTur = 1
                elif event.key == pygame.K_DOWN:
                    changeTur = -1
                elif event.key == pygame.K_p:
                    pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0
                

        gameDisplay.fill(white)
        mainTankX += tankMove
        currentTurPos += changeTur
        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0
        tank(mainTankX, mainTankY, currentTurPos)
        barrier(xlocation, randomHeight)
        pygame.display.update()
        clock.tick(FPS)
        
    pygame.quit()
    quit()

game_intro()
gameLoop()

            
        

