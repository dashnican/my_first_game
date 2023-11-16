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
        self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/BalloonSmall.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.angle = angle
        self.speed = 10
        self.angle_rads = math.radians(self.angle)
        self.x_move = math.cos(self.angle_rads) * self.speed
        self.y_move = -math.sin(self.angle_rads) * self.speed
        self.image, self.rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)

    def update(self):
        self.x += self.x_move
        self.y += self.y_move
        self.rect.center = (self.x, self.y)

        #removing balloon going out of bounds
        if self.x < -self.image.get_width():
            self.kill()
        elif self.x > self.screen.get_width() + self.image.get_width():
            self.kill()
        elif self.y < -self.image.get_height():
            self.kill()
        elif self.y > self.screen.get_height() + self.image.get_height():
            self.kill()
        self.screen.blit(self.image, self.rect)



