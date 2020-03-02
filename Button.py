import pygame

from Colors import BLACK, ORANGE
from TextLabel import TextLabel
from AppObject import AppObject


class Button:

    def __init__(self, surface, click_func):
        self.color = ORANGE
        self.surface = surface
        self.size = self.width, self.height = (self.surface.get_width()*0.25, self.surface.get_height()*0.15)
        self.text_height = int(0.7 * self.height)
        self.hovered = False
        self.click_func = click_func

    def hover_func(self):
        pygame.mouse.set_cursor(*pygame.cursors.tri_left)

    def is_hovered(self):
        mouse_position = pygame.mouse.get_pos()
        if self.x <= mouse_position[0] <= self.x + self.width and \
            self.y <= mouse_position[1] <= self.y + self.height:
            return True
        return False

    def generate_text(self):
        textLabel = TextLabel(
            int(self.height*0.7),
            (self.x + (self.width/2), self.y + (self.height/2)),
            self.text,
            self.surface)
        textLabel.show()

    def reset_hover(self):
        self.hovered = False
        self.color = ORANGE
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def on_click(self):
        self.click_func()


class QuitButton(Button):

    def __init__(self, surface, click_func):
        super(QuitButton, self).__init__(surface, click_func)
        screen_width, screen_height =  self.surface.get_size()
        self.x, self.y = (screen_width / 2 - self.width / 2, screen_height * 0.7)
        self.text = 'Exit'

        self.shape = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height)

    def show(self):
        pygame.draw.rect(self.surface, self.color, self.shape)
        self.generate_text()

    def on_hover(self):
        self.hover_func()
        if not self.hovered:
            self.color = (
                self.color[0] + 20,
                self.color[1] + 60,
                self.color[2] + 60)
            self.hovered = True


class PlayButton(Button):

    def __init__(self, surface, click_func):
        super(PlayButton, self).__init__(surface, click_func)
        screen_width, screen_height =  self.surface.get_size()
        self.x, self.y = (screen_width / 2 - self.width / 2, screen_height * 0.4)
        self.text = 'Play'

        self.shape = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height)

    def show(self):
        pygame.draw.rect(self.surface, self.color, self.shape)
        self.generate_text()

    def on_hover(self):
        self.hover_func()
        if not self.hovered:
            self.color = (
                self.color[0] + 20,
                self.color[1] + 60,
                self.color[2] + 60)
            self.hovered = True



# class Button(AppObject):

#     def __init__(self, size, position, color, text, screen, hover_func, click_func):

#         self.size = self.width, self.height = size
#         self.color = color
#         self.text = text

#         self.on_init(position, screen, hover_func, click_func)

#         self.shape = pygame.Rect(
#             self.x,
#             self.y,
#             self.width,
#             self.height)

#     def click(self):
#         self.click_func()

#     def is_clicked(self):
#         mouse_position = pygame.mouse.get_pos()
#         if self.x <= mouse_position[0] <= self.x + self.width and \
#             self.y <= mouse_position[1] <= self.y + self.height:
#             return True
#         return False

#     def is_hovered(self):
#         mouse_position = pygame.mouse.get_pos()
#         if self.x <= mouse_position[0] <= self.x + self.width and \
#             self.y <= mouse_position[1] <= self.y + self.height:
#             return True
#         return False

#     def on_hover(self):
#         self.hover_func()

#     def on_click(self):
#         self.click_func()

#     def generate_text(self):
#         textLabel = TextLabel(
#             int(self.height*0.7),
#             (self.x + (self.width/2), self.y + (self.height/2)),
#             self.text,
#             BLACK,
#             self.surface,
#             lambda: '',
#             lambda: '')
#         textLabel.show()

#     def show(self):
#         pygame.draw.rect(self.surface, self.color, self.shape)
#         self.generate_text()
