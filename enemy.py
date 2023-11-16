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
        self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/Enemy_03.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.player = player
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, self.player.x, self.player.y)
        self.speed = 3
        self.angle_rads = math.radians(self.angle)
        self.x_move = math.cos(self.angle_rads) * self.speed
        self.y_move = -math.sin(self.angle_rads) * self.speed

    def update(self):
        self.x += self.x_move
        self.y += self.y_move
        self.rect.center = (self.x, self.y)
        self.screen.blit(self.image, self.rect)