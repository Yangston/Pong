"""
-images MUST be saved in the same location of python file
-origin is at the top left. positive x is normal positive y goes down
"""

import pygame
import random
import time

#starts running pygame
pygame.init()

#all caps are constants. constans never change
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

#colour of background and stuff
WHITE = (245, 245, 245)
BLACK = (255, 45, 67)

#width of image
CAR_WIDTH = 73
CAR_HEIGHT = 73

#sets up clock and handles fps
clock = pygame.time.Clock()

#find this image and save into variable
carImg = pygame.image.load('racecar.png')


#this creates a game window with said width and height
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

#names window
pygame.display.set_caption('Your first game!')

#tells computer to draw the image at this specific location
def car(x, y):
    gameDisplay.blit(carImg, (x, y))

#draws the rectangle with given dimensions and colours
def obstacles(obstacleX, obstacleY, obstacleWidth, obstacleHeight, colour):
    pygame.draw.rect(gameDisplay, colour, [obstacleX, obstacleY, obstacleWidth, obstacleHeight])             

#creating invisiable rectangle to hold text
def textObjects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()#get rect is to get rectangle

#declares what text to display
def crash():
    messageDisplay('You Crashed!')

#handles text commands
def messageDisplay(text):
    #declares what font to use and size to display
    largeText = pygame.font.SysFont('mongolianbaiti', 115)
    #calls other functions
    textSurf, textRect = textObjects(text, largeText)
    #where to place the text
    textRect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/2))
    #displays picture
    gameDisplay.blit(textSurf, textRect)
    #updates the image on screen
    pygame.display.update()
    #time delay or how long the text stays on the screen
    time.sleep(2)
    #continues game loop
    gameLoop()

def welcome():
    messageDisplay('Welcome!')

def obstacleDodged(count):
    #details of wording
    font = pygame.font.SysFont('Comic Sans MS', 25)
    text = font.render("Score: " + str(count), True, BLACK)
    gameDisplay.blit(text, (675, 565))

#the game loop
def gameLoop():
    #delcares locatrion of the car (the width of window multiplied by said value
    x = (DISPLAY_WIDTH * 0.45)
    y = (DISPLAY_HEIGHT * 0.5)
    #speed and direction of the movement of the picture
    xVelocity = 0
    yVelocity = 0
    a = 0
    dodged = 0
    #where the obstacle starts, speed and size
    obstacleStartX = random.randrange(0, DISPLAY_WIDTH)
    obstacleStartY = -600
    obstacleSpeed = 7
    obstacleWidth = 100
    obstacleHeight = 100
    
    #to keep looping
    gameExit = False

    while gameExit == False:
        #event keeps track of all buttons pressed
        for event in pygame.event.get():
            #if event brought up is similar to quitting game, quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #which direction the image should go when a key goes down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xVelocity = -10
                elif event.key == pygame.K_RIGHT:
                    xVelocity = 10
                if event.key == pygame.K_UP:
                    yVelocity = -10
                if event.key == pygame.K_DOWN:
                    yVelocity = 10
                if event.key == pygame.K_a:
                    xVelocity = -10
                elif event.key == pygame.K_d:
                    xVelocity = 10
                if event.key == pygame.K_w:
                    yVelocity = -10
                if event.key == pygame.K_s:
                    yVelocity = 10
            #stops movement when the key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    xVelocity = 0
                    yVelocity = 0
                if event.key == pygame.K_a or event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_d:
                    xVelocity = 0
                    yVelocity = 0


        #updates the x and y coordinate of the picture
        x = x +xVelocity
        y = y + yVelocity
        #order of drawing shapes is important. its like layers
        #makes background said colour
        gameDisplay.fill(WHITE)

        c3 = random.randrange(255)
        c2 = random.randrange(255)
        c1 = random.randrange(255)
        RANDOM_COLOUR = (c1, c2, c3)
            
        obstacles(obstacleStartX, obstacleStartY, obstacleWidth, obstacleHeight, RANDOM_COLOUR)
        obstacleStartY = obstacleStartY + obstacleSpeed
        car(x, y)
        obstacleDodged(dodged)
        
        if x > DISPLAY_WIDTH - CAR_WIDTH:
            crash()
        if x < 0:
            crash()
        if y > DISPLAY_HEIGHT - CAR_HEIGHT:
            crash()
        if y < 5:
            crash()
        if y < obstacleStartY+obstacleHeight:
            if (x > obstacleStartX and x < obstacleStartX+ obstacleWidth) or (x + CAR_WIDTH > obstacleStartX and x + CAR_WIDTH < obstacleStartX+ obstacleWidth):
                crash()

        #if the shape reaches the bottom go back to the top at a random location
        if obstacleStartY > DISPLAY_HEIGHT:
            obstacleStartY = 0-obstacleHeight
            obstacleStartX = random.randrange(0, DISPLAY_WIDTH)
            obstacleSpeed = random.randrange(1, 50)
            obstacleHeight = random.randrange(50, 200)
            obstacleWidth = random.randrange(50, 200)
            a += 1
            dodged += a
        
        #updates the screen to show whats happening
        pygame.display.update()

        #how rapidly to update fps (basically fps)
        clock.tick(60)

welcome()
gameLoop()
