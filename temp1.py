import pygame
import random

class player:
	def __init__(self):
		self.speed = 5
		self.move_right = False
		self.move_left = False
		self.size = 2
		self.pos_x = display_width//2
		self.pos_y = display_heigth - self.size
		self.score = 0

	def walk_right(self):
		self.move_right = True
		self.move_left = False

	def walk_left(self):
		self.move_left = True
		self.move_right = False

	def stop(self):
		self.move_left = False
		self.move_right = False

	def update(self):
		if self.move_right == True:
			self.pos_x += self.speed
		elif self.move_left == True:
			self.pos_x -= self.speed
		pygame.draw.circle(gameDisplay,white,[self.pos_x,self.pos_y], self.size)


class falling_object:
	def __init__(self, object_type):
		self.object_type = object_type
		self.speed = random.randint(3,10)
		self.size = random.randint(display_width//100, display_width//10)
		self.pos_x = random.randint(self.size, display_width-self.size)
		self.pos_y = 0
		
	def update(self):
		self.pos_y += self.speed
		if self.object_type == 'snowball':
			pygame.draw.circle(gameDisplay,white,[self.pos_x,self.pos_y], self.size)
		else:
			pygame.draw.circle(gameDisplay,gray,[self.pos_x,self.pos_y], self.size)
			
		# if abs(self.pos_x - player.pos_x) < action_radius and abs(self.pos_y - player.pos_y) < action_radius:
		# 	##УДАЛЕНИЕ ОБЪЕКТА##

###################Инициализация###################
pygame.init()
pygame.font.init()

textfont = pygame.font.SysFont('Comic Sans MS', 30)
display_width = int(1280/1.1)
display_heigth = int(720/1.1)
gameDisplay = pygame.display.set_mode((display_width, display_heigth))

pygame.display.set_caption('snowball game')
clock = pygame.time.Clock()

white = (255,255,255)
gray = (150, 150, 150)
black = (0,0,0)
action_radius = 50
FPS = 60

player1 = player()
falling_objects_list = []
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		############################
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				player1.walk_left()				
			elif event.key == pygame.K_d:
				player1.walk_right()						
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				player1.stop()
		############################
	if len(falling_objects_list) < 10:
		falling_objects_list.append(falling_object('snowball'))
	gameDisplay.fill(black)
	i=0
	while i < len(falling_objects_list):
		falling_objects_list[i].update()
		if falling_objects_list[i].pos_y > display_heigth:
			del falling_objects_list[i]
		else:
			i+=1
	player1.update()
	pygame.display.update()
	clock.tick(FPS)