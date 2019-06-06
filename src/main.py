from sunflower import Sunflower
import pygame
from pygame.locals import *
import time

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

sunflower = Sunflower(screen, 0, 100)

while True:
	screen.fill((0,0,0))
	sunflower.update(time.time())
	sunflower.show_flower()
	pygame.display.update()