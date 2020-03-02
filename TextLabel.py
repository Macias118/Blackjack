import pygame

from Colors import BLACK, AQUA


class TextLabel:
    _FONT = 'freesansbold.ttf'

    def __init__(self, height, position, value, surface):
        self.height = height
        self.x, self.y = self.position = position
        self.value = value
        self.surface = surface
        self.color = BLACK

    def show(self):
        pygame.draw.ellipse(self.surface, AQUA, (self.x, self.y, self.height, 50))

        customFont = pygame.font.Font(self._FONT, self.height)
        textSurface = customFont.render(self.value, True, self.color)
        textShape = textSurface.get_rect()
        
        textShape.center = (self.position)
        self.surface.blit(textSurface, textShape)



# class TextLabel(AppObject):

#     _FONT = 'freesansbold.ttf'

#     def __init__(self, height, position, text, color, screen, hover_func, click_func):
#         self.height = height
#         self.text = text
#         self.color = color

#         self.on_init(position, screen, hover_func, click_func)

#     def show(self):
#         customFont = pygame.font.Font(self._FONT, self.height)
#         textSurface = customFont.render(self.text, True, self.color)
#         textShape = textSurface.get_rect()
        
#         textShape.center = (self.x, self.y)
#         self.surface.blit(textSurface, textShape)