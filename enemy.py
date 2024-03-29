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
        self.damage = 50
        
    def update(self, projectiles, crates):
        #getting the angle from the enemy's position to the player's location
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, self.player.x, self.player.y)
        self.angle_rads = math.radians(self.angle)
        #getting the enemy to move in that angle
        self.x_move = math.cos(self.angle_rads) * self.speed
        self.y_move = -math.sin(self.angle_rads) * self.speed
        #check if the enemy is moving into the crates
        new_x = self.x + self.x_move
        new_y = self.y + self.y_move
        test_rect = self.rect

        test_rect.center = (new_x,self.y)
        for crate in crates:
            if test_rect.colliderect(crate.rect):
                crate.getHit(self.damage)
                self.getHit(crate.damage)
                new_x = self.x

        test_rect.center = (new_y,self.x)
        for crate in crates:
            if test_rect.colliderect(crate.rect):
                crate.getHit(self.damage)
                self.getHit(crate.damage)
                
                new_y = self.y

        self.x = new_x
        self.y = new_y
        self.rect.center = (new_x, new_y)
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


        