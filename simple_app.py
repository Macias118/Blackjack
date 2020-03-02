import pygame
import requests
import signal
import threading
import time

from Colors import (
    ORANGE, BLUE, BLACK, WHITE
)

MAIN_FONT = 'freesansbold.ttf'
WIN_WIDTH, WIN_HEIGHT = WIN_SIZE = ( 600, 400 )
CLOCK = pygame.time.Clock()
app_buttons = {}
button_funcs = {}


def log(msg, level='info'):
    possible_levels = [
        'info',
        'warning',
        'error'
    ]
    if level not in possible_levels:
        level = 'info'
    print(f'{level.upper()}: {msg}')

def on_init():
    pygame.init()
    display_surf = pygame.display.set_mode(self.window_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.mouse.set_cursor(*pygame.cursors.arrow)

def on_execute():
    running = True

def load_backround(bg_obj):
    surface = pygame.display.get_surface()
    surface.blit(bg_obj, (0,0))

def on_render():
    pygame.display.update()
    CLOCK.tick(60)

def start_game():
    print('!! **Welcome to BLACKJACK** !!')

def on_exit():
    print('Bye bye!')
    pygame.quit()
    exit()

def create_background():
    url = f'https://picsum.photos/{WIN_WIDTH}/{WIN_HEIGHT}'
    try:
        response = requests.get(url, timeout=5)
    except Exception as e:
        log(f'Could not download background :: {e}', 'warning')
        create_error_background()
    else:
        filepath = f'gradients/background{WIN_WIDTH}x{WIN_HEIGHT}.jpg'
        with open(filepath, 'wb') as f:
            for chunk in response:
                f.write(chunk)
        load_background_from_file(filepath)

def load_background_from_file(bg_filepath):
    try:
        bg = pygame.image.load(bg_filepath)
    except Exception as e:
        log(f'Could not load background :: {e}', 'warning')
        create_error_background()
    else:
        pygame.display.get_surface().blit(bg, (0,0))

def create_error_background():
    pygame.display.get_surface().fill(BLUE)
    show_text(size=int(WIN_HEIGHT * 0.025), value='WARNING: Can not load background', color=WHITE)

def show_text(size=15, position=(WIN_WIDTH/2,10), value='', color=BLACK):
    customFont = pygame.font.Font(MAIN_FONT, size)
    textSurface = customFont.render(value, True, color)
    textShape = textSurface.get_rect()
    
    textShape.center = (position[0], position[1])
    pygame.display.get_surface().blit(textSurface, textShape)

def show_menu_page():
    button_width = WIN_WIDTH * 0.2
    play_button = create_button_rect(WIN_WIDTH / 2 - button_width / 2, WIN_HEIGHT * 0.4, 'PLAY')
    exit_button = create_button_rect(WIN_WIDTH / 2 - button_width / 2, WIN_HEIGHT * 0.6, 'EXIT')

def create_button_rect(x, y, text=''):
    surface = pygame.display.get_surface()
    button_width, button_height = WIN_WIDTH * 0.2, WIN_HEIGHT * 0.1

    r = pygame.Rect(
        x,
        y,
        button_width,
        button_height)
    app_buttons[text] = r
    return r

def show_button(r, color=ORANGE, text=''):
    surface = pygame.display.get_surface()
    pygame.draw.rect(surface, color, r)
    show_text(size=int(r.height*0.7), position=(r.x + r.width/2, r.y + r.height/2), value=text)

def is_button_hovered(b):
    mouse_position = pygame.mouse.get_pos()
    return (b.x <= mouse_position[0] <= b.x + b.width and \
        b.y <= mouse_position[1] <= b.y + b.height)

def show_all_buttons():
    is_cursor_changed = False
    for text, button in app_buttons.items():
        current_color = ORANGE
        if is_button_hovered(button):
            current_color = (
                ORANGE[0] + 20,
                ORANGE[1] + 40,
                ORANGE[2] + 40)
            is_cursor_changed = True
        show_button(button, color=current_color, text=text)
    if is_cursor_changed:
        pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    else:
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

def exec_exit():
    on_exit()

button_funcs['EXIT'] = exec_exit


if __name__ == '__main__':
    game_running = True
    pygame.init()
    pygame.display.set_mode(WIN_SIZE)
    clock = pygame.time.Clock()
    create_background()
    show_menu_page()

    while game_running:
        show_all_buttons()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for text, button in app_buttons.items():
                    if is_button_hovered(button):
                        try:
                            button_funcs[text]()
                        except Exception as e:
                            log(f'Can not run {text} function: {e}', 'error')
        on_render()
    on_exit()
