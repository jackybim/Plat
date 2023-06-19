import pygame, sys
pygame.init()

HEIGHT, WIDTH = (1000, 500)
# The HEIGHT and WIDTH can be change !!
screen = pygame.display.set_mode((HEIGHT, WIDTH))
bg_img = pygame.image.load("PLAT/ground.png")
bg_img = pygame.transform.scale(bg_img,(1000, 500))
clock = pygame.time.Clock()
running = True

class CAR():
	def __init__(self) -> None:
		self.x = None
		self.y = None
		self.width = None
		self.height = None
		self.vel = None
		self.shape = None
		
	def moving(self):
		LEFT = False
		RIGHT = False
		Keys = pygame.key.get_pressed()
		if Keys[pygame.K_UP]:
			self.y -= self.vel
		if Keys[pygame.K_DOWN]:
			self.y += self.vel
		if Keys[pygame.K_LEFT]:
			self.x -= self.vel
		if Keys[pygame.K_RIGHT]:
			self.x += self.vel
		# gravity #
		# self.y += self.vel
		
		# collision #
		if self.x == 0:
			self.vel = 0
		else:
			self.vel = 3
		

car1 = CAR()
car1.x = 90
car1.y = 90
car1.width = 30
car1.height = 20
car1.vel = 3

def Begin():
	
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