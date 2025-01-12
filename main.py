import random
from typing import List

import pygame
from CONSTANTS import *
from cherry import Cherry


def spawn_cherry(cherries: List[Cherry]):
    sX = random.randint(SCREEN_WIDTH / 100, SCREEN_WIDTH - SCREEN_WIDTH / 100)
    sY = random.randint(SCREEN_HEIGHT / 100, SCREEN_HEIGHT - SCREEN_HEIGHT / 100)

    cherries.append(Cherry(sX, sY))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(f'Snake')

    gameOn = True
    start_time = pygame.time.get_ticks()
    curr_time = start_time
    cherries = []

    while gameOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False

        screen.fill((255, 255, 255))

        if len(cherries) < MAX_CHERRY:
            spawn_cherry(cherries)

        for cherry in cherries:
            cherry.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
