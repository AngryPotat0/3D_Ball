import pygame,sys,math
from ball import*

size = 1000,600
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("project2")
BLACK = 0,0,0
pillar = [[200,500,100,100],[600,500,100,100]]
brige = [[290,500],[290,500]]
k = 0
s = 0
alf = 180
fps = 30
x = 0
y = 0
n = 1

ball = MyBall(30,25)

cp = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            k = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            k = 0
            s = 1
            n = 0
    screen.fill((255,255,255))
    points = ball.screen(5,1/1000,1/600,500,300).tolist()
    ball.rotate(0.1)
    for p in points:
        # print(p)
        x = int(p[0]) + 500
        y = int(p[1]) + 300
        # pygame.draw.rect(screen,(0,0,0),(x,y,20,10),0)
        pygame.draw.circle(screen,(0,0,0),[x,y],int(p[2] / 10) + 2,0)
    cp.tick(fps)
    pygame.display.update()