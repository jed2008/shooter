import pygame
from game import Game
pygame.init()

game = Game()

pygame.joystick.init()
joysticks = []

for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    #print("INIT")
for j in joysticks:
    j.init()

def main():
    game.game_loop()

if __name__ == '__main__':
    main()