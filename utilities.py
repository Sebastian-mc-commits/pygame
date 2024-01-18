from os import listdir
from os.path import join, isfile
import pygame as py_game

py_game.init()

py_game.display.set_caption("Platformer")

play_sound = py_game.mixer.Sound(join("assets", "Music", "play.ogg"))
set_sound = py_game.mixer.Sound(join("assets", "Music", "set.ogg"))

WIDTH, HEIGHT = 600, 500
FPS = 60
PLAYER_VEL = 5

window = py_game.display.set_mode((WIDTH, HEIGHT))



def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = py_game.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = py_game.Surface((width, height), py_game.SRCALPHA)
            rect = py_game.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(py_game.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def flip(sprites):
    return [py_game.transform.flip(sprite, True, False) for sprite in sprites]
