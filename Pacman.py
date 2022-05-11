import pygame
import random
import math


pygame.init()
playerX_change = 0
playerY_change = 0
screen = pygame.display.set_mode((1450, 835))
pygame.display.set_caption("Pacman")
icon = pygame.image.load('smiley (1).png')
pygame.display.set_icon(icon)


life = pygame.image.load('')
locations = ((750, 325), (750, 375), (725, 375), (775, 375))
# Player
playerImg = pygame.image.load('Pacman.png')
playerX = random.SystemRandom().uniform(1, 1400)
playerY = random.SystemRandom().uniform(1, 800)
blinkyImg = pygame.image.load('2469740-blinky.png')
inkyImg = pygame.image.load('2469741-inky.png')
pinkyImg = pygame.image.load('2469744-pinky.png')
clydeImg = pygame.image.load('2469743-orange.png')

# selection_random = random.randint(1, 24)
# print(selection_random)
# selection_random = 2
# if selection_random == 1:
#     blinkyX = locations[1][0]
#     blinkyY = locations[1][1]
#     inkyX = locations[3][0]
#     inkyY = locations[3][1]
#     pinkyX = locations[2][0]
#     pinkyY = locations[2][1]
#     clydeX = locations[0][0]
#     clydeY = locations[0][1]
# elif selection_random == 2:
#     blinkyX = locations[2][0]
#     blinkyY = locations[2][1]
#     inkyX = locations[1][0]
#     inkyY = locations[1][1]
#     pinkyX = locations[3][0]
#     pinkyY = locations[3][1]
#     clydeX = locations[0][0]
#     clydeY = locations[0][1]
blinkyX = 750
blinkyY = 325
inkyX = 750
inkyY = 375

pinkyX = 725
pinkyY = 375

clydeX = 775
clydeY = 375

running = True


def player():
    newPlayerImg = pygame.transform.scale(playerImg, (32, 32))

    screen.blit(newPlayerImg, (playerX, playerY))


def blinky():
    newBlinkyImg = pygame.transform.scale(blinkyImg, (32, 32))
    screen.blit(newBlinkyImg, (blinkyX, blinkyY))


def inky():
    newInkyImg = pygame.transform.scale(inkyImg, (32, 32))
    screen.blit(newInkyImg, (inkyX, inkyY))


def pinky():
    newPinkyImg = pygame.transform.scale(pinkyImg, (32, 32))
    screen.blit(newPinkyImg, (pinkyX, pinkyY))


def clyde():
    newClydeImg = pygame.transform.scale(clydeImg, (32, 32))
    screen.blit(newClydeImg, (clydeX, clydeY))


def collision_detection(ghostx, ghosty, playerx, playery):

    distance = math.sqrt(((ghostx - playerx) ** 2) + ((ghosty - playery) ** 2))
    if distance < 1:
        print("hello")

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerX_change = -0.1
            playerY_change = 0.0
        if keys[pygame.K_RIGHT]:
            playerX_change = 0.1
            playerY_change = 0.0
        if keys[pygame.K_UP]:
            playerY_change = -0.1
            playerX_change = 0.0
        if keys[pygame.K_DOWN]:
            playerY_change = 0.1
            playerX_change = 0.0
        if keys[pygame.K_SPACE]:
            playerX_change = 0.0
            playerY_change = 0.0

        # if event.type == pygame.KEYDOWN:
        #     playerY_change = -0.1
        #     if event.key == pygame.K_LEFT:
        #         playerX_change = -0.1
        #     if event.key == pygame.K_RIGHT:
        #         playerY_change = 0.1
        #
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         playerX_change = -0.1
        #     if event.key == pygame.K_RIGHT:
        #         playerX_change = 0.1
    playerY += playerY_change
    playerX += playerX_change
    blinky()
    inky()
    pinky()
    clyde()
    player()
    pygame.display.update()
