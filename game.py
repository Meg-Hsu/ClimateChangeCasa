import pygame
import pytmx

from waterPlantsGame.waterThePlants import * 
from pygame.locals import (
		# RLEACCEL is an internal var in pygame used
		# to make sprite drawing faster somehow ¯\_(ツ)_/¯
		RLEACCEL,
		K_q,
		K_UP,
		K_DOWN,
		K_LEFT,
		K_RIGHT,
		K_ESCAPE,
		KEYDOWN,
		KEYUP,
		QUIT,
)

pygame.init()


# arbitrary values change at discretion
# SCREEN_WIDTH \ SCREENHEIGHT should equal the golden ratio (~ 1.6)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# can either be 0 or 1. Only two frame animations possible
currAnimationFrame = 0

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pytmx_map = pytmx.load_pygame("floor_map.tmx")


# add and schedule events here and handle them in the game loop
TAKEOUT_TRASH = pygame.USEREVENT + 1
pygame.time.set_timer(TAKEOUT_TRASH, 10000)

TOGGLE_ANIMATION_FRAME = pygame.USEREVENT + 2
pygame.time.set_timer(TOGGLE_ANIMATION_FRAME, 100)


class Wall(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		super(Wall, self).__init__()
		self.surf = pygame.Surface((width, height))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect()
		self.rect.x = x
		self.rect.y = y


class Player(pygame.sprite.Sprite):
		isWalking = {
			"left": False,
			"right": False,
			"down": False,
			"up": False
		}
		isColliding = False
		speed = 2
		# can either be 1 or 2
		isFemme = 1
		standingImages = {
			1: pygame.image.load("Assets/char_1.png").convert_alpha(),
			2: pygame.image.load("Assets/char_2.png").convert_alpha()
		}
		
		leftWalkCycleImgs = [pygame.image.load("Assets/char_1_standing.png").convert_alpha(), 
			pygame.image.load("Assets/char_1_walking.png").convert_alpha()]
		rightWalkCycleImgs = [pygame.transform.flip(pygame.image.load("Assets/char_1_standing.png").convert_alpha(), True, False), 
			pygame.transform.flip(pygame.image.load("Assets/char_1_walking.png").convert_alpha(), True, False)]
		downWalkCycleImgs = [pygame.image.load("Assets/char_1_standing.png").convert_alpha(), 
			pygame.image.load("Assets/char_1_walking.png" ).convert_alpha()]
		upWalkCycleImgs = [pygame.image.load("Assets/char_1_standing.png").convert_alpha(), 
			pygame.image.load("Assets/char_1_walking.png" ).convert_alpha()]

		def __init__(self):
				super(Player, self).__init__()
				self.surf = self.standingImages[self.isFemme]
				self.rect = self.surf.get_rect()

		# Move the sprite based on user keypresses
		def update(self, pressed_keys):	
			velocityX = 0
			velocityY = 0
			if pressed_keys[K_UP]:
					velocityY = -self.speed
			if pressed_keys[K_DOWN]:
					velocityY = self.speed
			if pressed_keys[K_LEFT]:
					velocityX = -self.speed
			if (pressed_keys[K_RIGHT]):
					velocityX = self.speed

			self.rect.move_ip(velocityX, velocityY)

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

collidableSprites = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
allSprites.add(collidableSprites)
allSprites.add(player)

background = pygame.Surface((25*32, 25*32))

running = True
while running:
	#waterThePlants.doWaterThePlantsGame()
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
					running = False
			elif event.key == K_UP:
				player.isWalking["up"] = True
			elif event.key == K_DOWN:
				player.isWalking["down"] = True 
			elif event.key == K_LEFT:
				player.isWalking["left"] = True
			elif event.key == K_RIGHT:
				player.isWalking["right"] = True
			elif event.key ==  K_q:
				doWaterThePlantsGame()

		elif event.type == KEYUP:	
			if event.key == K_UP:
				player.isWalking["up"] = False
				player.surf = player.standingImages[player.isFemme]
			elif event.key == K_DOWN:
				player.isWalking["down"] = False 
				player.surf = player.standingImages[player.isFemme]
			elif event.key == K_LEFT:
				player.isWalking["left"] = False
				player.surf = player.standingImages[player.isFemme]
			elif event.key == K_RIGHT:
				player.isWalking["right"] = False
				player.surf =player.standingImages[player.isFemme]

		elif event.type == QUIT:
				running = False

		elif event.type == TAKEOUT_TRASH:
			# TODO make this actually do something
			print("take out the darn trash kiddo")

		elif event.type == TOGGLE_ANIMATION_FRAME:
			currAnimationFrame = 1 - currAnimationFrame
			if(player.isWalking["left"]):
				player.surf = player.leftWalkCycleImgs[currAnimationFrame]
			if(player.isWalking["right"]):
				player.surf = player.rightWalkCycleImgs[currAnimationFrame]
			if(player.isWalking["down"]):
				player.surf = player.downWalkCycleImgs[currAnimationFrame]
			if(player.isWalking["up"]):
				player.surf = player.upWalkCycleImgs[currAnimationFrame]
	
	
	oldPlayerX, oldPlayerY = player.rect.topleft


	layer_index = 0
	for layer in pytmx_map.visible_layers:
		if isinstance(layer, pytmx.TiledTileLayer):
			for x in range(0, 25):
				for y in range(0, 25):
					image = pytmx_map.get_tile_image(x, y, layer_index)
					if image != None:
						background.blit(image, (32*x, 32*y))
		layer_index += 1


	#read current key presses and update player accordingly
	pressed_keys = pygame.key.get_pressed()
	player.update(pressed_keys)
	collidableSprites.update()


	# Do collision detection ¡IMPORTANT! this must be before updating the player 
	# if pygame.sprite.spritecollideany(player, collidableSprites):		
	# 	player.rect.topleft = oldPlayerX, oldPlayerY
	for sprites in collidableSprites:
		if player.rect.colliderect(sprites):
			player.rect.topleft = oldPlayerX, oldPlayerY
	

	for event in pygame.event.get():
		pass

		
	layer_index = 0
	for layer in pytmx_map.visible_layers:
		if isinstance(layer, pytmx.TiledTileLayer):
			for x in range(0, 25):
				for y in range(0, 25):
					image = pytmx_map.get_tile_image(x, y, layer_index)
					if image != None:
						background.blit(image, (32*x, 32*y))

		layer_index += 1
		if isinstance(layer, pytmx.TiledObjectGroup):
			if layer.name == "thing_objects":
				for obj in layer:
					if pygame.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(player.rect) == True:
						player.rect.topleft = oldPlayerX, oldPlayerY
						print("YOU HIT THE RED BLOCK!!")
						break

	screen.blit(background, (0,0))

	# Draw all sprites
	for sprite in allSprites:
			screen.blit(sprite.surf, sprite.rect)
	
	# render everything
	pygame.display.flip()


# Done! Time to quit.
pygame.quit()
