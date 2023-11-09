import pygame
import toolbox
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, angle):
        #make projectile a sprite
        pygame.sprite.Sprite.__init__(self,self.containers)
        #set up projectile variables
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/Player_05.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.angle = angle
        self.speed = 5
        self.angle_rads = math.radians(self.angle)
        self.x_move = math.cos(self.angle_rads) * self.speed
        self.y_move = -math.sin(self.angle_rads) * self.speed
        self.image, self.rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)

    def update(self):
        self.x = self.x_move
        self.y = self.y_move
        self.rect.center = (self.x, self.y)

        self.screen.blit(self.image, self.rect)


