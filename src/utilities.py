import pygame
import os
from pygame.locals import *

class Utilities():
	@staticmethod
	def load_image(file, number):
		file = os.path.join('../res/image', file)
		try:
			surface = pygame.image.load(file).convert_alpha()
		except pygame.error:
			raise SystemExit('Could not load image \'%s\' %s' % (file, pygame.get_error()))
		width = surface.get_width()
		height = surface.get_height()
		if number == 0:
			return surface
		sub_width = int(width / number)
		print(sub_width, height)
		return [surface.subsurface(
			Rect((i * sub_width, 0), (sub_width, height))
			) for i in range(number)]