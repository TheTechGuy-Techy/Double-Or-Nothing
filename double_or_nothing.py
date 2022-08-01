#!/usr/bin/python
import pygame
from pygame.locals import *

pygame.init()
game_name = "DOUBLE OR NOTHING"
window_title = f"{game_name[0].upper()}{game_name[1:10].lower()}{game_name[10].upper()}{game_name[11:].lower()}"

# Initialising the window
window_width = window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)

# Variables
FPS = 60
clock = pygame.time.Clock()
font = pygame.font.get_fonts()[1]

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NEON_RED = (222, 23, 56)
BRIGHT_RED = (255, 22, 12)
GREEN = (0, 255, 0)

# Font function
def text(font, size, dialogue, colour):
    return pygame.font.SysFont(font, size).render(dialogue, True, colour)

# @param: pos_n_size --> [x, y, width, height]
# @param: name_pos   --> [x, y] for the button name
def button(name, name_pos, inactive_colour, active_colour, pos_n_size, function = None):
    pos_n_size = tuple(pos_n_size)
    if pos_n_size[0] + pos_n_size[2] > mouse_position[0] > pos_n_size[0] and pos_n_size[1] + pos_n_size[3] > mouse_position[1] > pos_n_size[1]:
        pygame.draw.rect(window, active_colour, pos_n_size)
        if mouse_click[0] and function != None:
            function()
    else:
        pygame.draw.rect(window, inactive_colour, pos_n_size)
    window.blit(text(font, 20, name, WHITE), tuple(name_pos))


def close():
    pygame.quit()
    quit()

# Buttons
play = button
play_name_pos = [(35 / 3) + (150 / 2), (400 - 20) + (150 / 2)]
exit = button
exit_name_pos = [(410 - 20) + (150 / 2), (400 - 20) + (150 / 2)]

def game_intro():
    while True:
        global mouse_position, mouse_click
        mouse_position = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
        window.fill(BLACK)
        window.blit(text(font, 70, game_name[0:6], WHITE), (140, 60))
        window.blit(text(font, 50, game_name[7:9], WHITE), (270, 155))
        window.blit(text(font, 70, game_name[10:], WHITE), (120, 225))
        window.blit(text(font, 15, "TheTechGuy", WHITE), (260, 315))

        play("Play", play_name_pos, NEON_RED, BRIGHT_RED, [35, 400, 150, 150], main_game)
        exit("Quit", exit_name_pos, NEON_RED, BRIGHT_RED, [410, 400, 150, 150], close)

        clock.tick(FPS)
        pygame.display.update()

def flashing_text():
    x = (game_name[0:6], game_name[10:])
    for i in x:
        pygame.draw.rect(window, GREEN, (window_width / 2 - 270, window_height / 2 - 70, 540, 120))
        if i is x[0]:
            window.blit(text(font, 80, i, WHITE), (window_width / 2 - 180, window_height / 2 - 70))
        else:
            window.blit(text(font, 80, i, WHITE), (window_width / 2 - 190, window_height / 2 - 70))
        pygame.display.update()

def main_game():
    score = 100
    score_text = text
    back = button
    back_name_pos = [(150 - 40) + (350 / 2), (175 - 20) + (150 / 2)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
        window.fill(BLACK)
        #flashing_text()
        back("Back", back_name_pos, NEON_RED, BRIGHT_RED, [220, 450, 175, 75], game_intro)
        clock.tick(FPS)
        pygame.display.update()

game_intro()
main_game()