import pygame


class Missile(pygame.sprite.Sprite):

    def __init__(self, player, x,y):
        super(Missile, self).__init__()
        self.image = player.game.imageManager.images["missile"]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 3
        self.touch = False

    def move(self):
        self.rect.y -= self.velocity
        if self.rect.bottom <= 0:
            self.kill()

