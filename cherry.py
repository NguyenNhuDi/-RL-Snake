import pygame
from CONSTANTS import *


class Cherry(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.mask = None
        self.x = x
        self.y = y

        self.w = SCREEN_WIDTH / 100
        self.h = SCREEN_HEIGHT / 100

        self.color = (215, 15, 242)

        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(color=tuple(self.color))

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.image, self.rect)
