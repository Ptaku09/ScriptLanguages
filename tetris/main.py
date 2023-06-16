import sys

import pygame

from block import possible_colors
from button import Button
from checkbox import Checkbox
from input_box import InputBox
from tetris import GameStates, Tetris
from utils import get_font, FieldSize, extract_field_size, store_result

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Tetris")

bg = pygame.image.load("assets/images/background.jpg")


def configuration_screen():
    username_input = InputBox((375, 300), 530, 60)

    small_field_checkbox = Checkbox((430, 500), text=FieldSize.SMALL.value)
    medium_field_checkbox = Checkbox((580, 500), text=FieldSize.MEDIUM.value)
    large_field_checkbox = Checkbox((730, 500), text=FieldSize.LARGE.value)
    checkboxes = [small_field_checkbox, medium_field_checkbox, large_field_checkbox]

    while True:
        conf_mouse_pos = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))

        conf_text = get_font(45).render("CONFIGURATION", True, "White")
        conf_rect = conf_text.get_rect(center=(640, 100))
        screen.blit(conf_text, conf_rect)

        username_text = get_font(25).render("Username:", True, "White")
        username_rect = username_text.get_rect(center=(490, 275))
        screen.blit(username_text, username_rect)

        field_size_text = get_font(25).render("Field size:", True, "White")
        field_size_rect = field_size_text.get_rect(center=(520, 470))
        screen.blit(field_size_text, field_size_rect)

        conf_back = Button(pos=(500, 650), text_input="BACK", font=get_font(40), base_color="White",
                           hovering_color="#f0d467")

        conf_play = Button(pos=(780, 650), text_input="PLAY", font=get_font(40), base_color="White",
                           hovering_color="#f0d467")

        for button in [conf_back, conf_play]:
            button.change_color(conf_mouse_pos)
            button.update(screen)

        for checkbox in checkboxes:
            checkbox.draw(screen)

        username_input.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if conf_back.check_for_input(conf_mouse_pos):
                    menu_screen()
                if conf_play.check_for_input(conf_mouse_pos):
                    username = username_input.get_text()
                    username = "Player" if username == "" else username
                    selected = [c for c in checkboxes if c.checked]
                    field_size = FieldSize.LARGE.value if len(selected) == 0 else selected[0].text
                    play_screen(username, field_size)

            # make sure only one checkbox is checked
            for checkbox in checkboxes:
                if checkbox.check_for_input(event):
                    for c in checkboxes:
                        c.checked = False
                    checkbox.checked = True

            username_input.handle_event(event)

        pygame.display.update()


def play_screen(username, field_size):
    fs = extract_field_size(field_size)
    clock = pygame.time.Clock()
    fps = 25
    game = Tetris((640 - 30 * fs[1], 100), fs[0], fs[1])
    counter = 0
    is_result_stored = False

    pressing_down = False

    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        screen.blit(bg, (0, 0))

        score_text = get_font(25).render(f"Score: {game.score}", True, "White")
        score_rect = score_text.get_rect()
        score_rect.top = 100
        score_rect.left = 680
        screen.blit(score_text, score_rect)

        level_text = get_font(25).render(f"Level: {game.level - 1}", True, "White")
        level_rect = level_text.get_rect()
        level_rect.top = 150
        level_rect.left = 680
        screen.blit(level_text, level_rect)

        player_text = get_font(25).render(f"Player: {username}", True, "White")
        player_rect = player_text.get_rect()
        player_rect.top = 200
        player_rect.left = 680
        screen.blit(player_text, player_rect)

        play_menu = Button(pos=(900, 550), text_input="MENU", font=get_font(40), base_color="White",
                           hovering_color="#f0d467")

        play_again = Button(pos=(900, 650), text_input="PLAY AGAIN", font=get_font(40), base_color="White",
                            hovering_color="#f0d467")

        if game.state == GameStates.END:
            if not is_result_stored:
                store_result(username, game.score, game.level - 1, field_size)
                is_result_stored = True

            for button in [play_menu, play_again]:
                button.change_color(play_mouse_pos)
                button.update(screen)

        # generate the initial block
        if game.block is None:
            game.new_block()

        counter += 1

        if counter > 100000:
            counter = 0

        # manage the speed of the block
        if counter % game.get_speed() == 0 or pressing_down:
            if game.state == GameStates.START:
                game.go_down()

        # draw the field and frozen blocks
        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, "White",
                                 [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, possible_colors[game.field[i][j]],
                                     [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2,
                                      game.zoom - 1])

        # draw the falling block
        if game.block is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.block.image():
                        pygame.draw.rect(screen, possible_colors[game.block.color],
                                         [game.x + game.zoom * (j + game.block.x) + 1,
                                          game.y + game.zoom * (i + game.block.y) + 1,
                                          game.zoom - 2, game.zoom - 2])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    pressing_down = True
                if event.key == pygame.K_LEFT:
                    game.go_side(-1)
                if event.key == pygame.K_RIGHT:
                    game.go_side(1)
                if event.key == pygame.K_SPACE:
                    game.go_space()
                if event.key == pygame.K_ESCAPE:
                    game.state = GameStates.END
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False
            if event.type == pygame.MOUSEBUTTONUP:
                if play_menu.check_for_input(play_mouse_pos):
                    menu_screen()
                if play_again.check_for_input(play_mouse_pos):
                    game.__init__((640 - 30 * fs[1], 100), fs[0], fs[1])
                    is_result_stored = False

        pygame.display.update()
        clock.tick(fps)


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
