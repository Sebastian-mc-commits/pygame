from utilities import py_game
from screen import get_background, draw_main, menu_view
from Player import Player
from Traps import Fire
from Objects import Block
from movement import handle_move
from utilities import HEIGHT, WIDTH, FPS, window, set_sound


def main(window):
    clock = py_game.time.Clock()
    background, bg_image = get_background("Blue.png")

    block_size = 96

    player = Player(100, 100, 50, 50)
    fire = Fire(100, HEIGHT - block_size - 64, 16, 32)
    fire.on()
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    objects = [*floor, Block(0, HEIGHT - block_size * 2, block_size),
               Block(block_size * 3, HEIGHT - block_size * 4, block_size), fire]

    offset_x = 0
    scroll_area_width = 200
    show_menu = True

    run = True
    while run:
        clock.tick(FPS)

        for event in py_game.event.get():
            if event.type == py_game.QUIT:
                run = False
                break

            if event.type == py_game.KEYDOWN:
                if event.key == py_game.K_SPACE and player.jump_count < 2:
                    player.jump()

        keys = py_game.key.get_pressed()

        if keys[py_game.K_ESCAPE] and not show_menu:
            show_menu = True
        elif show_menu:
            show_menu = menu_view()
            if not show_menu:
                set_sound.stop()
        else:
            player.loop(FPS)
            fire.loop()
            handle_move(player, objects)
            draw_main(window, background, bg_image, player, objects, offset_x)

            if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                    (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
                offset_x += player.x_vel

    py_game.quit()
    quit()


if __name__ == "__main__":
    main(window)
