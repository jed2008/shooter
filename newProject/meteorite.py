import random

import pygame


class Meteorite(pygame.sprite.Sprite):

    def __init__(self, game):
        super(Meteorite, self).__init__()
        self.game = game
        self.image = self.game.imageManager.images[f"meteorite{random.randint(1, 3)}"]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.game.screen.get_width() - self.rect.w)
        self.rect.y = random.randint(-500, 0)
        self.velocity = random.randint(1, 3)

    def move(self):
        self.rect.y += self.velocity
        if self.rect.bottom >= self.game.screen.get_height():
            self.game.add_score(-5)
            self.remove()

    def remove(self):
        self.rect.x = random.randint(0, self.game.screen.get_width() - self.rect.w)
        self.rect.y = random.randint(-500, 0)
        self.velocity = random.randint(1, 3)
