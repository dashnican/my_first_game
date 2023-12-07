import pygame
import math
import toolbox

class Enemy(pygame.sprite.Sprite):
#add an enemy 
    def __init__(self, screen, x, y, player):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/Enemy_02.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.player = player
        self.angle = 0
        self.speed = 3.5
        self.healthpoints = 100
        self.hurt = False
        self.imagehurt = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/Enemy_02hurt.png")

    def update(self, projectiles):
        #getting the angle from the enemy's position to the player's location
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, self.player.x, self.player.y)
        self.angle_rads = math.radians(self.angle)
        #getting the enemy to move in that angle
        self.x_move = math.cos(self.angle_rads) * self.speed
        self.y_move = -math.sin(self.angle_rads) * self.speed
        self.x += self.x_move
        self.y += self.y_move
        self.rect.center = (self.x, self.y)
        
        for projectile in projectiles:
            if self.rect.colliderect(projectile.rect):
                self.getHit(projectile.damage)
                projectile.explode()
        if self.healthpoints <=50:
            imagetodraw = self.imagehurt

        else:
            imagetodraw = self.image
                
        self.screen.blit(imagetodraw, self.rect)

    def getHit(self, damage):
        self.x -= self.x_move
        self.y -= self.y_move
        self.healthpoints -= damage
        if self.healthpoints <= 0: 
            self.kill()

        