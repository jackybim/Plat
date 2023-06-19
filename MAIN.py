import pygame, sys
pygame.init()

HEIGHT, WIDTH = (1000, 500)
# The HEIGHT and WIDTH can be change !!
screen = pygame.display.set_mode((HEIGHT, WIDTH))
bg_img = pygame.image.load("PLAT/ground.png")
bg_img = pygame.transform.scale(bg_img,(1000, 500))
clock = pygame.time.Clock()
running = True
floor = pygame.Rect(0, 451, 1000, 73)

class CAR():
	def __init__(self) -> None:
		self.x = None
		self.y = None
		self.width = None
		self.height = None
		self.vel = None
		self.shape = None
		self.LEFT = None
		self.RIGHT = None
		self.gravity = None
		
	def moving(self):

		Keys = pygame.key.get_pressed()

		if Keys[pygame.K_UP]:
			self.y -= self.vel

		if self.LEFT == True:
			if Keys[pygame.K_LEFT]:
				self.x -= self.vel
		if self.RIGHT == True:
			if Keys[pygame.K_RIGHT]:
				self.x += self.vel

		if self.x == 0:
			self.LEFT = False
		if  self.x > 0:
			self.LEFT = True
		
		if self.x == 970:
			self.RIGHT = False
		if self.x < 970:
			self.RIGHT = True

		if self.shape.colliderect(floor):
			self.gravity = False
		
		if self.gravity == True:
			if self.y < 432:
				self.gravity = True
				self.y += self.vel
				
			

car1 = CAR()
car1.x = 90
car1.y = 90
car1.width = 30
car1.height = 20
car1.vel = 3
car1.LEFT = True
car1.RIGHT = True
car1.gravity = True

def Begin():
	pygame.draw.rect(screen, (0,0,0), (floor))
	car1.shape = pygame.Rect(car1.x, car1.y, car1.width, car1.height)
	car1.moving()
	screen.blit(bg_img, (0, 0))
	
	pygame.draw.rect(screen, (255,255,255), car1.shape)
	print(car1.x, car1.y)
	

while running:
	Begin()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			sys.exit()

	clock.tick(60)
	pygame.display.flip()
	pygame.display.update()