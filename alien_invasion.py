import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
	""" Manage game resources and actions """
	def __init__(self):
		""" Initialize game and setup resources """
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		self.ship = Ship(self)

		# Set background color
		self.bg_color = self.settings.bg_color

	def run_game(self):
		""" Start the main loop """
		while True:
			# Monitor events from keyboard and mouse
			self._check_events()
			'''
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			'''

			self.ship.update()

			self._update_screen()
			'''
			self.screen.fill(self.bg_color)
			self.ship.blitme()

			# Visualize the most recent screen
			pygame.display.flip()
			'''
			
	def _check_events(self):
		""" Helper method: respond to events """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_Q:
			sys.exit()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _update_screen(self):
		""" Helper method: update screen """
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		pygame.display.flip()



if __name__ == '__main__':
	# Create instance and run
	ai = AlienInvasion()
	ai.run_game()