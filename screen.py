from utilities import py_game
from os.path import join
from utilities import WIDTH, HEIGHT, window, play_sound, set_sound


def get_background(name):
    image = py_game.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw_main(window, background, bg_image, player, objects, offset_x):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    player.draw(window, offset_x)

    py_game.display.update()


is_pressed = False


def menu_view():
    global is_pressed
    tiles, image = get_background("Gray.png")
    play = py_game.image.load(
        join("assets", "Menu", "Buttons", "Play.png")).convert_alpha()
    rect = play.get_rect()
    rect.center = (WIDTH // 2, HEIGHT // 2)
    rect.size = (100, 100)

    for tile in tiles:
        window.blit(image, tile)

    window.blit(py_game.transform.scale(play, (100, 100)), rect)

    mouse_buttons = py_game.mouse.get_pressed()
    set_menu_visibility = True

    if mouse_buttons[0] == 1 and rect.collidepoint(py_game.mouse.get_pos()):
        set_sound.play()
        play_sound.stop()
        py_game.time.delay(500)
        is_pressed = True
        set_menu_visibility = False

    elif rect.collidepoint(py_game.mouse.get_pos()) and not is_pressed:
        play_sound.play()

    else:
        py_game.time.delay(50)
        play_sound.fadeout(500)

    if not set_menu_visibility:
        is_pressed = False

    py_game.display.update()

    return set_menu_visibility
