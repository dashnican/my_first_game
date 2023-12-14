import pygame
import math
import toolbox

class Crate(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, player):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/powerupCrate.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.player = player
        self.healthpoints = 10000
        self.imagehurt = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/SmallExplosion1.png")
    
    def update(self):
        