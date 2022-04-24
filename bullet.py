import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" Manage bullets """
	def __init__(self, ai_game):
		""" Create a bullet in front of ship """
		# super(Sprite, self).__init__()
		Sprite.__init__(self)
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		self.y = float(self.rect.y)

	def update(self):
		""" Move up """
		self.y -= self.settings.bullet_speed
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)