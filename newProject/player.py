import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, game, x: int, y: int):
        super().__init__()
        self.game = game
        self.image = self.game.player_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 20
        self.health = 100
        self.max_health = 100

    def move_right(self):
        self.rect.x += self.velocity
        if self.rect.x > 1080:
            self.move_left()

    def move_left(self):
        self.rect.x -= self.velocity
        if self.rect.left < 0:
            self.move_right()

    def health_bar(self):

        health_bar = pygame.rect.Rect(self.rect.x + 14, self.rect.bottom + 10, self.health, 10)
        max_health_bar = pygame.rect.Rect(self.rect.x + 14, self.rect.bottom + 10, self.max_health, 10)

        pygame.draw.rect(self.game.screen, 'black', max_health_bar)
        pygame.draw.rect(self.game.screen, 'green', health_bar)