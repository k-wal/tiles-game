import sys
import os
import pygame
import random

class Tile():
	total = 30
	background_choices = []
	border_choices = []
	flower_choices = []
	for i in range(total//2):
		background_choices.append(random.choice([1,2,3,4]))
		border_choices.append(random.choice([1,2,3,4]))
		flower_choices.append(random.choice([1,2,3,4,5]))
	background_choices = background_choices*2
	border_choices = border_choices*2
	flower_choices = flower_choices*2

	# li, lj : length across dimensions
	# ti, tj : total tiles across dimensions
	# i, j : index of tile
	def __init__(self, i, j, ti, tj, li, lj, border=5):
		self.i = i
		self.j = j
		self.ai = (li/ti) - 2*border
		self.aj = (lj/tj) - 2*border
		self.xi_beg = ((i*li)/ti) + border
		self.xi_end = self.xi_beg + self.ai
		self.xj_beg = ((j*lj)/tj) + border
		self.xj_end = self.xj_beg + self.aj
		self.color = self.random_color()
		# to change when two matches are selected
		self.is_background = True
		self.is_border = True
		self.is_flower = True
		self.visible_elements = 3

		self.background_number = random.choice(Tile.background_choices)
		Tile.background_choices.remove(self.background_number)
		self.border_number = random.choice(Tile.border_choices)
		Tile.border_choices.remove(self.border_number)
		self.flower_number = random.choice(Tile.flower_choices)
		Tile.flower_choices.remove(self.flower_number)
		self.is_selected = False
		self.rect = ''

	def random_color(self):
	    levels = range(32,256,32)
	    return tuple(random.choice(levels) for _ in range(3))
	
	def show_background(self, screen):
		if not self.is_background:
			return
		filepath = 'pictures/backgrounds2/' + str(self.background_number) + '.png'
		image = pygame.image.load(filepath)
		image = pygame.transform.scale(image, (int(self.ai), int(self.aj)))
		image.set_alpha(200)
		screen.blit(image, (self.xi_beg, self.xj_beg))
		self.rect = image.get_rect(topleft=(self.xi_beg, self.xj_beg))

	def show_border(self, screen):
		if not self.is_border:
			return
		filepath = 'pictures/borders/' + str(self.border_number) + '.png'
		image = pygame.image.load(filepath)
		image = pygame.transform.scale(image, (int(self.ai), int(self.aj)))
		screen.blit(image, (self.xi_beg, self.xj_beg))

	def show_flowers(self, screen):
		if not self.is_flower:
			return
		offset = 25
		filepath = 'pictures/flowers/' + str(self.flower_number) + '.png'
		image = pygame.image.load(filepath)
		image = pygame.transform.scale(image, (int(self.ai-2*offset), int(self.aj-2*offset)))
		screen.blit(image, (self.xi_beg+offset, self.xj_beg+offset))

	def show_selection(self, screen):
		if not self.is_selected:
			return
		if self.visible_elements > 0:
			color = (0,255,255)
		else:
			color = (0, 200, 200)
		offset = 5
		pygame.draw.rect(screen, color, pygame.Rect(self.xi_beg-offset, self.xj_beg-offset, self.ai+2*offset, self.aj+2*offset))
		pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.xi_beg, self.xj_beg, self.ai, self.aj))

	def show_solid(self, screen):
		if self.visible_elements > 0:
			return
		pygame.draw.rect(screen, self.color, pygame.Rect(self.xi_beg, self.xj_beg, self.ai, self.aj))

	def display(self, screen):
		# self.show_solid(screen)
		self.show_selection(screen)
		self.show_flowers(screen)
		self.show_background(screen)
		self.show_border(screen)
		self.show_flowers(screen)

	def click_event(self, pos):
		if self.rect.collidepoint(pos) and not self.is_selected:
			self.is_selected = True
			return True
		else:
			return False