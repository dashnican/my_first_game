import pygame
import toolbox
import projectile

class Player(pygame.sprite.Sprite):
    # Player constructor function (stuff that happens right when you make player)
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/Player_02.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.angle = 0
        self.speed = 5
        self.shoot_cooldown = 0
        self.shoot_cooldown_max = 10
        self.healthpoints = 1000
        self.alive = True 
        self.hitcooldown = 0

    # Player update function (stuff to happen over and over again)
    def update(self, enemies):
        self.rect.center = (self.x, self.y)
        if self.shoot_cooldown > 0:
            self.shoot_cooldown = self.shoot_cooldown -1

        #get the angle between the player and the mouse
        if self.alive:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.angle = toolbox.angleBetweenPoints(self.x, self.y, mouse_x, mouse_y)

        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                self.getHit(enemy.damage)

        

        if self.alive:
            self.hitcooldown = self.hitcooldown - 1
            if self.hitcooldown > 0:
                self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/Player_02hurt.png")
            else:
                self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/Player_02.png")
        else:
            self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/LargeExplosion2.png")

        image_to_draw, image_rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)

        self.screen.blit(image_to_draw, image_rect)
        
    def move(self, x_movement, y_movement):
        if self.alive:
            self.x += self.speed * x_movement
            self.y += self.speed * y_movement

    #player can now die
    def getHit(self, damage):
       if self.alive == True:
           self.healthpoints = self.healthpoints - damage
           print(self.healthpoints)
           self.hitcooldown = 5
           if self.healthpoints <= 0:
                self.healthpoints = 0
                self.alive == False
                
        
    def shoot(self):
        if self.shoot_cooldown <=0 and self.alive:
            self.shoot_cooldown = self.shoot_cooldown_max
            projectile.Projectile(self.screen, self.x, self.y, self.angle)