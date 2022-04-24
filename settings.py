class Settings:
	""" Save all settings """
	def __init__(self):
		""" Initialize game """
		# Screen
		self.screen_width = 1200
		self.screen_height = 800
		# Background color grey
		self.bg_color = (230, 230, 230)
		# Background color blue
		# self.bg_color = (0, 0, 255)

		# Ship setting
		self.ship_speed = 1.5

		# Bullet setting
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3