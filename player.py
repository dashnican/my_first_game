import pygame
import toolbox
import projectile
import crate

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
        self.healthpoints = 5000
        self.alive = True 
        self.hitcooldown = 4
        self.health_bar_width = self.image.get_width()
        self.health_bar_height = 8
        self.health_bar_green = pygame.Rect(0, 0, self.health_bar_width, self.health_bar_height)
        self.health_bar_red = pygame.Rect(0, 0, self.health_bar_width, self.health_bar_height)
        self.crateammo = 10000
        self.cratecooldown = 0
    # Player update function (stuff to happen over and over again)
    def update(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                self.getHit(enemy.damage)

        self.rect.center = (self.x, self.y)
        if self.shoot_cooldown > 0:
            self.shoot_cooldown = self.shoot_cooldown -1

        #get the angle between the player and the mouse
        if self.alive:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.angle = toolbox.angleBetweenPoints(self.x, self.y, mouse_x, mouse_y)

        if self.alive:
            self.hitcooldown = self.hitcooldown - 1
            if self.hitcooldown > 0:
                self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/Player_02hurt.png")
            else:
                self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/Player_02.png")
        else:  
            self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/LargeExplosion2.png")

        image_to_draw, image_rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)

        if self.cratecooldown > 0:
            self.cratecooldown = self.cratecooldown -1
        self.screen.blit(image_to_draw, image_rect)

        self.draw_healthbar()
        
    def move(self, x_movement, y_movement):
        if self.alive:
            self.x += self.speed * x_movement
            self.y += self.speed * y_movement

    #player can now die
    def getHit(self, damage):
       if self.alive == True:
           self.healthpoints = self.healthpoints - damage
           self.hitcooldown = 5
           if self.healthpoints <= 0:
                self.healthpoints = 0
                self.alive = False
                
        
    def shoot(self):
        if self.shoot_cooldown <=0 and self.alive:
            self.shoot_cooldown = self.shoot_cooldown_max
            projectile.Projectile(self.screen, self.x, self.y, self.angle)
    #added a depleting healthbar
    def draw_healthbar(self):
        self.health_bar_red.x = self.rect.x
        self.health_bar_red.bottom = self.rect.y - 5
        pygame.draw.rect(self.screen, (255, 0, 0), self.health_bar_red)
        self.health_bar_green.topleft = self.health_bar_red.topleft
        print(self.healthpoints)
        healthpercentage = self.healthpoints / 5000
        print(healthpercentage)
        self.health_bar_green.width = healthpercentage * self.health_bar_width

        if self.alive:
            pygame.draw.rect(self.screen, (0, 255, 0), self.health_bar_green)

    def placeCrate(self):
        if self.alive and self.crateammo >0 and self.cratecooldown <= 0:
            self.crateammo = self.crateammo -1 
            self.cratecooldown = 5
            crate.Crate(self.screen, self.x, self.y, self)
            




    
