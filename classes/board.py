import sys
import os
import pygame
import random
from .tile import Tile

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

	def match(self):
		break_score = True
		i,j = self.idx_tile1, self.idx_tile2
		if self.check_background_match(i, j):
			break_score = False
			self.tiles[i].is_background = False
			self.tiles[j].is_background = False

		if self.check_border_match(i, j):
			break_score = False
			self.tiles[i].is_border = False
			self.tiles[j].is_border = False

		if self.check_flower_match(i, j):
			break_score = False
			self.tiles[i].is_flower = False
			self.tiles[j].is_flower = False

		if break_score:
			self.score = 0
		else:
			self.score += 1

		print(self.score)
		self.tiles[i].is_selected = False
		self.idx_tile1 = j
		self.idx_tile2 = None
		self.n_selected = 1

	def click_event(self, pos):
		for i,tile in enumerate(self.tiles):
			is_selected = tile.click_event(pos)
			if is_selected:
				self.n_selected += 1
				if not self.idx_tile1:
					self.idx_tile1 = i
				else:
					self.idx_tile2 = i
				break
		if self.n_selected == 2:
			self.match()


	def display_tiles(self, screen):
		for tile in self.tiles:
			tile.display(screen)

	