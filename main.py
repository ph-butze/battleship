#!/usr/bin/python3

import pygame
import os
import sys
import time
import random

#construct pygame canvas
WIDTH,HEIGHT = 450,450
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
bg = [55,80,80]
pygame.display.set_caption("Battleship")

#load images
#player
SHIP = pygame.image.load(os.path.join("images","ship.png"))
SHIP = pygame.transform.scale(SHIP,(40,40))


class Ship:
	def __init__(self, x, y, health=100):
		self.x = x
		self.y = y
		self.width = 40
		self.height = 40
		self.health = health
		self.ship_img = None
		self.laser_img = None
		self.lasers = []
		self.speed = 5

	def draw(self,window):
		window.blit(self.ship_img, (self.x,self.y))

	def get_width(self):
		return self.ship_img.get_width()

	def get_height(self):
		return self.ship_img.get_height()

class Player(Ship):
	def __init__(self, x, y, health=100):
		super().__init__(x, y, health)
		self.ship_img = SHIP
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.max_health = health

#start the game loop
def main():
	run = True
	FPS = 60
	clock = pygame.time.Clock()
	player = Player(WIDTH/2,HEIGHT-40)
	player.ship_img = SHIP
	player.speed = 12

	def redraw():
		pygame.display.update()
		WINDOW.fill(bg)
		player.draw(WINDOW)

	while run:
		clock.tick(FPS)
		redraw()
	
		#check for events	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		#define keys input for movement and so on
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]: #escape
			run = False
		if keys[pygame.K_LEFT] and player.x - player.speed >= 0: #left
			player.x -= player.speed
		if keys[pygame.K_RIGHT] and player.x + player.speed + player.get_width() <= WIDTH: #right
			player.x += player.speed
		if keys[pygame.K_UP] and player.y - player.speed > 0: #up
			player.y -= player.speed
		if keys[pygame.K_DOWN] and player.y + player.speed + player.get_height() <= HEIGHT: #down
			player.y += player.speed

main()
