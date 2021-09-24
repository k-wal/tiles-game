from classes.tile import Tile
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([700, 500])

tiles = []
for i in range(5):
	for j in range(5):
		tiles.append(Tile(i, j, 5, 5, 500, 500))

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    for tile in tiles:
    	tile.display(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()