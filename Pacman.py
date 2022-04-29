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

life = pygame.image.load('heart.jpg')
locations = ((750, 325), (750, 375), (725, 375), (775, 375))
# Player
playerImg = pygame.image.load('Pacman.png')
playerX = random.SystemRandom().uniform(1, 1400)
playerY = random.SystemRandom().uniform(1, 800)
playerX = 12
playerY = 4
blinkyImg = pygame.image.load('2469740-blinky.png')
inkyImg = pygame.image.load('2469741-inky.png')
pinkyImg = pygame.image.load('2469744-pinky.png')
clydeImg = pygame.image.load('2469743-orange.png')
pac_pellet_image = pygame.image.load('Pac_Pellet.png').convert_alpha()
power_pellet_image = pygame.image.load('Power_Pellet.png').convert_alpha()

wallImg = pygame.image.load('Wall.png')

tile = 32  # side length in pixels of a square tile
lives = []
number_of_lives = 3
for life in range(number_of_lives):
    lives.append(pygame.image.load('heart.png'))

score = 0

# selection_random = random.randint(1, 24)
# print(selection_random)

# blinkyX = locations[1][0]
# blinkyY = locations[1][1]
# inkyX = locations[3][0]
# inkyY = locations[3][1]
# pinkyX = locations[2][0]
# pinkyY = locations[2][1]
# clydeX = locations[0][0]
# clydeY = locations[0][1]


blinkyX = 750
blinkyY = 325

inkyX = 750
inkyY = 375

pinkyX = 725
pinkyY = 375

clydeX = 775
clydeY = 375
selection_random = 3


def randomize(sel_random):
    global clydeX, clydeY, inkyX, inkyY, blinkyX, blinkyY, pinkyX, pinkyY

    if sel_random == 1:

        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[3][0]
        inkyY = locations[3][1]
        pinkyX = locations[1][0]
        pinkyY = locations[1][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 2:
        blinkyX = locations[3][0]
        blinkyY = locations[3][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[2][0]
        pinkyY = locations[2][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 3:
        blinkyX = locations[1][0]
        blinkyY = locations[1][1]
        inkyX = locations[3][0]
        inkyY = locations[3][1]
        pinkyX = locations[2][0]
        pinkyY = locations[2][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 4:
        blinkyX = locations[3][0]
        blinkyY = locations[3][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[2][0]
        pinkyY = locations[2][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 5:
        blinkyX = locations[3][0]
        blinkyY = locations[3][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 6:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 7:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 8:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 9:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 10:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 11:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 12:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 13:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 14:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 15:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 16:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 17:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 18:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 19:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 20:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 21:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 22:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 23:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    elif sel_random == 24:
        blinkyX = locations[2][0]
        blinkyY = locations[2][1]
        inkyX = locations[1][0]
        inkyY = locations[1][1]
        pinkyX = locations[3][0]
        pinkyY = locations[3][1]
        clydeX = locations[0][0]
        clydeY = locations[0][1]
    return blinkyX, blinkyY, inkyX, inkyY, pinkyX, pinkyY, clydeX, clydeY


blinkyX, blinkyY, inkyX, inkyY, pinkyX, pinkyY, clydeX, clydeY = randomize(selection_random)

# blinkyX = 750
# blinkyY = 325
#
# inkyX = 750
# inkyY = 375
#
# pinkyX = 725
# pinkyY = 375
#
# clydeX = 775
# clydeY = 375

wallX = 10
wallY = 2

running = True


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.invincibility = False

    def update(self, x, y):
        global score
        self.rect.x += playerX_change
        self.rect.y += playerY_change
        if pygame.sprite.spritecollide(self, walls, False):
            self.rect.x -= playerX_change
            self.rect.y -= playerY_change
        if pygame.sprite.spritecollide(self, ghosts, False):
            if self.invincibility:
                # kill the ghost
                print("You ate a ghost!")
            else:
                # kill pacman
                print("You died :( ")
        if pygame.sprite.spritecollide(self, pac_pellets, True):
            score += 40
            print(score)
        if pygame.sprite.spritecollide(self, power_pellets, True):
            self.invincibility = True
            # add some sort of limiter to make invincibility run out
            # ghosts also need to turn blue while pacman is invincible


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, image, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        self.sprite = pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = self.image.get_size()
        self.smaller_image = pygame.transform.scale(self.image, (int(self.size[0] / 2), (int(self.size[1] / 2))))


class PacPellet(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        self.sprite = pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PowerPellet(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        self.sprite = pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


'''
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
'''

new_player_image = pygame.transform.scale(playerImg, (32, 32))
new_inky_image = pygame.transform.scale(inkyImg, (32, 32))
new_blinky_image = pygame.transform.scale(blinkyImg, (32, 32))
new_pinky_image = pygame.transform.scale(pinkyImg, (32, 32))
new_clyde_image = pygame.transform.scale(clydeImg, (32, 32))

smaller_image = pygame.transform.scale(wallImg, (2, 2))
pacman = Player(playerX, playerY, new_player_image)
player_sprite = pygame.sprite.Group(pacman)

inky = Ghost(inkyX, inkyY, new_inky_image, "Inky")
blinky = Ghost(blinkyX, blinkyY, new_blinky_image, "Blinky")
pinky = Ghost(pinkyX, pinkyY, new_pinky_image, "Pinky")
clyde = Ghost(clydeX, clydeY, new_clyde_image, "Clyde")
ghosts = pygame.sprite.Group([inky, blinky, pinky, clyde])

wall = Wall(wallX, wallY, smaller_image)
walls = pygame.sprite.Group([wall])

power_pellet = PowerPellet(500, 500, power_pellet_image)
power_pellets = pygame.sprite.Group(power_pellet)

all_sprites = pygame.sprite.Group([pacman, wall, inky, blinky, pinky, clyde, power_pellet])

pac_pellets = pygame.sprite.Group()
for x in range(0, 32):
    pelletX = random.randint(0, 1440)
    pelletY = random.randint(0, 739)

    pellet = PacPellet(pelletX, pelletY, pac_pellet_image)

    if (pelletX == wallX) or (pelletY == wallY):
        pelletX = random.randint(0, 1440)
        pelletY = random.randint(0, 739)
        pellet = PacPellet(pelletX, pelletY, pac_pellet_image)
    all_sprites.add(pellet)
    pac_pellets.add(pellet)


def hud():
    global wallX, wallY
    wallX = 10
    wallY = 10
    for y_wall in range(0, 740):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 1425):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    wallX = 50
    wallY = 40
    for y_wall in range(0, 325):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1

    wallX = wallX + 40
    for y_wall in range(0, 325):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 400):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 325):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    wallY = wallY - 40
    for x_wall in range(0, 550):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    wallX = wallX - 40
    for y_wall in range(0, 285):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallX = wallX - 40
    for y_wall in range(0, 245):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 185):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    wallX = wallX - 40
    for x_wall in range(0, 200):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 245):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallY = wallY + 40
    wallX = wallX + 40
    for x_wall in range(0, 345):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    wallY = wallY + 40

    for x_wall in range(0, 345):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    wallX = 345 / 2 + wallX

    for y_wall in range(0, 130):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    wallY = wallY - 210
    wallX = wallX - 345 / 2

    for x_wall in range(0, 345):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    wallY = wallY + 120
    for y_wall in range(0, 134):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 90):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 134):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 90):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallX = wallX - 345
    for x_wall in range(0, 131):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 90):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 131):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for x_wall in range(0, 90):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallY = wallY + 205
    wallX = wallX - 85
    for x_wall in range(0, 190):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 40):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallY = wallY + 80
    for x_wall in range(0, 190):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 310):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 120):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 35):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 120):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    wallX = wallX + 40
    for y_wall in range(0, 70):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    wallY = wallY - 305
    for y_wall in range(0, 70):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 30):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 40):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 85):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 30):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 115):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    wallX = wallX + 150
    wallY = wallY - 40
    for y_wall in range(0, 150):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    wallX = wallX - 35
    for y_wall in range(0, 40):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 40):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 80):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    wallY = wallY - 40
    for x_wall in range(0, 40):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    wallX = wallX - 40
    for x_wall in range(0, 75):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 75):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 75):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 35):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallY = wallY + 85
    wallX = wallX - 75
    for x_wall in range(0, 115):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 90):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 150):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    wallY = wallY - 35
    for x_wall in range(0, 115):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    wallY = wallY + 35
    wallX = wallX + 115
    for y_wall in range(0, 160):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    wallX = wallX + 40
    wallY = wallY - 35
    for y_wall in range(0, 160):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 150):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    wallX = wallX - 190
    for y_wall in range(0, 100):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 115):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    wallX = wallX + 155
    for x_wall in range(0, 115):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    wallY = wallY + 40
    for x_wall in range(0, 115):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 60):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    wallX = wallX + 115
    for y_wall in range(0, 60):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallY = wallY + 60
    wallX = wallX + 85
    for x_wall in range(0, 365):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 515):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 400):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    wallX = wallX + 40
    wallY = wallY + 40

    for x_wall in range(0, 320):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 200):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    print(wallX)
    print(wallY)
    for x_wall in range(0, 40):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 165):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 280):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 35):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallX -= 40
    wallY += 80
    for x_wall in range(0, 280):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 150):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 40):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 110):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 240):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    wallX += 40
    wallY += 40
    for x_wall in range(0, 160):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 60):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 125):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 20):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 35):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 40):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallX = 1360
    wallY = 325
    for y_wall in range(0, 195):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 325):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 95):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 50):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 50):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 235):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 150):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 40):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    wallX -= 80
    wallY += 40
    for x_wall in range(0, 200):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    wallX += 120
    for y_wall in range(0, 20):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 120):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 20):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    wallY += 60
    wallX += 45
    for x_wall in range(0, 160):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 20):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 160):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 20):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    wallY -= 60
    wallX -= 90
    for x_wall in range(0, 180):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    wallY += 40
    for x_wall in range(0, 125):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    wallY += 90
    wallX -= 30
    for x_wall in range(0, 35):
        for y_wall in range(0, 60):
            wall_image = Wall(wallX, wallY, smaller_image)
            all_sprites.add(wall_image)
            walls.add(wall_image)
            wallY = wallY + 1
        wallY -= 60
        wallX += 1
    wallX -= 850
    wallY -= 410
    for y_wall in range(0, 100):
        for x_wall in range(0, 100):
            wall_image = Wall(wallX, wallY, smaller_image)
            all_sprites.add(wall_image)
            walls.add(wall_image)
            wallX = wallX + 1
        wallX -= 100
        wallY += 1
    wallX += 145

    for x_wall in range(0, 165):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 100):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 165):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 100):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    wallX += 650
    wallY += 270
    for x_wall in range(0, 55):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 50):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 130):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 50):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    wallX += 180
    for x_wall in range(0, 90):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallX -= 900
    wallY -= 140
    for x_wall in range(0, 100):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 100):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 100):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 100):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallX += 145
    for x_wall in range(0, 165):

        for y_wall in range(0, 100):
            wall_image = Wall(wallX, wallY, smaller_image)
            all_sprites.add(wall_image)
            walls.add(wall_image)
            wallY = wallY + 1
        wallY -= 100
        wallX += 1
    wallX -= 310
    wallY += 140
    for x_wall in range(0, 310):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 270):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 75):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 200):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    for x_wall in range(0, 235):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 70):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallY += 115
    for x_wall in range(0, 190):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 235):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 190):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 235):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallX = 50
    wallY = 415
    for x_wall in range(0, 40):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 300):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 40):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 300):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallX = 880
    wallY = 600
    for x_wall in range(0, 200):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 115):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 200):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 115):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallX += 245
    for x_wall in range(0, 275):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 115):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 275):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 115):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    print(wallX)
    print(wallY)
    return wallX, wallY


def wall_and_cage():
    global wallX, wallY

    for x_wall in range(0, 1425):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1
    for y_wall in range(0, 813):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1
    for x_wall in range(0, 1425):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1
    for y_wall in range(0, 813):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1
    wallX = 720
    wallY = 368

    for x_wall in range(0, 32):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1

    wallX = 720
    wallY = 368

    for y_wall in range(0, 45):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY + 1

    for x_wall in range(0, 90):
        wall_image = Wall(wallX, wallY, smaller_image)

        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX + 1

    for y_wall in range(0, 45):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallY = wallY - 1

    for x_wall in range(0, 32):
        wall_image = Wall(wallX, wallY, smaller_image)
        all_sprites.add(wall_image)
        walls.add(wall_image)
        wallX = wallX - 1


    return wallX, wallY


wallX, wallY = wall_and_cage()
wallX, wallY = hud()
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerX_change = -2
            playerY_change = 0
            # if (playerX_change == 0) and (playerY_change == -3):
            #     playerX_change = -3
            #     playerY_change = 0
            # screen.blit(pygame.transform.rotate(new_player_image, 90), (playerX, playerY))
            # if (playerX_change == 0) and (playerY_change == 3):
            #     playerX_change = -3
            #     playerY_change = 0
            #     # pygame.transform.rotate(new_player_image, 90)
            # if (playerX_change == 3) and (playerY_change == 0):
            #     playerX_change = -3
            #     playerY_change = 0
        if keys[pygame.K_RIGHT]:
            playerX_change = 2
            playerY_change = 0
        if keys[pygame.K_UP]:
            playerX_change = 0
            playerY_change = -2
        if keys[pygame.K_DOWN]:
            playerX_change = 0
            playerY_change = 2
        if keys[pygame.K_SPACE]:
            playerX_change = 0
            playerY_change = 0
        if keys[pygame.K_TAB]:
            if (playerX_change < 0) and (playerY_change == 0):
                playerX_change -= 1
            elif(playerX_change > 0) and (playerY_change == 0):
                playerX_change += 1
            elif(playerX_change == 0) and (playerY_change < 0):
                playerY_change -= 1
            elif(playerX_change == 0) and (playerY_change > 0):
                playerY_change += 1



    '''
    playerY += playerY_change
    playerX += playerX_change
    blinky()
    inky()
    pinky()
    clyde()
    player()
    wall()
    '''
    pacman.update(playerX_change, playerY_change)
    ghosts.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    # pygame.display.update()
