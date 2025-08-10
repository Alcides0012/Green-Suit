import pygame

pygame.init()
class greensuit(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface((20,30))
        self.rect = self.image.get_rect()

