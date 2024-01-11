"""
this program is a video game named pong that involves the movement
of a ball and paddle. This game has three modes, all of which the
common objective is to deflect the ball with the paddle and not
let the ball go past the paddle and touch your side of the screen
"""
#April 30 - May 13 2019, Stone Yang

#imported libraries
import pygame
import random
import time
import shelve

#initializing programs
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.init()

#declared constants
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 750
BLACK = (0, 0, 0)
WHITE = (255, 255, 255,)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0 )
MENU_COLOUR = (0, 211, 255)
PADDLE_COLOUR = (255, 255, 255)
BALL_COLOUR = (255, 255, 255)

#highscore system
highScore = 0
#function used to create seperate file to store and open highscore
allTimeHighScore = shelve.open('high_score.txt')   
highScore = allTimeHighScore['high_score']

#delcared global variables
clock = pygame.time.Clock()
#https://www.youtube.com/watch?v=siLkbdVxntU
paddleBounceSound = pygame.mixer.Sound('heehee.wav')
#https://www.youtube.com/watch?v=3H23zy0n2YY
wallBounceSound = pygame.mixer.Sound('waa.wav')
#https://www.youtube.com/watch?v=GUf7pPiZSNY
deathSound = pygame.mixer.Sound('uh oh.wav')
#https://www.youtube.com/watch?v=T4dZCUtq-yI
gameOverSound = pygame.mixer.Sound('freak.wav')
#https://www.youtube.com/watch?v=B3WJaC-7g2c
winnerSound = pygame.mixer.Sound('avengers.wav')
#https://www.youtube.com/watch?v=NmTJ3N00dOw
scoreSound1 = pygame.mixer.Sound('kirby.wav')
#https://www.youtube.com/watch?v=3H23zy0n2YY
scoreSound2 = pygame.mixer.Sound('take that.wav')
#https://www.youtube.com/watch?v=qTKRydIT3do
scoreSound3 = pygame.mixer.Sound('whip nae.wav')
#https://www.youtube.com/watch?v=4sVZNcxELCY
scoreSound4 = pygame.mixer.Sound('too easy.wav')
#https://www.youtube.com/watch?v=NYtVw9vdFe0
scoreSound5 = pygame.mixer.Sound('kick it.wav')
#https://www.youtube.com/watch?v=VZrxq0jKm2E
scoreSound6 = pygame.mixer.Sound('sorry.wav')
#https://www.youtube.com/watch?v=N-1ad57WZdA
scoreSound7 = pygame.mixer.Sound('sorry bucko.wav')
#https://www.youtube.com/watch?v=SOFbGHS9jZw
scoreSound8 = pygame.mixer.Sound('ahaha.wav')
#https://www.youtube.com/watch?v=3POMUa7UJCI
scoreSound9 = pygame.mixer.Sound('epic style.wav')
#https://www.youtube.com/watch?v=_Pc0RTsBRXU
backgroundMusic = pygame.mixer.music.load('harpX.mp3')

#plays music
pygame.mixer.music.play(-1)
#sets window size
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
#names program window
pygame.display.set_caption("Stone's Pong Game")

#draws recangles
def rectangle(rectangleX, rectangleY, rectangleWidth, rectangleHeight, rectangleColour):
    pygame.draw.rect(gameDisplay, rectangleColour, [rectangleX, rectangleY, rectangleWidth, rectangleHeight])

#draws circles
def circle(circleXY, circleRadius, circleColour):
    pygame.draw.circle(gameDisplay, BALL_COLOUR, circleXY, circleRadius) 

#creates invisible rectanges for text
def textObjects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

#draws settings logo
def settingsLogo(settingsIcon):
    gameDisplay.blit(settingsIcon, (88, 330))

#draws help logo
def helpLogo(helpIcon):
    gameDisplay.blit(helpIcon, (822, 340))

#keeps track of and dislays score
def scoreSystem(score):
    messageDisplay("Score: " + str(score), 55, 20, BLACK, 'yugothicregularyugothicuisemilight', 25)
    return score

#keeps track of and dislays lives
def livesSystem(lives):
    messageDisplay("Lives: " + str(lives), 945, 20, RED, 'yugothicregularyugothicuisemilight', 25)

#displays text
def messageDisplay(message, x, y, colour, font, size):
    largeText = pygame.font.SysFont(font, size)
    textSurf, textRect = textObjects(message, largeText, colour)
    textRect.center = (x, y)
    gameDisplay.blit(textSurf, textRect)

#tells the player the lost 
def gameOver():
    gameOverSound.play()
    alertDisplay ('Game Over', 2.1, BLACK)

#tells the player they died
def died():
    deathSound.play()
    alertDisplay('You Died', 4.1, BLACK)

#tells the player they won
def victory():
    #delcared variables
    gameExit = False
    endless = False

    pause = 1.0

    buttonWidth = 200
    buttonHeight = 50
    buttonX = 150
    buttonY = 550
    button1Colour = (0,205,0)
    button2Colour = (238,54,54)

    #game loop
    while gameExit == False:
        for event in pygame.event.get():
            #if player decides to quit, store highscore and exit game
            if event.type == pygame.QUIT:
                allTimeHighScore = shelve.open('high_score.txt')   
                allTimeHighScore['high_score'] = highScore
                allTimeHighScore.close()
                pygame.quit()
                quit()

            #gets the coordinates of the mouse
            mouseX, mouseY = pygame.mouse.get_pos()

            #checks if mouse is hovering of the buttons. If so, make the buttons light up
            if mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                button1Colour = (0,238,0)
            else: button1Colour = (0,205,0)    
            if mouseX > buttonX + 500 and mouseX < buttonX + 500 + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                button2Colour = (255,64,64)
            else: button2Colour = (238,54,54)

            #checks if player has clicked any buttons and takes them to appropriate location
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                endless = True
                return endless
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX + 500 and mouseX < buttonX + 500 + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                mainMenu(highScore)

        #draws and handles all visuals and text      
        rectangle(buttonX, buttonY, buttonWidth, buttonHeight, button1Colour)
        rectangle(buttonX + 500, buttonY , buttonWidth, buttonHeight, button2Colour)
        messageDisplay('Continue', 250, 575, BLACK, 'yugothicregularyugothicuisemilight', 25)
        messageDisplay('Menu', 750, 575, BLACK, 'yugothicregularyugothicuisemilight', 25)
        messageDisplay("You Won!", 500, 445, RED, 'yugothicregularyugothicuisemilight', 35)
        messageDisplay('Congratulations!', 500, 375, BLACK, 'mongolianbaiti', 80)
        pygame.display.update()
        clock.tick(60)

#tells the player they have won
def winner(text):
    colour = BLACK
    winnerSound.play()
    alertDisplay(text, 10.1, colour)

#tells the player they have scored
def scored(text, delay, randomSound):
    colour = BLACK
    scoredSoundEffect = randomSound
    scoredSoundEffect.play()
    alertDisplay(text, delay, colour)

#displays large disappearing text  
def alertDisplay(text, pause, colour):
    largeText = pygame.font.SysFont('mongolianbaiti', 80)
    textSurf, textRect = textObjects(text, largeText, colour)
    textRect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(pause)

#allows user to select either an easy mode or a hard mode
def selectMode(mode, highscore):
    #declared variables
    gameExit = False

    buttonWidth = 200
    buttonHeight = 50
    buttonX = 0
    buttonY = 700
    button1Colour = (238,238,0)

    modeButtonWidth = 200
    modeButtonHeight = 200
    modeButtonX = 220
    modeButtonY = 345
    modeButton1Colour = (0, 218, 118)
    modeButton2Colour = (235,110,180)

    #game loop
    while gameExit == False:
        for event in pygame.event.get():
            #if player decides to quit, store highscore and exit game
            if event.type == pygame.QUIT:
                allTimeHighScore = shelve.open('high_score.txt')   
                allTimeHighScore['high_score'] = highScore
                allTimeHighScore.close()
                pygame.quit()
                quit()

            #gets the position of the mouse
            mouseX, mouseY = pygame.mouse.get_pos()

            #checks if mouse is hovering of the buttons. If so, make the buttons light up
            if mouseX > modeButtonX and mouseX < modeButtonX + modeButtonWidth and mouseY > modeButtonY and mouseY < modeButtonY + modeButtonHeight:
                modeButton1Colour = (78,238,148) 
            else: modeButton1Colour = (0, 218, 118) 
            if mouseX > modeButtonX + 370 and mouseX < modeButtonX + 370 + modeButtonWidth and mouseY > modeButtonY and mouseY < modeButtonY + modeButtonHeight:
                modeButton2Colour = (255, 130, 171)
            else: modeButton2Colour = (235,110,180)
            if mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                button1Colour = (255,255,0)
            else: button1Colour = (238,238,0)   

            #checks if player has clicked any buttons and takes them to appropriate location
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > modeButtonX and mouseX < modeButtonX + modeButtonWidth and mouseY > modeButtonY and mouseY < modeButtonY + modeButtonHeight:
                time.sleep(0.05)
                difficulty = 'easy'
                #if player chooses easy game mode
                if mode == 'classic':
                    gameLoopClassic(difficulty, highScore)
                if mode == 'practice':
                    gameLoopPractice(difficulty, highScore)
                if mode == 'multiplayer':
                    gameLoopMultiplayer(difficulty, highScore)
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > modeButtonX + 370 and mouseX < modeButtonX + 370 + modeButtonWidth and mouseY > modeButtonY and mouseY < modeButtonY + modeButtonHeight:
                time.sleep(0.05)
                difficulty = 'hard'
                #if player chooses hard game mode
                if mode == 'classic':
                    gameLoopClassic(difficulty, highScore)
                if mode == 'practice':
                    gameLoopPractice(difficulty, highScore)
                if mode == 'multiplayer':
                    gameLoopMultiplayer(difficulty, highScore)
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                mainMenu(highScore)
                
        #draws and handles all visuals and text      
        gameDisplay.fill(MENU_COLOUR)
        rectangle(modeButtonX, modeButtonY, modeButtonWidth, modeButtonHeight, modeButton1Colour)
        rectangle(modeButtonX + 370, modeButtonY, modeButtonWidth, modeButtonHeight, modeButton2Colour)
        rectangle(buttonX, buttonY, buttonWidth, buttonHeight, button1Colour)
        if mode == 'classic':
            messageDisplay('Classic', 500, 200, BLACK, 'gillsans', 125)
        if mode == 'practice':
            messageDisplay('Practice', 500, 200, BLACK, 'horizon', 125)
        if mode == 'multiplayer':
            messageDisplay('Multiplayer', 500, 200, BLACK, 'goodtimes', 75)
        messageDisplay('Back', 100, 725, BLACK, 'yugothicregularyugothicuisemilight', 25)
        messageDisplay('Easy', 320, 445, BLACK, 'twcencondensedextra', 85)
        messageDisplay('Hard', 685, 445, BLACK, 'twcencondensedextra', 85)
        pygame.display.update()
        clock.tick(60)

#classic mode game loop
def gameLoopClassic(difficulty, highScore):
    #delcared variables
    gameExit = False
    endless = False
    wallDetection = False
    paddleDetection = False
    initialStart = 0
    displayedScore = 0
    score = 0
    lives = 3
    speedBoost = 0
    counter = 0
    counter2 = 10
    counter3 = 0
    hardModeAlterations = 0
    redness = 255
    easyClassicColour = (0, 250, 154)
    hardPaddleColour = (255, redness, redness)
    hardClassicColour = (152, 245, 255)
    classicColour = easyClassicColour
    
    #dimensions and details of paddle
    paddleStartX = 425
    paddleStartY = 720
    paddleWidth = 150
    paddleHeight = 15
    paddleVelocity = 0
    paddleColour = PADDLE_COLOUR
    
    #dimensions and details of ball
    ballStartX = 500
    ballStartY = 375
    ballX = 500
    ballY = 375
    ballRadius = 10
    ball_xVelocity = 0
    ball_yVelocity = 0
    ballVelocity = 5

    #game loop
    while gameExit == False:
        for event in pygame.event.get():
            #if player decides to quit, store highscore and exit game
            if event.type == pygame.QUIT:
                allTimeHighScore = shelve.open('high_score.txt')   
                allTimeHighScore['high_score'] = highScore
                allTimeHighScore.close()
                pygame.quit()
                quit()
                
            #checks if the player has pressed any buttons and if so where to move
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddleVelocity = -7
                elif event.key == pygame.K_RIGHT:
                    paddleVelocity = 7
                if event.key == pygame.K_a:
                    paddleVelocity = -7
                elif event.key == pygame.K_d:
                    paddleVelocity = 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    paddleVelocity = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    paddleVelocity = 0
                    
        #prevents paddle from going off the edge of the screen
        if paddleStartX < 0 and paddleVelocity < 0:
            paddleVelocity = 0
        if paddleStartX > DISPLAY_WIDTH-paddleWidth and paddleVelocity > 0 :
            paddleVelocity = 0
                        
        #once the paddle moves the ball moves
        if paddleVelocity != 0:
            initialStart += 5

        if initialStart == 5:
            ball_yVelocity = ballVelocity
            ball_xVelocity = ballVelocity - ballVelocity

        #randomizes random variations of movement for the ball
        while True:
            xRandomVariation = random.choice([-1, 1, 2, 8, 9, 11,])
            break

        #prevents triggering collison codes twice
        wallDetection = False
        paddleDetection = False

        #loop to check for the ball's position more precisely
        for i in range(ballVelocity):                
            ballX += (ball_xVelocity/ballVelocity)
            ballY += (ball_yVelocity/ballVelocity)

            if paddleDetection == False:    
                #checks if the ball touches the paddle and bounces off if so
                if (ballX > paddleStartX and ballX < paddleStartX + paddleWidth) and ((ballY + ballRadius/2) == paddleStartY):
                    if ball_yVelocity > 0:
                        ball_yVelocity = -ballVelocity 
                    if ball_xVelocity == 0:
                        ball_xVelocity = ballVelocity - xRandomVariation
                    #updates score
                    score += 1
                    counter += 2
                    paddleDetection = True

            if paddleDetection == False:
                #makes ball bounce in the opposite direction if in contact with a corner
                if (ballX + ballRadius > paddleStartX and ballX < paddleStartX) and ((ballY + ballRadius/2) == paddleStartY):
                    ball_yVelocity = -ballVelocity
                    ball_xVelocity = -ballVelocity
                    score += 1
                    counter += 2
                    paddleDetection = True
                if (ballX - ballRadius < paddleStartX + paddleWidth and ballX > paddleStartX + paddleWidth) and ((ballY + ballRadius/2) == paddleStartY):
                    ball_yVelocity = -ballVelocity
                    ball_xVelocity = ballVelocity
                    score += 1
                    counter += 2
                    paddleDetection = True

            if paddleDetection == False:
                #makes ball bounce off the side of the paddle when in contact
                if (ballX + ballRadius > paddleStartX and ballX < paddleStartX) and (ballY > paddleStartY and ballY < paddleStartY + paddleHeight):
                    ball_yVelocity = ballVelocity
                    ball_xVelocity = -ballVelocity
                    paddleDetection = True
                if (ballX - ballRadius < paddleStartX + paddleWidth and ballX > paddleStartX + paddleWidth) and (ballY > paddleStartY and ballY < paddleStartY + paddleHeight):
                    ball_yVelocity = ballVelocity
                    ball_xVelocity = ballVelocity
                    paddleDetection = True

            if wallDetection == False:
                #makes ball bounce of the walls when in contact
                if ((ballX + ballRadius/2 < DISPLAY_WIDTH) and (ballX - ballRadius/2 > 0) and (ballY - ballRadius/2 < 0)):
                    if ball_yVelocity < 0:
                        ball_yVelocity = -ball_yVelocity
                    wallDetection = True
                if (ballY < 750) and (ballX + ballRadius/2 > DISPLAY_WIDTH):
                    if ball_xVelocity > 1:
                        ball_xVelocity = -ball_xVelocity
                    if ball_xVelocity < -1:
                        ball_xVelocity = ball_xVelocity
                    wallDetection = True
                if (ballY < 750) and (ballX - ballRadius/2 < 0):
                    if ball_xVelocity > 0:
                        ball_xVelocity = -ball_xVelocity
                    if ball_xVelocity < 0:
                        ball_xVelocity -= ball_xVelocity*2
                    wallDetection = True
                
            #extra challengs if player chooses hard mode
            if difficulty == 'hard':
                #changes visual colours
                paddleColour = hardPaddleColour
                classicColour = hardClassicColour
                if counter == counter2:
                    #speeds up ball, changes paddle colour and shortens paddle length every 5 points
                    hardModeAlterations += 1
                    speedBoost += hardModeAlterations
                    ballVelocity += speedBoost
                    paddleWidth -= 10
                    redness -= 35
                    counter2 += 10

        #updates ball's actual position
        ballStartX = int(ballX)
        ballStartY = int(ballY)

        #plays bounce sound
        if paddleDetection == True and counter3 == 0:
            paddleBounceSound.play()
            counter3 += 1
        if wallDetection == True and counter3 == 0:
            wallBounceSound.play()
            counter3 += 1
        #prevents triggering bounce sound twice
        if counter3 > 3:
            counter3 = 0
        if counter3 <= 3 and counter3 > 0:
            counter3 += 1

        #tells player they've won when they reach a score of 25
        if displayedScore == 25 and endless == False:
            endless = victory()                    
        
        #checks if the player has died andupdates lives 
        if (ballStartX > 0 and ballStartX < DISPLAY_WIDTH and ballStartY > 750):
            if lives > 1:
                #resets the screen when the player dies
                lives -= 1
                initialStart = 0
                counter = 0
                counter2 = 10
                redness = 255
                paddleWidth = 150
                ballVelocity = 5
                hardModeAlterations = 0
                speedBoost = 0
                ballStartX = 500
                ballStartY = 375
                ballX = 500
                ballY = 375
                ball_xVelocity = 0
                ball_yVelocity = 0
                paddleStartX = 425
                paddleStartY = 720
                died()
            #checks if the player has lost the game
            else:
                #if player has beat a highscore, updates highscore
                if score > highScore:
                    highScore = score
                else:
                    highScore = highScore
                gameOver()
                mainMenu(highScore)

        
        #draws and handles all visuals and text      
        paddleStartX += paddleVelocity
        ballStartY += ball_yVelocity
        ballStartX += ball_xVelocity
        hardPaddleColour = (255, redness, redness)
        gameDisplay.fill(classicColour)
        rectangle(paddleStartX, paddleStartY, paddleWidth, paddleHeight, paddleColour)
        circle([ballStartX, ballStartY,], ballRadius, BALL_COLOUR)
        displayedScore = scoreSystem(score)
        if initialStart < 8:
            messageDisplay('Move Your Paddle to Start', 500, 415, BLACK, 'mongolianbaiti', 30)
        livesSystem(lives)
        pygame.display.update()
        clock.tick(60)

#practice mode game loop
def gameLoopPractice(difficulty, highScore):
    #declared variables
    gameExit = False
    detection = False

    delay = 0
    counter = 0
    initialStart = 0
    player1Lives = 3
    player2Lives = 3
    easyPracticeColour = (255,131,250)
    hardPaddle1Colour = GREEN
    hardPaddle2Colour = RED
    hardPracticeColour = (0,245,0)
    practiceColour = easyPracticeColour
    
    #dimensions and details of paddle
    paddle1StartX = 425
    paddle1StartY = 720
    paddle1Width = 150
    paddle1Height = 15
    paddle1Velocity = 0
    paddle1Colour = PADDLE_COLOUR

    #dimensions and details of second paddle
    paddle2StartX = 425
    paddle2StartY = 15
    paddle2Width = 150
    paddle2Height = 15
    paddle2Velocity = 0
    paddle2Colour = PADDLE_COLOUR
    
    #dimensions and details of ball
    ballStartX = 500
    ballStartY = 375
    ballX = 500
    ballY = 375
    ballRadius = 10
    ball_xVelocity = 0
    ball_yVelocity = 0
    ballVelocity = 5

    #extra challengs if player chooses hard mode
    if difficulty == 'hard':
        paddle1Colour = hardPaddle1Colour
        paddle2Colour = hardPaddle2Colour
        practiceColour = hardPracticeColour
        paddle2StartX = 435
        paddle2Width = 170
        
    #game loop 
    while gameExit == False:
        for event in pygame.event.get():
            #if player decides to quit, store highscore and exit game
            if event.type == pygame.QUIT:
                allTimeHighScore = shelve.open('high_score.txt')   
                allTimeHighScore['high_score'] = highScore
                allTimeHighScore.close()
                pygame.quit()
                quit()
                
            #checks which keys the player is pressing and moves the paddle accordingly
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle1Velocity = -7
                if event.key == pygame.K_RIGHT:
                    paddle1Velocity = 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    paddle1Velocity = 0

        #prevents the paddle from going past the edge of the screen
        if paddle1StartX < 0 and paddle1Velocity < 0:
            paddle1Velocity = 0
        if paddle1StartX > DISPLAY_WIDTH - paddle1Width and paddle1Velocity > 0:
            paddle1Velocity = 0

        #controls the not very smart AI'S movements
        if ball_xVelocity > 0:
            #since AI is always a little slower than ball, the paddle will never go off the screen
            paddle2Velocity = ball_xVelocity - 1
        elif ball_xVelocity < 0:
            paddle2Velocity = ball_xVelocity + 1
        else:
            paddle2Velocity = ball_xVelocity

        #randomizes random variations in ball movement
        while True:
            xRandomVariation = random.choice([-1, 1, 9, 11,])
            yRandomVariation = random.choice([-5, 5])
            break
                        
        #once the paddle moves the ball moves
        if paddle1Velocity != 0:
            if initialStart == 0:
                initialStart += 3

        if initialStart == 3:
            ball_yVelocity = yRandomVariation
            ball_xVelocity = ballVelocity - ballVelocity
            initialStart += 5

        #prevents triggering collison codes twice
        wallDetection = False
        paddleDetection = False

        #loop to check for the ball's position more precisely
        for i in range(ballVelocity):                
            ballX += (ball_xVelocity/ballVelocity)
            ballY += (ball_yVelocity/ballVelocity)

            if paddleDetection == False:
                #checks if the ball touches the paddles and bounces off if so
                if (ballX > paddle1StartX and ballX < paddle1StartX + paddle1Width) and ((ballY + ballRadius/2) == paddle1StartY):
                    if ball_yVelocity > 0:
                        ball_yVelocity = -ballVelocity 
                    if ball_xVelocity == 0:
                        ball_xVelocity = ballVelocity - xRandomVariation
                    paddleDetection = True
            if paddleDetection == False:
                if (ballX > paddle2StartX and ballX < paddle2StartX + paddle2Width) and ((ballY + ballRadius/2) == paddle2StartY + paddle2Height):
                    if ball_yVelocity < 0:
                        ball_yVelocity = ballVelocity 
                    if ball_xVelocity == 0:
                        ball_xVelocity = ballVelocity - xRandomVariation
                    paddleDetection = True

            if paddleDetection == False:
                #checks if the ball hits the corner or the side of the player's paddle and bounces away if so
                #corner detection
                if (ballX + ballRadius > paddle1StartX and ballX < paddle1StartX) and ((ballY + ballRadius/2) == paddle1StartY):
                    ball_yVelocity = -ballVelocity
                    ball_xVelocity = -ballVelocity
                    paddleDetection = True
                if (ballX - ballRadius < paddle1StartX + paddle1Width and ballX > paddle1StartX + paddle1Width) and ((ballY + ballRadius/2) == paddle1StartY):
                    ball_yVelocity = -ballVelocity
                    ball_xVelocity = ballVelocity
                    paddleDetection = True

            if paddleDetection == False:
                #side detection
                if (ballX + ballRadius > paddle1StartX and ballX < paddle1StartX) and ((ballY + ballRadius/2) > paddle1StartY and ballY < paddle1StartY + paddle1Height):
                    ball_yVelocity = ballVelocity
                    ball_xVelocity = -ballVelocity
                    paddleDetection = True
                if ((ballX - ballRadius < paddle1StartX + paddle1Width) and (ballX > paddle1StartX + paddle1Width)) and ((ballY + ballRadius/2) > paddle1StartY and ballY < paddle1StartY + paddle1Height):
                    ball_yVelocity = ballVelocity
                    ball_xVelocity = ballVelocity
                    paddleDetection = True

            if paddleDetection == False:
                #checks if the ball hits the corner or the side of the the CPU'S paddle and bounces away if so
                #corner detection
                if (ballX + ballRadius > paddle2StartX and ballX < paddle2StartX) and ((ballY - ballRadius/2) == paddle2StartY + paddle2Height):
                    ball_yVelocity = ballVelocity
                    ball_xVelocity = -ballVelocity
                    paddleDetection = True
                if (ballX - ballRadius < paddle2StartX + paddle2Width and ballX > paddle2StartX + paddle2Width) and ((ballY - ballRadius/2) == paddle2StartY + paddle2Height):
                    ball_yVelocity = ballVelocity
                    ball_xVelocity = ballVelocity
                    paddleDetection = True
            if paddleDetection == False:
                #side detection
                if (ballX + ballRadius > paddle2StartX and ballX < paddle2StartX) and ((ballY + ballRadius/2) > paddle2StartY and (ballY) < paddle2StartY + paddle2Height):
                    ball_yVelocity = -ballVelocity
                    ball_xVelocity = -ballVelocity
                    paddleDetection = True
                if (ballX - ballRadius < paddle2StartX + paddle2Width and ballX > paddle2StartX + paddle2Width) and ((ballY + ballRadius/2) > paddle2StartY and ballY < paddle2StartY + paddle2Height):
                    ball_yVelocity = -ballVelocity
                    ball_xVelocity = ballVelocity
                    paddleDetection = True

            if wallDetection == False:
                #checks if the ball is touching the wall and bounces away if so
                if (ballY < 750) and (ballX + ballRadius/2 > DISPLAY_WIDTH):
                    if ball_xVelocity > 1:
                        ball_xVelocity = -ball_xVelocity
                    if ball_xVelocity < -1:
                        ball_xVelocity = ball_xVelocity
                    wallDetection = True
                if (ballY < 750) and (ballX - ballRadius/2 < 0):
                    if ball_xVelocity > 0:
                        ball_xVelocity = -ball_xVelocity
                    if ball_xVelocity < 0:
                        ball_xVelocity -= ball_xVelocity*2
                    wallDetection = True

        #update the ball's actual position      
        ballStartX = int(ballX)
        ballStartY = int(ballY)

        #plays bounce sound
        if paddleDetection == True and counter == 0:
            paddleBounceSound.play()
            counter += 1
        if wallDetection == True and counter == 0:
            wallBounceSound.play()
            counter += 1
        #prevents triggering bounce sound twice
        if counter > 3:
            counter = 0
        if counter <= 3 and counter > 0:
            counter += 1

        #randomly generates a sound effect for the winner   
        while True:
            randomSound = random.choice([scoreSound1, scoreSound2, scoreSound3, scoreSound4, scoreSound5, scoreSound6, scoreSound7, scoreSound8, scoreSound9])
            if randomSound == scoreSound1:
                delay = 5.1
            elif randomSound == scoreSound2:
                delay = 0.9
            elif randomSound == scoreSound3:
                delay = 3.3
            elif randomSound == scoreSound4:
                delay = 1.3
            elif randomSound == scoreSound5:
                delay = 5.9
            elif randomSound == scoreSound6:
                delay = 2.5
            elif randomSound == scoreSound7:
                delay = 4.1
            elif randomSound == scoreSound8:
                delay = 1.4
            elif randomSound == scoreSound9:
                delay = 6.7
            break

        #checks if a player has died andupdates lives 
        if (ballStartX > 0 and ballStartX < DISPLAY_WIDTH and ballStartY > 750):
            if player1Lives > 1:
                #resets the screen once the player dies
                player1Lives -= 1
                initialStart = 0
                ballStartX = 500
                ballStartY = 375
                ballX = 500
                ballY = 375
                ball_xVelocity = 0
                ball_yVelocity = 0
                ballVelocity = 5
                paddle1StartX = 425
                paddle1StartY = 720
                paddle2StartX = 425
                paddle2StartY = 15
                initialStart = 0
                if difficulty == 'hard':
                    paddle2StartX = 435
                scored('Friday Scored', delay, randomSound)
            else:
                winner('Friday WINS')
                mainMenu(highScore)
        if (ballStartX < DISPLAY_WIDTH and ballStartX > 0 and ballStartY < -11):
            if player2Lives > 1:
                #resets the screen once the player dies
                player2Lives -= 1
                initialStart = 0 
                ballStartX = 500
                ballStartY = 375
                ballX = 500
                ballY = 375
                ball_xVelocity = 0
                ball_yVelocity = 0
                ballVelocity = 5
                paddle1StartX = 425
                paddle1StartY = 720
                paddle2StartX = 425
                paddle2StartY = 15
                initialStart = 0
                if difficulty == 'hard':
                    paddle2StartX = 435
                scored('Player 1 Scored', delay, randomSound)
            else:
                winner('Player 1 WINS')
                mainMenu(highScore)

        #handles and draws all visuals and text
        paddle1StartX += paddle1Velocity
        paddle2StartX += paddle2Velocity
        ballStartY += ball_yVelocity
        ballStartX += ball_xVelocity
        gameDisplay.fill(practiceColour)
        rectangle(paddle1StartX, paddle1StartY, paddle1Width, paddle1Height, paddle1Colour)
        rectangle(paddle2StartX, paddle2StartY, paddle2Width, paddle2Height, paddle2Colour)
        circle([ballStartX, ballStartY,], ballRadius, BALL_COLOUR)
        messageDisplay("Player 1 Lives: " + str(player1Lives), 100, 375, RED, 'yugothicregularyugothicuisemilight', 25)
        messageDisplay("Friday's Lives: " + str(player2Lives), 890, 375, BLUE, 'yugothicregularyugothicuisemilight', 25)
        if initialStart < 8:
            messageDisplay('Move Your Paddle to Start', 500, 415, BLACK, 'mongolianbaiti', 30)
        pygame.display.update()
        clock.tick(60)

#multiplayer mode game loop
def gameLoopMultiplayer(difficulty, highScore):
    #declared variables
    gameExit = False
    player1 = False
    player2 = False
    detection = False

    delay = 0
    counter = 0
    initialStart = 0
    player1Lives = 3
    player2Lives = 3
    multiplayerColour = (124, 252, 0)
    
    #dimensions and details of paddle
    paddle1StartX = 425
    paddle1StartY = 720
    paddle1Width = 150
    paddle1Height = 15
    paddle1Velocity = 0

    #dimensions and details of secondpaddle
    paddle2StartX = 425
    paddle2StartY = 15
    paddle2Width = 150
    paddle2Height = 15
    paddle2Velocity = 0
    paddleVelocity = 7

    #dimensions and details of ball
    ballStartX = 500
    ballStartY = 375
    ballX = 500
    ballY = 375
    ballRadius = 10
    ball_xVelocity = 0
    ball_yVelocity = 0
    ballVelocity = 5

    #extra challenges if players picks hard mode
    if difficulty == 'hard':
        paddleVelocity = 3
        multiplayerColour = (255,185,15)

    #game loop
    while gameExit == False:
        for event in pygame.event.get():
            #if players decides to quit, store highscore and exit game
            if event.type == pygame.QUIT:
                allTimeHighScore = shelve.open('high_score.txt')   
                allTimeHighScore['high_score'] = highScore
                allTimeHighScore.close()
                pygame.quit()
                quit()
                
            #checks which keys the players are pressing down and moves the paddle accordingly
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle1Velocity = -paddleVelocity
                if event.key == pygame.K_RIGHT:
                    paddle1Velocity = paddleVelocity
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    paddle1Velocity = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    paddle2Velocity = -paddleVelocity
                if event.key == pygame.K_d:
                    paddle2Velocity = paddleVelocity
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    paddle2Velocity = 0

        #prevents the paddle from going past the edge of the screen
        if paddle1StartX < 0 and paddle1Velocity < 0:
            paddle1Velocity = 0
        if paddle1StartX > DISPLAY_WIDTH - paddle1Width and paddle1Velocity > 0:
            paddle1Velocity = 0
        if paddle2StartX < 0 and paddle2Velocity < 0:
            paddle2Velocity = 0
        if paddle2StartX > DISPLAY_WIDTH - paddle2Width and paddle2Velocity > 0:
            paddle2Velocity = 0
                        
        #randomizes random variations in the ball's movement
        while True:
            xRandomVariation = random.choice([-1, 1, 2, 8, 9, 11,])
            yRandomVariation = random.choice([-5, 5])
            break
                        
        #once both paddles moves the ball moves
        if paddle1Velocity != 0:
            if initialStart == 0:
                initialStart += 3
            if initialStart == 5:
                initialStart += 2
        if paddle2Velocity != 0:
            if initialStart == 0:
                initialStart += 5
            if initialStart == 3:
                initialStart += 4

        if initialStart == 7:
            ball_yVelocity = yRandomVariation
            ball_xVelocity = ballVelocity - ballVelocity
            initialStart += 5
            
        #prevents triggering collison codes twice
        wallDetection = False
        paddleDetection = False

        #loop to check for the ball's position more precisely
        for i in range(ballVelocity):                
            ballX += (ball_xVelocity/ballVelocity)
            ballY += (ball_yVelocity/ballVelocity)

            if paddleDetection == False:
                #checks if the ball touches the paddles and bounces off if so
                if (ballX > paddle1StartX and ballX < paddle1StartX + paddle1Width) and ((ballY + ballRadius/2) == paddle1StartY):
                    if ball_yVelocity > 0:
                        ball_yVelocity = -ballVelocity 
                    if ball_xVelocity == 0:
                        ball_xVelocity = ballVelocity - xRandomVariation
                    paddleDetection = True
            if paddleDetection == False:
                if (ballX > paddle2StartX and ballX < paddle2StartX + paddle2Width) and ((ballY + ballRadius/2) == paddle2StartY + paddle2Height):
                    if ball_yVelocity < 0:
                        ball_yVelocity = ballVelocity 
                    if ball_xVelocity == 0:
                        ball_xVelocity = ballVelocity - xRandomVariation
                    paddleDetection = True

            if paddleDetection == False:
                #checks if the ball hits the corner or the side of the player 1's paddle and bounces away if so
                #corner detection
                if (ballX + ballRadius > paddle1StartX and ballX < paddle1StartX) and ((ballY + ballRadius/2) == paddle1StartY):
                    ball_yVelocity = -ballVelocity
                    ball_xVelocity = -ballVelocity
                    paddleDetection = True
                if (ballX - ballRadius < paddle1StartX + paddle1Width and ballX > paddle1StartX + paddle1Width) and ((ballY + ballRadius/2) == paddle1StartY):
                    ball_yVelocity = -ballVelocity
                    ball_xVelocity = ballVelocity
                    paddleDetection = True

            if paddleDetection == False:
                #side detection
                if (ballX + ballRadius > paddle1StartX and ballX < paddle1StartX) and ((ballY + ballRadius/2) > paddle1StartY and ballY < paddle1StartY + paddle1Height):
                    ball_yVelocity = ballVelocity
                    ball_xVelocity = -ballVelocity
                    paddleDetection = True
                if ((ballX - ballRadius < paddle1StartX + paddle1Width) and (ballX > paddle1StartX + paddle1Width)) and ((ballY + ballRadius/2) > paddle1StartY and ballY < paddle1StartY + paddle1Height):
                    ball_yVelocity = ballVelocity
                    ball_xVelocity = ballVelocity
                    paddleDetection = True

            if paddleDetection == False:
                #checks if the ball hits the corner or the side of the the player 2's paddle and bounces away if so
                #corner detection
                if (ballX + ballRadius > paddle2StartX and ballX < paddle2StartX) and ((ballY - ballRadius/2) == paddle2StartY + paddle2Height):
                    ball_yVelocity = ballVelocity
                    ball_xVelocity = -ballVelocity
                    paddleDetection = True
                if (ballX - ballRadius < paddle2StartX + paddle2Width and ballX > paddle2StartX + paddle2Width) and ((ballY - ballRadius/2) == paddle2StartY + paddle2Height):
                    ball_yVelocity = ballVelocity
                    ball_xVelocity = ballVelocity
                    paddleDetection = True
            if paddleDetection == False:
                #side detection
                if (ballX + ballRadius > paddle2StartX and ballX < paddle2StartX) and ((ballY + ballRadius/2) > paddle2StartY and ballY < paddle2StartY + paddle2Height):
                    ball_yVelocity = -ballVelocity
                    ball_xVelocity = -ballVelocity
                    paddleDetection = True
                if (ballX - ballRadius < paddle2StartX + paddle2Width and ballX > paddle2StartX + paddle2Width) and ((ballY + ballRadius/2) > paddle2StartY and ballY < paddle2StartY + paddle2Height):
                    ball_yVelocity = -ballVelocity
                    ball_xVelocity = ballVelocity
                    paddleDetection = True

            if wallDetection == False:
                #checks if the ball is touching the wall and bounces away if so
                if (ballY < 750) and (ballX + ballRadius/2 > DISPLAY_WIDTH):
                    if ball_xVelocity > 1:
                        ball_xVelocity = -ball_xVelocity
                    if ball_xVelocity < -1:
                        ball_xVelocity = ball_xVelocity
                    wallDetection = True
                if (ballY < 750) and (ballX - ballRadius/2 < 0):
                    if ball_xVelocity > 0:
                        ball_xVelocity = -ball_xVelocity
                    if ball_xVelocity < 0:
                        ball_xVelocity -= ball_xVelocity*2
                    wallDetection = True

        #update the ball's actual position      
        ballStartX = int(ballX)
        ballStartY = int(ballY)

        #plays bounce sound
        if paddleDetection == True and counter == 0:
            paddleBounceSound.play()
            counter += 1
        if wallDetection == True and counter == 0:
            wallBounceSound.play()
            counter += 1
        #prevents triggering bounce sound twice
        if counter > 3:
            counter = 0
        if counter <= 3 and counter > 0:
            counter += 1

        #generates random victory sound effect for the winner
        while True:
            randomSound = random.choice([scoreSound1, scoreSound2, scoreSound3, scoreSound4, scoreSound5, scoreSound6, scoreSound7, scoreSound8, scoreSound9])
            if randomSound == scoreSound1:
                delay = 5.1
            elif randomSound == scoreSound2:
                delay = 0.9
            elif randomSound == scoreSound3:
                delay = 3.3
            elif randomSound == scoreSound4:
                delay = 1.3
            elif randomSound == scoreSound5:
                delay = 5.9
            elif randomSound == scoreSound6:
                delay = 2.5
            elif randomSound == scoreSound7:
                delay = 4.1
            elif randomSound == scoreSound8:
                delay = 1.4
            elif randomSound == scoreSound9:
                delay = 6.7
            break

        #checks if a player has died andupdates lives 
        if (ballStartX > 0 and ballStartX < DISPLAY_WIDTH and ballStartY > 750):
            if player1Lives > 1:
                #resets the screen once a player dies
                player1Lives -= 1
                initialStart = 0
                ballStartX = 500
                ballStartY = 375
                ballX = 500
                ballY = 375
                ball_xVelocity = 0
                ball_yVelocity = 0
                paddle1StartX = 425
                paddle1StartY = 720
                paddle2StartX = 425
                paddle2StartY = 15
                initialStart = 0
                scored('Player 2 Scored', delay, randomSound)
            #ends the game if a player wins
            else:
                winner('Player 2 WINS')
                mainMenu(highScore)
        #checks if the player has died andupdates lives 
        if (ballStartX < DISPLAY_WIDTH and ballStartX > 0 and ballStartY < -11):
            if player2Lives > 1:
                #resets the screen once a player dies
                player2Lives -= 1
                initialStart = 0
                ballStartX = 500
                ballStartY = 375
                ballX = 500
                ballY = 375
                ball_xVelocity = 0
                ball_yVelocity = 0
                paddle1StartX = 425
                paddle1StartY = 720
                paddle2StartX = 425
                paddle2StartY = 15
                initialStart = 0
                scored('Player 1 Scored', delay, randomSound)
            #ends the game if a player wins
            else:
                winner('Player 1 WINS')
                mainMenu(highScore)

        #handles and draws all visuals and text
        paddle1StartX += paddle1Velocity
        paddle2StartX += paddle2Velocity
        ballStartY += ball_yVelocity
        ballStartX += ball_xVelocity
        gameDisplay.fill(multiplayerColour)
        rectangle(paddle1StartX, paddle1StartY, paddle1Width, paddle1Height, PADDLE_COLOUR)
        rectangle(paddle2StartX, paddle2StartY, paddle2Width, paddle2Height, PADDLE_COLOUR)
        circle([ballStartX, ballStartY,], ballRadius, BALL_COLOUR)
        messageDisplay("Player 1 Lives: " + str(player1Lives), 100, 375, RED, 'yugothicregularyugothicuisemilight', 25)
        messageDisplay("Player 2 Lives: " + str(player2Lives), 890, 375, BLUE, 'yugothicregularyugothicuisemilight', 25)
        if initialStart < 12:
            messageDisplay('Move Your Paddles to Start', 500, 415, BLACK, 'mongolianbaiti', 30)
        pygame.display.update()
        clock.tick(60)

#very nice chair loop
def chair(highScore):
    #declared variables
    gameExit = False

    buttonWidth = 50
    buttonHeight = 50
    buttonX = 400
    buttonY = 590
    buttonColour = BLACK

    #https://pngio.com/PNG/467-chair-png.html
    chairImg = pygame.image.load('chair.PNG').convert_alpha()

    #game loop
    while gameExit == False:
        for event in pygame.event.get():
            #if players decides to quit, store highscore and exit game
            if event.type == pygame.QUIT:
                allTimeHighScore = shelve.open('high_score.txt')   
                allTimeHighScore['high_score'] = highScore
                allTimeHighScore.close()
                pygame.quit()
                quit()

            #gets the coordinates of the mouse
            mouseX, mouseY = pygame.mouse.get_pos()

            #checks if the mouse is hovering over a button and lights it up if so
            if mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                buttonColour = (25, 25, 25)
            else: buttonColour = BLACK

            #checks if the mouse has clicked and takes the player to designated location
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                mainMenu(highScore)

        #handles and draws all visuals and text    
        gameDisplay.fill(BLACK)
        rectangle(buttonX, buttonY, buttonWidth, buttonHeight, buttonColour)
        messageDisplay('ok', 425, 615, WHITE, 'yugothicregularyugothicuisemilight', 25)
        messageDisplay('chair', 250, 375, WHITE, 'yugothicregularyugothicuisemilight', 150)
        gameDisplay.blit(chairImg, (525, 55))
        pygame.display.update()
        clock.tick(60)

#settings loop
def settings(highScore, helpPage):
    #declared variables
    gameExit = False

    buttonWidth = 200
    buttonHeight = 50
    buttonX = 0
    buttonY = 700
    button1Colour = (238,238,0)
    button2Colour = (238,54,54)

    #https://ya-webdesign.com/image/keys-transparent-wasd/1421582.html
    #https://james-priest.github.io/node_samples/ch13-Drag-Drop/
    settingsImg = pygame.image.load('controls.PNG').convert_alpha()

    #page loop
    while gameExit == False:
        for event in pygame.event.get():
            #if players decides to quit, store highscore and exit game
            if event.type == pygame.QUIT:
                allTimeHighScore = shelve.open('high_score.txt')   
                allTimeHighScore['high_score'] = highScore
                allTimeHighScore.close()
                pygame.quit()
                quit()

            #gets the coordinates of the mouse
            mouseX, mouseY = pygame.mouse.get_pos()

            #checks if the mouse is hovering over a button and lights it up if so
            if mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                button1Colour = (255,255,0)
            else: button1Colour = (238,238,0)     
            if mouseX > buttonX + 800 and mouseX < buttonX + 800 + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                button2Colour = (255,64,64)
            else: button2Colour = (238,54,54)

            #checks if the mouse has clicked and takes the player to designated location
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                if helpPage == True:
                    howToPlay(highScore)
                else:
                    mainMenu(highScore)
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX + 800 and mouseX < buttonX + 800 + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                if helpPage == True:
                    mainMenu(highScore)
                    
        #handles and draws all visuals and text       
        gameDisplay.fill(MENU_COLOUR)
        rectangle(buttonX, buttonY, buttonWidth, buttonHeight, button1Colour)
        if helpPage == True:
            rectangle(buttonX + 800, buttonY , buttonWidth, buttonHeight, button2Colour)
        messageDisplay('Back', 100, 725, BLACK, 'yugothicregularyugothicuisemilight', 25)
        if helpPage == True:
            messageDisplay('Menu', 900, 725, BLACK, 'yugothicregularyugothicuisemilight', 25)
        messageDisplay('Paddle Controls', 500, 120, BLACK, 'franklingothicdemicond', 55)
        gameDisplay.blit(settingsImg, (118, 215))
        pygame.display.update()
        clock.tick(60)

#help page loop
def howToPlay(highScore):
    #declared variables
    gameExit = False
    helpPage = False

    buttonWidth = 200
    buttonHeight = 50
    buttonX = 0
    buttonY = 700
    button1Colour = (238,238,0)
    button2Colour = (0,205,0)

    instructionsImg = pygame.image.load('instructions.PNG').convert_alpha()

    #page loop
    while gameExit == False:
        for event in pygame.event.get():
            #if players decides to quit, store highscore and exit game
            if event.type == pygame.QUIT:
                allTimeHighScore = shelve.open('high_score.txt')   
                allTimeHighScore['high_score'] = highScore
                allTimeHighScore.close()
                pygame.quit()
                quit()

            #gets the coordinates of the mouse
            mouseX, mouseY = pygame.mouse.get_pos()

            #if players decides to quit, store highscore and exit game
            if mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                button1Colour = (255,255,0)
            else: button1Colour = (238,238,0)     
            if mouseX > buttonX + 800 and mouseX < buttonX + 800 + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                button2Colour = (0,238,0)
            else: button2Colour = (0,205,0)

            #checks if the mouse has clicked and takes the player to designated location
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                mainMenu(highScore)
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX + 800 and mouseX < buttonX + 800 + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                helpPage = True
                settings(highScore, helpPage)

        #handles and draws all visuals and text
        gameDisplay.fill(MENU_COLOUR)
        rectangle(buttonX, buttonY, buttonWidth, buttonHeight, button1Colour)
        rectangle(buttonX + 800, buttonY , buttonWidth, buttonHeight, button2Colour)
        messageDisplay('Welcome, greenie to PONG!', 500, 90, BLACK, 'franklingothicdemicond', 55)
        messageDisplay('Back', 100, 725, BLACK, 'yugothicregularyugothicuisemilight', 25)
        messageDisplay('Settings', 900, 725, BLACK, 'yugothicregularyugothicuisemilight', 25)
        gameDisplay.blit(instructionsImg, (194, 155))
        pygame.display.update()
        clock.tick(60)

#menu page loop
def mainMenu(highScore):
    #declared variables
    gameExit = False
    helpPage = False

    buttonWidth = 250
    buttonHeight = 75
    buttonX = 375
    buttonY = 200
    button1Colour = (238,238,0)
    button2Colour = (255,69,0)
    button3Colour = (255,48,48)
    button4Colour = (154,50,205)
    button5Colour = (0,205,0)
    button6Colour = (16,78,139)

    #https://www.istockphoto.com/ca/vector/settings-vector-icon-on-transparent-background-settings-icon-gm1013490786-272897394
    settingsIcon = pygame.image.load('settings.png').convert_alpha()
    #https://www.flaticon.com/free-icon/round-help-button_61671
    helpIcon = pygame.image.load('help.png').convert_alpha()
    
    #page loop
    while gameExit == False:
        for event in pygame.event.get():
            #if players decides to quit, store highscore and exit game
            if event.type == pygame.QUIT:
                allTimeHighScore = shelve.open('high_score.txt')   
                allTimeHighScore['high_score'] = highScore
                allTimeHighScore.close()
                pygame.quit()
                quit()

            #gets the position of the mouse
            mouseX, mouseY = pygame.mouse.get_pos()

            #detects mouse cursor location and lights up button if cursor is hovering over button
            if mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                button1Colour = (255,255,0)
            else: button1Colour = (238,238,0)     
            if mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY + 130 and mouseY < buttonY + 130 + buttonHeight:
                button2Colour = (255,128,0)
            else: button2Colour = (255,69,0)
            if mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY + 260 and mouseY < buttonY + 260 + buttonHeight:
                button3Colour = (255,68,68)
            else: button3Colour = (238,44,44)
            if mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY + 390 and mouseY < buttonY + 390 + buttonHeight:
                button4Colour = (191,62,255)
            else: button4Colour = (154,50,205)
            if mouseX > buttonX - 300 and mouseX < buttonX - 300 + buttonWidth/2 and mouseY > buttonY + 135 and mouseY < buttonY + 135 + buttonHeight + 50:
                button5Colour = (0,238,0)
            else: button5Colour = (0,205,0)
            if mouseX > buttonX + 425 and mouseX < buttonX + 425 + buttonWidth/2 and mouseY > buttonY + 135 and mouseY < buttonY + 135 + buttonHeight + 50:
                button6Colour = (24,116,205)
            else: button6Colour = (16,78,139)

            #checks if the mouse has clicked and takes the player to designated location
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY and mouseY < buttonY + buttonHeight:
                time.sleep(0.05)
                mode = 'classic'
                selectMode(mode, highScore)
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY + 130 and mouseY < buttonY + 130 + buttonHeight:
                time.sleep(0.05)
                mode = 'practice'
                selectMode(mode, highScore)
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY + 260 and mouseY < buttonY + 260 + buttonHeight:
                time.sleep(0.05)
                chair(highScore)
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX and mouseX < buttonX + buttonWidth and mouseY > buttonY + 390 and mouseY < buttonY + 390 + buttonHeight:
                time.sleep(0.05)
                mode = 'multiplayer'
                selectMode(mode, highScore)
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX - 300 and mouseX < buttonX - 300 + buttonWidth/2 and mouseY > buttonY + 135 and mouseY < buttonY + 135 + buttonHeight + 50:
                time.sleep(0.05)
                settings(highScore, helpPage)
            if event.type == pygame.MOUSEBUTTONDOWN and mouseX > buttonX + 425 and mouseX < buttonX + 425 + buttonWidth/2 and mouseY > buttonY + 135 and mouseY < buttonY + 135 + buttonHeight + 50:
                time.sleep(0.05)
                howToPlay(highScore)

        #handles and draws all visuals and text
        gameDisplay.fill(MENU_COLOUR)
        rectangle(buttonX, buttonY, buttonWidth, buttonHeight, button1Colour)
        rectangle(buttonX, buttonY + 130, buttonWidth, buttonHeight, button2Colour)
        rectangle(buttonX, buttonY + 260, buttonWidth, buttonHeight, button3Colour)
        rectangle(buttonX, buttonY + 390, buttonWidth, buttonHeight, button4Colour)
        rectangle(buttonX - 300, buttonY + 135, buttonWidth/2, buttonHeight + 50, button5Colour)
        rectangle(buttonX + 425, buttonY + 135, buttonWidth/2 , buttonHeight + 50, button6Colour)
        messageDisplay('Pong', 500, 100, BLACK, 'yugothicregularyugothicuisemilight', 150)
        messageDisplay('Highscore: ' + str(highScore), 500, 175, BLACK, 'yugothicregularyugothicuisemilight', 25)
        messageDisplay('Classic', 500, 237, BLACK, 'yugothicregularyugothicuisemilight', 35)
        messageDisplay('Practice', 500, 367, BLACK, 'yugothicregularyugothicuisemilight', 35)
        messageDisplay('ok', 500, 497, BLACK, 'yugothicregularyugothicuisemilight', 35)
        messageDisplay('Multiplayer', 500, 627, BLACK, 'yugothicregularyugothicuisemilight', 35)
        messageDisplay('Help', 862, 435, BLACK, 'yugothicregularyugothicuisemilight', 25)
        messageDisplay('Settings', 135, 435, BLACK, 'yugothicregularyugothicuisemilight', 25)
        settingsLogo(settingsIcon)
        helpLogo(helpIcon)
        pygame.display.update()
        clock.tick(60)

#start of progame. Calls menu page
mainMenu(highScore)
