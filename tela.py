import pygame

pygame.init()

monitor = pygame.display.Info()
width = monitor.current_w
height = monitor.current_h 
size = (width, height)
tela = pygame.display.set_mode(size)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	pygame.display.flip()
