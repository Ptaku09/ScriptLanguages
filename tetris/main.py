import pygame as py

from button import Button
from screen import Screen


def launch_game():
    py.init()
    py.font.init()

    menu_screen = Screen('Menu Screen')
    conf_screen = Screen('Configuration Screen')

    menu_screen.make_current_screen()

    play_button = Button(150, 150, 150, 50, (255, 250, 250), (255, 0, 0), (255, 255, 255), 'Play')
    control_button = Button(150, 150, 150, 50, (0, 0, 0), (0, 0, 255), (255, 255, 255), 'Back')

    done = False

    while not done:
        for event in py.event.get():
            menu_screen.screen_update()
            conf_screen.screen_update()

            mouse_pos = py.mouse.get_pos()
            mouse_click = py.mouse.get_pressed()

            if menu_screen.check_update((25, 0, 255)):
                control_bar_button = play_button.focus_check(mouse_pos, mouse_click)
                play_button.show_button(menu_screen.screen)

                if control_bar_button:
                    conf_screen.make_current_screen()
                    menu_screen.end_current_screen()

            elif conf_screen.check_update((255, 0, 255)):
                return_back = control_button.focus_check(mouse_pos, mouse_click)
                control_button.show_button(conf_screen.screen)

                if return_back:
                    conf_screen.end_current_screen()
                    menu_screen.make_current_screen()

            if event.type == py.QUIT:
                done = True

        py.display.update()

    py.quit()


if __name__ == '__main__':
    launch_game()
