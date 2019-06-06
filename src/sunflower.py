import pygame
from pygame.locals import *
from utilities import Utilities

class Sunflower():
	def __init__(self, screen, x, y):
		self.images = []
		self.order = 0
		pygame.sprite.Sprite.__init__(self)
		if len(self.images) == 0:
			self.images = Utilities.load_image("sunflower.png", 18)
		self.image = self.images[self.order]
		self.rect = Rect(0, 0, self.image.get_width(), self.image.get_height())
		self.screen = screen
		self.x = x
		self.y = y

	def show_flower(self):
		self.screen.blit(self.image, (self.x, self.y))

	def update(self, passed_time):
		self.order = (passed_time * 10) % 18
		self.image = self.images[int(self.order)]