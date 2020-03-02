import pygame
import pygame.gfxdraw

from Colors import (
    GRANNY_SMITH_APPLE, BLACK, WHITE, BLUE, ORANGE
)
from Button import Button, QuitButton, PlayButton
from TextLabel import TextLabel
from GradientHandler import GradientHandler
from Card import Card


class App:
    def __init__(self):
        self.running = True
        self.app_objects = []
        self.startPage = True
        self.font = 'freesansbold.ttf'
        self.window_width, self.window_height = self.window_size = (800, 600)
        self.clock = pygame.time.Clock()
        self.hovered_obj = None
        self.background_path = GradientHandler.download_gradient(self.window_width, self.window_height)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.window_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        self.running = True
        self.generate_start_page()

    def generate_start_page(self):
        def click_func():
            self.running = False
        button = QuitButton(self._display_surf, click_func)
        self.app_objects.append(button)

        def click_func():
            self.generate_gameboard()
        button = PlayButton(self._display_surf, click_func)
        self.app_objects.append(button)

    def generate_gameboard(self):
        self.app_objects = []
        t = TextLabel(40, (self.window_width/2, self.window_height * 0.05), "Welcome!", self._display_surf)
        self.app_objects.append(t)

        card = Card((50, 100), self._display_surf, 'S', 'A')
        self.app_objects.append(card)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in self.app_objects:
                if hasattr(b, 'is_hovered') and b.is_hovered():
                    b.on_click()

    def create_button(self, size, position, color, text, hover_func, click_func):
        button = Button(size, position, color, text, self._display_surf, hover_func, click_func)
        self.app_objects.append(button)

    def on_loop(self):
        pass

    def on_render(self):
        current_surface = pygame.display.get_surface()
        # self.draw_gradient_background()
        an = pygame.image.load(self.background_path)
        current_surface.blit(an, (0, 0))
        for b in self.app_objects:
            b.show()

        pygame.display.update()
        self.clock.tick(30)
        # pygame.display.flip()

    def on_cleanup(self):
        print('Bye bye!')
        pygame.quit()

    def over_button(self):
        for b in self.app_objects:
            if b.is_hovered():
                b.on_hover()
                return True
        return False

    def draw_gradient_background(self):
        rng = (8, 230)
        x = rng[0]
        dx = (rng[1] - rng[0]) / self.window_width
        for col in range(self.window_width):
            x += dx
            if x > rng[1]:
                x = rng[0]
            color = (20, int(x), 130)
            for p in range(self.window_height):
                pygame.gfxdraw.pixel(self._display_surf, col, p, color)

    def get_hovered_object(self):
        for b in self.app_objects:
            if hasattr(b, 'is_hovered') and b.is_hovered():
                return b
        return None

    def on_app_objects_loop(self):
        temp_obj = self.get_hovered_object()
        if temp_obj:
            self.hovered_obj = temp_obj
            self.hovered_obj.on_hover()
        else:
            if self.hovered_obj:
                self.hovered_obj.reset_hover()
                self.hovered_obj = None

    def on_execute(self):
        self.on_init()

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

            self.on_app_objects_loop()
            # if not self.over_button():
            #     pygame.mouse.set_cursor(*pygame.cursors.arrow)

        self.on_cleanup()