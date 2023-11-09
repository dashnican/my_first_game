import pygame
import toolbox
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, speed, screen, x, y, z):
        #make projectile a sprite
        pygame.sprite.Sprite.__init__(self,self.containers)
        #set up projectile variables
        self.x = x
        self.y = y
        self.image = pygame.image.load
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.angle = z
        self.speed = 5
        self.angle_rads = math.radians(self.angle)
        self.x_move = math.cos(self.angle_rads) * self.speed
        self.y_move = -math.sin(self.angle_rads) * self.speed
        self.image, self.rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)

    def update(self):
        self.x = self.x_move
        self.y = self.y_move
        self.rect.center = (self.x, self.y)

        self.screen.blit(image_to_draw, image_rect)


