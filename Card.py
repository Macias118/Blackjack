import pygame


class Card:
    def __init__(self, position, surface, suit, symbol):
        self.surface = surface
        self.suit = suit
        self.symbol = symbol
        self.x, self.y = self.position = position
        self.height = int(self.surface.get_height() * 0.2)
        self.image_path = f'Deck/{self.symbol}{self.suit}.png'

    def show(self):
        loaded_image = pygame.image.load(self.image_path)
        loaded_image = pygame.transform.scale(
            loaded_image,
            (
                int(loaded_image.get_width() * self.height / loaded_image.get_height()),
                int(self.height)
            ))
        self.surface.blit(loaded_image, (self.x, self.y))
