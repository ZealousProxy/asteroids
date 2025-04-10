from circleshape import*
from constants import*
from shot import*


class Player(CircleShape):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		CircleShape.__init__(self, x=self.x, y = self.y, radius=PLAYER_RADIUS)
		self.rotation = 0
		self.shot_timer = 0

# in the player class
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self,screen):
		pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)

	def rotate(self,dt):
		self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

	def move(self,dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		if self.shot_timer <= 0:
			shot = Shot(self.x,self.y,5)
			shot.position = self.position
			shot.velocity = (pygame.Vector2(0,1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED
			self.shot_timer = PLAYER_SHOOT_COOLDOWN

	def update(self, dt):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			self.rotate(dt)
		if keys[pygame.K_LEFT]:
			self.rotate(dt * (-1))
		if keys[pygame.K_UP]:
			self.move(dt)
		if keys[pygame.K_DOWN]:
			self.move(dt * (-1))
		if keys[pygame.K_SPACE]:
			self.shoot()
		if self.shot_timer > 0:
			self.shot_timer = (self.shot_timer - dt)


