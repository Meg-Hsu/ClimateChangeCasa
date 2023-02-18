import pygame

from pygame.locals import (
		# RLEACCEL is an internal var in pygame used
		# to make sprite drawing faster somehow ¯\_(ツ)_/¯
		RLEACCEL,
		K_UP,
		K_DOWN,
		K_LEFT,
		K_RIGHT,
		K_ESCAPE,
		KEYDOWN,
		QUIT,
)

pygame.init()


# add and schedule events here and handle them in the game loop
TAKEOUT_TRASH = pygame.USEREVENT + 1
pygame.time.set_timer(TAKEOUT_TRASH, 10000)


# arbitrary values change at your own discretion
# SCREEN_WIDTH \ SCREENHEIGHT should equal the golden ratio (~ 1.6)
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


class Player(pygame.sprite.Sprite):
		def __init__(self):
				super(Player, self).__init__()
				# TODO: change two lines down here to this dead code with "our.png" replaced
				# to draw as sprite
				# self.surf = pygame.image.load("our.png").convert()
				# self.surf.set_colorkey((255, 255, 255), RLEACCEL)
				self.surf = pygame.Surface((75, 25))
				self.surf.fill((255, 255, 255))
				self.rect = self.surf.get_rect()

		# Move the sprite based on user keypresses
		def update(self, pressed_keys):
				if pressed_keys[K_UP]:
						self.rect.move_ip(0, -5)
				if pressed_keys[K_DOWN]:
						self.rect.move_ip(0, 5)
				if pressed_keys[K_LEFT]:
						self.rect.move_ip(-5, 0)
				if pressed_keys[K_RIGHT]:
						self.rect.move_ip(5, 0)

				# Keep player on the screen
				if self.rect.left < 0:
						self.rect.left = 0
				if self.rect.right > SCREEN_WIDTH:
						self.rect.right = SCREEN_WIDTH
				if self.rect.top <= 0:
					self.rect.top = 0
				if self.rect.bottom >= SCREEN_HEIGHT:
						self.rect.bottom = SCREEN_HEIGHT


player = Player()

# To make a sprite collidable do:
# collidableSprites.add(theObjectYouWantToMakeCollidable)

collidableSprites = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
allSprites.add(player)

running = True
while running:
	for event in pygame.event.get():
		# Did the user hit a key?s
		if event.type == KEYDOWN:
			# Was it the Escape key? If so, stop the loop.
			if event.key == K_ESCAPE:
					running = False
		elif event.type == QUIT:
				running = False

		elif event.type == TAKEOUT_TRASH:
			# TODO make this actually do something
			print("take out the darn trash kiddo")
		

	#read current key presses and update player accordingly
	pressed_keys = pygame.key.get_pressed()
	player.update(pressed_keys)
	collidableSprites.update()

	# TODO make this draw the background
	screen.fill((0,0,0))

	# Draw all sprites
	for entity in allSprites:
			screen.blit(entity.surf, entity.rect)

	# Do collision detection 
	#if pygame.sprite.spritecollideany(player, collidableSprites):
		#TODO handle collisions

	
	#render everything
	pygame.display.flip()


# Done! Time to quit.
pygame.quit()