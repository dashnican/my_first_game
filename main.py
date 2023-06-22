# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

# Load the background image
background_image=pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/BG_Grass.png")

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(background_image, (0,0))


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()