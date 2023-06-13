import sys

import pygame

from button import Button

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Tetris")

bg = pygame.image.load("assets/images/background.jpg")


def get_font(size):
    return pygame.font.Font("assets/fonts/tetris.ttf", size)


def configuration_screen():
    while True:
        conf_mouse_pos = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))

        conf_text = get_font(45).render("CONFIGURATION", True, "White")
        conf_rect = conf_text.get_rect(center=(640, 100))
        screen.blit(conf_text, conf_rect)

        conf_back = Button(pos=(640, 460), text_input="BACK", font=get_font(75), base_color="White",
                           hovering_color="#f0d467")

        conf_back.change_color(conf_mouse_pos)
        conf_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if conf_back.check_for_input(conf_mouse_pos):
                    menu_screen()

        pygame.display.update()


def results_screen():
    while True:
        results_mouse_pos = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))

        results_text = get_font(45).render("BEST RESULTS", True, "White")
        results_rect = results_text.get_rect(center=(640, 100))
        screen.blit(results_text, results_rect)

        results_back = Button(pos=(640, 460), text_input="BACK", font=get_font(75), base_color="White",
                              hovering_color="#f0d467")

        results_back.change_color(results_mouse_pos)
        results_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if results_back.check_for_input(results_mouse_pos):
                    menu_screen()

        pygame.display.update()


def menu_screen():
    while True:
        menu_mouse_pos = pygame.mouse.get_pos()
        
        screen.blit(bg, (0, 0))

        menu_text = get_font(100).render("TETRIS", True, "#f1c40f")
        menu_rect = menu_text.get_rect(center=(640, 100))
        screen.blit(menu_text, menu_rect)

        play_button = Button(pos=(640, 250), text_input="PLAY", font=get_font(75), base_color="White",
                             hovering_color="#f0d467")
        results_button = Button(pos=(640, 400), text_input="BEST RESULTS", font=get_font(75), base_color="White",
                                hovering_color="#f0d467")
        quit_button = Button(pos=(640, 550), text_input="QUIT", font=get_font(75), base_color="White",
                             hovering_color="#f0d467")

        for button in [play_button, results_button, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if play_button.check_for_input(menu_mouse_pos):
                    configuration_screen()
                if results_button.check_for_input(menu_mouse_pos):
                    results_screen()
                if quit_button.check_for_input(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


menu_screen()
