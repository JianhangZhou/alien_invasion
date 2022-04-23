import pygame

class Ship:
	""" Manage ships """
	def __init__(self, ai_game):
		""" Initialize ship and position """
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# Load ship image and get rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Position
		self.rect.midbottom = self.screen_rect.midbottom
		self.moving_right = False

	def update(self):
		if self.moving_right:
			self.rect.x += 1

	def blitme(self):
		""" Render new ship """
		self.screen.blit(self.image, self.rect)