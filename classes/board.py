import sys
import os
import pygame
import random
from .tile import Tile
pygame.font.init()

class Board():
	def __init__(self, ti, tj, li, lj):
		self.ti = ti
		self.tj = tj
		self.tiles = []
		self.initialize_tiles(li, lj)
		self.score = 0
		self.max_score = 0
		self.idx_tile1 = None
		self.idx_tile2 = None
		self.n_selected = 0
		self.textbox_i = li + 50
		self.textbox_j = lj/2 - 50

	def display_score(self, screen):
		white = (255, 255, 255)
		green = (0, 160, 0)
		blue = (0, 0, 128)
		black = (0, 0, 0)
		
		to_write = 'SCORE : ' + str(self.score)
		myfont = pygame.font.SysFont('dejavuserif', 30)
		textsurface = myfont.render(to_write, False, black)
		screen.blit(textsurface, (self.textbox_i, self.textbox_j))
		
		to_write =  'MAX SCORE : ' + str(self.max_score)
		myfont = pygame.font.SysFont('dejavuserif', 25)
		textsurface = myfont.render(to_write, False, black)
		screen.blit(textsurface, (self.textbox_i-20, self.textbox_j + 50))

		if not self.idx_tile1 or self.tiles[self.idx_tile1].visible_elements > 0:
			return
		to_write =  'click on any tile'
		myfont = pygame.font.SysFont('dejavuserif', 20)
		textsurface = myfont.render(to_write, False, green)
		screen.blit(textsurface, (self.textbox_i+6, self.textbox_j + 100))
		
	def initialize_tiles(self, li, lj):
		for i in range(self.ti):
			for j in range(self.tj):
				self.tiles.append(Tile(i, j, self.ti, self.tj, li, lj))

	def check_background_match(self, i, j):
		if not self.tiles[i].is_background or not self.tiles[j].is_background:
			return False
		if self.tiles[i].background_number == self.tiles[j].background_number:
			return True
		return False

	def check_border_match(self, i, j):
		if not self.tiles[i].is_border or not self.tiles[j].is_border:
			return False
		if self.tiles[i].border_number == self.tiles[j].border_number:
			return True
		return False

	def check_flower_match(self, i, j):
		if not self.tiles[i].is_flower or not self.tiles[j].is_flower:
			return False
		if self.tiles[i].flower_number == self.tiles[j].flower_number:
			return True
		return False

	def update_max_score(self):
		if self.score > self.max_score:
			self.max_score = self.score

	def match(self):
		break_score = True
		i,j = self.idx_tile1, self.idx_tile2
		if self.check_background_match(i, j):
			break_score = False
			self.tiles[i].is_background = False
			self.tiles[j].is_background = False
			self.tiles[i].visible_elements -= 1
			self.tiles[j].visible_elements -= 1

		if self.check_border_match(i, j):
			break_score = False
			self.tiles[i].is_border = False
			self.tiles[i].visible_elements -= 1
			self.tiles[j].visible_elements -= 1
			self.tiles[j].is_border = False

		if self.check_flower_match(i, j):
			break_score = False
			self.tiles[i].is_flower = False
			self.tiles[j].is_flower = False
			self.tiles[i].visible_elements -= 1
			self.tiles[j].visible_elements -= 1

		if break_score:
			self.score = 0
		else:
			self.score += 1

		self.tiles[i].is_selected = False
		self.idx_tile1 = j
		self.idx_tile2 = None
		self.n_selected = 1
		self.update_max_score()

	def click_event(self, pos):
		for i,tile in enumerate(self.tiles):
			is_selected = tile.click_event(pos)
			if is_selected:
				if not self.idx_tile1:
					self.idx_tile1 = i
					self.n_selected = 1
				else:
					if self.tiles[self.idx_tile1].visible_elements == 0:
						self.tiles[self.idx_tile1].is_selected = False
						self.idx_tile1 = i
						self.n_selected = 1
					else:
						self.idx_tile2 = i
						self.n_selected = 2
				break
		if self.n_selected == 2:
			self.match()


	def display(self, screen):
		for tile in self.tiles:
			tile.display(screen)
		self.display_score(screen)

	