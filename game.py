from classes.board import Board
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([700, 600])


board = Board(5, 6, 500, 600)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
        	pos = pygame.mouse.get_pos()
        	board.click_event(pos)

        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    board.display_tiles(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()