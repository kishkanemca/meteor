import random

import pygame

pygame.init()
win = pygame.display.set_mode((400,400))
FPS = 99999999999999999
clock = pygame.time.Clock()


class Circle:
    def __init__(self, x,y,rad,color):
        self.x = x
        self.y = y
        self.color = color
        self.rad = rad
        self.dir = 'right'

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)

    def horizontal_movement(self):
        if self.dir == 'right':
            self.x += 200
            if self.x > 100:
                self.dir = 'left'
        if self.dir == 'left':
            self.x -= 1
            if self.x < 50:
                self.dir = 'right'


list_circles = []
for i in range(100):
    list_circles.append(Circle(i * 10, i * 5, 30, random.choices(range(256), k=3)))


while True:
    win.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    for i in range(100):
        list_circles[i].draw()
        list_circles[i].horizontal_movement()
    pygame.display.update()
    clock.tick(FPS)