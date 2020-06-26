""""
Hello This game is developed by Shahoriar Rahman Shazin
You can clone and download it and use it in ur project
This video game will give u a clear idea about how a classic game works
Regards Shahoriar Rahman
fB: http://facebook.com/srshazin
"""

import pygame
import random
import math
from pygame import mixer
GAME_OVER = False

# initialize pygame
pygame.init()
winHeight = 600
winWidth = 800
wn = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Jumping Ball")

# Score
score = 0
#Update Score

def updateScore():
    global score
    score += 1

# Draw Score
font = pygame.font.Font("freesansbold.ttf", 20)

scoreX = 10
scoreY = 10
# Show font function
def renderScore():
    render = font.render("Score: " + str(score), True, (255, 255, 255))
    wn.blit(render, (scoreX, scoreY))

#Game Over
game_over_text = pygame.font.Font("freesansbold.ttf", 64)

def game_over():
    render = game_over_text.render("GAME OVER" , True, (255, 255, 255))
    wn.blit(render, (200, 250))





# Making bricks

brickHeight = []
brickWidth = []
brickNum = 100
brickX = []
brickY = []
bX = random.randint(70, 150)

# Speed of the Brick
brickSpeed = 0.8
# Brick Color

color_r = []
color_g = []
color_b = []

# Draw Bricks Function
brickX = []
for x in range(brickNum):
    brickHeight.append(random.randint(-100, -50))
    brickWidth.append(20)
    bX += random.randint(400, 500)
    brickX.append(bX)
    color_r.append(random.randint(0, 255))
    color_g.append(random.randint(0, 255))
    color_b.append(random.randint(0, 255))


def drawBricks():
    for i in range(brickNum):
        # print(brickX[i])
        pygame.draw.rect(wn, (color_r[i], color_g[i], color_b[i]), [brickX[i], 600, brickWidth[i], brickHeight[i]])


# Drawing the ball
# Ball Co-ordinates
ballX = 20
ballY = 600 - 32
ballspeed = 1
ball = pygame.image.load("ball.png")


def drawBall():
    wn.blit(ball, (ballX, ballY))


# ball States

ball_state = "start"


# Collision detection

def isCollision(brickX, brickY, ballX, ballY, brickHeight):
    distance = math.sqrt(math.pow(ballX - brickX, 2) + math.pow(ballY - brickY, 2))
    if abs(ballX - brickX) <  32 and abs(600 - ballY + brickHeight) < 32:
        return True
    else:
        return False


# main Game Loop
running = True
while running:
    wn.fill((30, 40, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if GAME_OVER is False:
                    press_sound = mixer.Sound("laser.wav")
                    press_sound.play()
                    ball_state = "jump"

    # Controlling The Ball
    if ball_state == "static":
        if ballY <= 568:
            ballY += ballspeed - 0.3
    if ball_state == "jump":
        ballY -= ballspeed
    if ballY <= 400:
        ball_state = "static"
    # Collision detection

    # Draw Ball
    drawBall()
    # Draw Bricks
    drawBricks()

    # Moving the bricks

    for x in range(brickNum):
        brickX[x] -= brickSpeed

    # Rendering Score on Top
    renderScore()
    # Updating Score
    if GAME_OVER is False:
        updateScore()

    # Collision Detection
    for k in range(brickNum):
        coll = isCollision(brickX[k], 600, ballX, ballY, brickHeight[k])
        if coll:
            if GAME_OVER is False:
                collision_sound = mixer.Sound("explosion.wav")
                collision_sound.play()
            brickSpeed = 0
            ball_state = "start"
            GAME_OVER = True
            scoreX = 380
            scoreY = 340
            game_over()


    pygame.display.update()
