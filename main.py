# Example file showing a basic pygame "game loop"
import pygame
from player import Player
from projectile import Projectile
from enemy import Enemy
# pygame setup
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

# Load the background image
background_image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/BG_Grass.png")
#make all sprite groups
projectileGroup = pygame.sprite.Group()
playerGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
#put every sprite class in a group
Player.containers = playerGroup
Projectile.containers = projectileGroup
Enemy.containers = enemyGroup

mr_player = Player(screen, game_width/2, game_height/2)
robot = Enemy(screen, 100 , 100, mr_player)

while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        mr_player.move(1, 0)
    if keys[pygame.K_a]:
        mr_player.move(-1, 0)
    if keys[pygame.K_w]:
        mr_player.move(0, -1)
    if keys[pygame.K_s]:
        mr_player.move(0, 1)
    if pygame.mouse.get_pressed()[0]:
        mr_player.shoot()
    
    screen.blit(background_image, (0,0))
    
    mr_player.update()
    for projectile in projectileGroup:
        projectile.update()
    for enemy in enemyGroup:
        enemy.update(projectileGroup)

    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(40)
    pygame.display.set_caption("ATTACK OF THE ROBOTS fps: " + str(clock.get_fps()))
