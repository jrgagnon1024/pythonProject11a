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
blinkyImg = pygame.image.load('2469740-blinky.png')
inkyImg = pygame.image.load('2469741-inky.png')
pinkyImg = pygame.image.load('2469744-pinky.png')
clydeImg = pygame.image.load('2469743-orange.png')
pac_pellet_image = pygame.image.load('Pac_Pellet.png').convert_alpha()
power_pellet_image = pygame.image.load('Power_Pellet.png').convert_alpha()

wallImg = pygame.image.load('Wall.png')

tile = 32  # side length in pixels of a square tile

score = 0

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

wallX = 300
wallY = 300

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

pacman = Player(playerX, playerY, new_player_image)
player_sprite = pygame.sprite.Group(pacman)

inky = Ghost(inkyX, inkyY, new_inky_image, "Inky")
blinky = Ghost(blinkyX, blinkyY, new_blinky_image, "Blinky")
pinky = Ghost(pinkyX, pinkyY, new_pinky_image, "Pinky")
clyde = Ghost(clydeX, clydeY, new_clyde_image, "Clyde")
ghosts = pygame.sprite.Group([inky, blinky, pinky, clyde])

wall = Wall(wallX, wallY, wallImg)
walls = pygame.sprite.Group([wall])

power_pellet = PowerPellet(500, 500, power_pellet_image)
power_pellets = pygame.sprite.Group(power_pellet)

all_sprites = pygame.sprite.Group([pacman, wall, inky, blinky, pinky, clyde, power_pellet])

pac_pellets = pygame.sprite.Group()
for x in range(0, 32):
    pellet = PacPellet(random.randint(0, 1450), random.randint(0, 835), pac_pellet_image)
    all_sprites.add(pellet)
    pac_pellets.add(pellet)

clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerX_change = -1
            playerY_change = 0
        if keys[pygame.K_RIGHT]:
            playerX_change = 1
            playerY_change = 0
        if keys[pygame.K_UP]:
            playerX_change = 0
            playerY_change = -1
        if keys[pygame.K_DOWN]:
            playerX_change = 0
            playerY_change = 1
        if keys[pygame.K_SPACE]:
            playerX_change = 0
            playerY_change = 0

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
