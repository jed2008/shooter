import pygame
from imageManager import ImageManager
from meteorite import Meteorite
from player import Player
from missile import Missile


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((1080,720))
        pygame.display.set_caption("Game")

        self.imageManager = ImageManager()
        self.imageManager.add_images()
        self.player_image = self.imageManager.images.get("player")

        self.player = Player(self, 450, 550)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)

        self.all_missiles = pygame.sprite.Group()
        self.all_meteorites = pygame.sprite.Group()
        for meteorite in range(10):
            self.all_meteorites.add(Meteorite(self))

        self.score = 0
        self.font = pygame.font.SysFont('Arial', 30, True)

        self.running = True
        self.is_playing = False

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            #print(True)
            if self.is_playing:
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0:
                        #print(event.value)
                        if event.value == 1:
                            self.player.move_right()
                        elif event.value <= -1:
                            self.player.move_left()

                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 1:
                        sound_tir = self.load_sound('tir', "waw")
                        pygame.mixer.music.play()
                        #print("TIR")
                        self.all_missiles.add(
                            Missile(self.player, self.player.rect.x - 50, self.player.rect.y - 35))
                        self.all_missiles.add(
                            Missile(self.player, self.player.rect.x + 50, self.player.rect.y - 35))
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    self.is_playing = True

    def display(self):
        self.screen.blit(self.imageManager.images.get("background"), (0, 0))
        if self.is_playing:
            self.screen.blit(self.player.image,
                             (self.player.rect.x, self.player.rect.y))
            for missil in self.all_missiles:
                missil.move()
                if self.check_collide(missil, self.all_meteorites):
                    missil.touch = True
            for meteorite in self.all_meteorites:
                meteorite.move()
                if self.check_collide(meteorite, self.all_missiles):
                    sound_meteorite = self.load_sound('explosion', "waw")
                    pygame.mixer.music.play()
                    meteorite.remove()
                    self.add_score(10)

                if self.check_collide(meteorite, self.all_players):

                    meteorite.remove()
                    self.add_score(-5)
                    self.player.health -= 5
                    if self.player.health <= 0:
                        self.game_over()

            for missil in self.all_missiles:
                if missil.touch:
                    missil.kill()
            self.all_missiles.draw(self.screen)
            self.all_meteorites.draw(self.screen)

            self.player.health_bar()

            self.text = self.font.render(f"Score : {self.score}", True, 'red')
            self.screen.blit(self.text, (30, 30))

        else:
            self.screen.blit(self.imageManager.images.get("banner2"), (260, 150))
            self.screen.blit(self.imageManager.images.get("banner"), (284, 450))
            self.screen.blit(self.imageManager.images.get("start"), (284, 100))
            txt = self.font.render("Appuyez sur la touche A pour jouer", True, "red")
            self.screen.blit(txt, (284, 200))


    def game_loop(self):
        while self.running:
            self.display()
            self.get_events()
            pygame.display.update()
            pygame.display.flip()

    def check_collide(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def add_score(self, points):
        self.score += points
        if self.score <= -100:
            self.game_over()

    def game_over(self):
        self.is_playing = False
        self.score = 0
        self.player.health = self.player.max_health
        for missile in self.all_missiles:
            missile.kill()
        for meteorite in self.all_meteorites:
            meteorite.remove()

    def load_sound(self, name, format):
        return pygame.mixer.music.load(f"sounds/{name}.{format}")