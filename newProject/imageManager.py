import random

import pygame


class ImageManager:

    def __init__(self):
        self.background = pygame.transform.scale(
            self.load_image("background", "jpg"), (1080, 720))
        self.start_button = self.load_image('start', "png")
        self.start_button = pygame.transform.scale(self.start_button, (512, 512))

        self.images = {
            "background": self.background,
            "player": self.load_image("player", "png"),
            "start": self.start_button,
            "banner": self.load_image("banner", "png"),
            "banner2": self.load_image("banner2", "png")
        }

    def load_image(self, name: str, format: str):
        return pygame.image.load(f'images/{name}.{format}')

    def add_images(self):
        missil= self.load_image("missile", "png")
        missil = pygame.transform.rotozoom(missil, 45, 1)
        missil = pygame.transform.scale(missil, (128, 128))
        self.images["missile"] = missil

        for i in range(1, 4):
            image = self.load_image(f"meteorite{i}", "png")
            image = pygame.transform.rotozoom(image, 45, 1)
            size = random.randint(64, 256)
            image = pygame.transform.scale(image, (size, size))
            self.images[f"meteorite{i}"] = image



