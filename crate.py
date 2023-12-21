import pygame
import math
import toolbox

class Crate(pygame.sprite.Sprite):

    def __init__ (self,screen,x,y,player):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/powerupCrate.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.player = player
        self.healthpoints = 1000
        self.hitcooldown = 0
        self.imagehurt = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/SmallExplosion1.png")
        self.just_placed = True

    def update(self, projectiles):

        if not self.rect.colliderect(self.player.rect):
            self.just_placed = False 

        for projectile in projectiles:
            if self.rect.colliderect(projectile.rect):
                self.getHit(projectile.damage)
                projectile.explode()
        if self.hitcooldown > 0:
            self.hitcooldown = self.hitcooldown - 1
            imagetodraw = self.imagehurt
        else:
            imagetodraw = self.image

            self.screen.blit(imagetodraw, self.rect)
                
    def getHit(self, damage):
        self.hitcooldown = 1.5
        self.healthpoints -= damage
        if self.healthpoints <= 0: 
            self.kill()