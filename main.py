import pygame
import sys
from constants import*
from player import*
from asteroid import*
from asteroidfield import*
from circleshape import*
from shot import*


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")


	clock = pygame.time.Clock()
	dt = 0
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroid_group = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updateable,drawable)
	Asteroid.containers = (asteroid_group,updateable,drawable)
	AsteroidField.containers = (updateable,)
	Shot.containers = (shots,updateable,drawable)
	
	player =  Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	asteroid_field = AsteroidField()

	while 1 == 1:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
		        	return
		screen.fill((0,0,0))
		updateable.update(dt)
		for item in drawable:
			item.draw(screen)
		pygame.display.flip()

		for item in asteroid_group:
			crash = CircleShape.collisions(player,item)
			if crash == True:
				print("GAME OVER!")
				sys.exit()

		for item in asteroid_group:
			for bullet in shots:
				crash = CircleShape.collisions(bullet,item)
				if crash == True:
					item.split()
					bullet.kill()

		clock.tick(60)
		dt = (clock.tick(60))/1000

if __name__ == "__main__":
	main()
