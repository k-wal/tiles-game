import sys
import os
import pygame
import random

class Tile():
	# li, lj : length across dimensions
	# ti, tj : total tiles across dimensions
	# i, j : index of tile
	def __init__(self, i, j, ti, tj, li, lj, border=2):
		self.i = i
		self.j = j
		self.ai = (li/ti) - 2*border
		self.aj = (lj/tj) - 2*border
		self.xi_beg = ((i*li)/ti) + border
		self.xi_end = self.xi_beg + self.ai
		self.xj_beg = ((j*lj)/tj) + border
		self.xj_end = self.xj_beg + self.aj
		self.color = self.random_color()
		self.background_number = random.choice([1,4,6,7,8])
		self.border_number = random.choice([1,2,3,4,5])
		self.flower_number = random.choice([1,2,3,4,5])

	def random_color(self):
	    levels = range(32,256,32)
	    return tuple(random.choice(levels) for _ in range(3))
	
	def show_background(self, screen):
		filepath = 'pictures/background/' + str(self.background_number) + '.jpg'
		image = pygame.image.load(filepath)
		image = pygame.transform.scale(image, (int(self.ai), int(self.aj)))
		image.set_alpha(255)
		screen.blit(image, (self.xi_beg, self.xj_beg))

	def show_border(self, screen):
		filepath = 'pictures/borders/' + str(self.border_number) + '.png'
		image = pygame.image.load(filepath)
		image = pygame.transform.scale(image, (int(self.ai), int(self.aj)))
		screen.blit(image, (self.xi_beg, self.xj_beg))

	def show_flowers(self, screen):
		offset = 25
		filepath = 'pictures/flowers/' + str(self.flower_number) + '.png'
		image = pygame.image.load(filepath)
		image = pygame.transform.scale(image, (int(self.ai-2*offset), int(self.aj-2*offset)))
		screen.blit(image, (self.xi_beg+offset, self.xj_beg+offset))

	def display(self, screen):
		self.show_background(screen)
		self.show_border(screen)
		self.show_flowers(screen)
		# pygame.draw.rect(screen, self.color, pygame.Rect(self.xi_beg, self.xj_beg, self.ai, self.aj))
