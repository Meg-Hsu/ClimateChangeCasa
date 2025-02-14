import pygame
import pytmx

from waterPlantsGame.waterThePlants import * 
from trash_game import *
from tvMinigame.minigame import *
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


SCREEN_WIDTH = 47*32
SCREEN_HEIGHT = 26*32

# can either be 0 or 1. Only two frame animations possible
currAnimationFrame = 0

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pytmx_map = pytmx.load_pygame("floor_map.tmx")

# STAR = pygame.transform.scale(pygame.image.load(
#     os.path.join('Assets','stars.png')), (75, 75))
# star_x = 90
# star_y = 300


# add and schedule events here and handle them in the game loop
TAKEOUT_TRASH = pygame.USEREVENT + 1
pygame.time.set_timer(TAKEOUT_TRASH, 10000)

TOGGLE_ANIMATION_FRAME = pygame.USEREVENT + 2
pygame.time.set_timer(TOGGLE_ANIMATION_FRAME, 100)

STAR_EVENT = pygame.USEREVENT + 3
start_event = "plants" #change to "trash" or "tv"


class Wall(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		super(Wall, self).__init__()
		self.surf = pygame.Surface((width, height))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect()
		self.rect.x = x
		self.rect.y = y

class Star(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.surf = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets','stars.png')), (50, 50))
		self.rect = self.surf.get_rect()
		self.rect.x = x
		self.rect.y = y
	def update(self, new_x, new_y):
		self.rect.x = new_x
		self.rect.y = new_y



class Player(pygame.sprite.Sprite):
		isWalking = {
			"left": False,
			"right": False,
			"down": False,
			"up": False
		}
		isColliding = False
		speed = 4
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

		def __init__(self, x, y):
				super(Player, self).__init__()
				self.surf = self.standingImages[self.isFemme]
				self.rect = self.surf.get_rect()
				self.x = x
				self.y = y
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

player = Player(42,42)
w = Wall(100,100,100,100)
star = Star(90,300)

collidableSprites = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
allSprites.add(collidableSprites)
allSprites.add(player)
allSprites.add(star)

background = pygame.Surface((47*32, 25*32))

running = True
while running:
	if player.rect.colliderect(star.rect):
		pygame.event.post(pygame.event.Event(STAR_EVENT))
	#create star rectangle using STAR
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
		
		elif event.type == STAR_EVENT:
			if start_event == "plants":
				win = doWaterThePlantsGame()	#return value to add points
				time.sleep(.2)
				start_event = "trash"
				star_x = 600
				star_y = 100
				star.update(star_x, star_y)
				#screen.blit(sprite.surf, (star_x, star_y))
				#move the star
			elif start_event == "trash":
				win = trash_game()	#return value to add points
				time.sleep(.2)
				start_event = "tv"
				star_x = 400
				star_y = 300
				star.update(star_x, star_y)
				#move the star
			elif start_event == "tv":
				win = puzzle()
				#call tv program	return value to add points
				#once done, call end screen
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

	if player.rect.colliderect(star.rect):
		pygame.event.post(pygame.event.Event(STAR_EVENT))



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
			for x in range(0, 47):
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
						break

	screen.blit(background, (0,0))
	#screen.blit(STAR, (star_x,star_y))

	# Draw all sprites
	for sprite in allSprites:
		screen.blit(sprite.surf, sprite.rect)
	
	# render everything
	pygame.display.flip()


# Done! Time to quit.
pygame.quit()