import pygame, sys
from pygame.locals import *
from PIL import Image
import fileinput
import os

pygame.init()

clock = pygame.time.Clock()
clock.tick(144)

width = int(1280)
height = int((width/16)*9)

pygame.display.set_caption("Platformer")

screen = pygame.display.set_mode((width, height))

r = 55
g = 125
b = 255

f = 0.5; #desaturate by 20%
L = 0.3*r + 0.6*g + 0.1*b
r1 = r + f * (L - r)
g1 = g + f * (L - g)
b1 = b + f * (L - b)

## player stuff

speed = 0.25
score = 0

player_img = pygame.image.load("player.png")
player_rect = player_img.get_rect()

moving_right = 0
moving_left = 0
moving_up = 0
moving_down = 0

player_location = [50,50]

outputFolder = os.path.dirname(__file__)

output = outputFolder + "/player.png"
outputFile = Image.new("RGB", (16,16), (int(r1),int(g1),int(b1)))
outputFile.save(output, "PNG")

timer = 0
while 1: # game loop

    screen.fill((40.4,40.4,40.4))

    for y in range(int(height/18)):
        for i in range(int(width/32)):
            if i % 2 == 0 and y % 2 == 0:
                screen.fill((67.5,67.5,67.5), ((i * 32),y * 32, 32, 32))
            elif i % 2 == 0 and y % 2 != 0:
                screen.fill((67.5,67.5,67.5), ((i * 32) + 32,y * 32, 32, 32))

    player_img = pygame.image.load("player.png")
    screen.blit(player_img, player_location)

    if moving_right == 1:
        player_location[0] += speed
    if moving_left == 1:
        player_location[0] -= speed

    if moving_up == 1:
        player_location[1] -= speed
    if moving_down == 1:
        player_location[1] += speed

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == K_d:
                moving_right = 1
            if event.key == K_LEFT or event.key == K_a:
                moving_left = 1
            if event.key == K_UP or event.key == K_w:
                moving_up = 1
            if event.key == K_DOWN or event.key == K_s: 
                moving_down = 1
        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_d:
                moving_right = 0
            if event.key == K_LEFT or event.key == K_a:
                moving_left = 0
            if event.key == K_UP or event.key == K_w:
                moving_up = 0
            if event.key == K_DOWN or event.key == K_s:
                moving_down = 0

    print(player_location)
    timer += 1

    if player_location[0] == width:
        player_location[0] = 0
    if player_location[0] == -16:
        player_location[0] = width - 1
    if player_location[1] == height:
        player_location[1] = 0
    if player_location[1] == -16:
        player_location[1] = height - 1

    pygame.display.update()