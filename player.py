import pygame

class Player():
    # Player constructor function (stuff that happens right when you make player)
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("/Users/dashnican/Desktop/coding/my_first_game/assets/Player_05.png")
        self.speed = 5

    # Player update function (stuff to happen over and over again)
    def update(self):
        self.screen.blit(self.image, (self.x, self.y))
        
    def move(self, x_movement, y_movement):
        self.x += self.speed * x_movement
        self.y += self.speed * y_movement