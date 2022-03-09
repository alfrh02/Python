import sys, pygame

pygame.init()
size = width, height = 1280,720
speed = [1,1]

r = 0
g = 0
b = 0

ballamount = 0

screen = pygame.display.set_mode(size)
ball = pygame.image.load("tutorial.png")
ball_red = ball
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect. right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed [1]

    r += 1
    g += 1
    b += 1

    background = r,g,b

    if r == 255 OR r == 254:
        r = 0
        g = 0
        b = 0

    screen.fill(background)
    screen.blit(ball, ballrect)
    pygame.display.flip()