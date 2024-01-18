from utilities import py_game
from os.path import join


def get_block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = py_game.image.load(path).convert_alpha()
    surface = py_game.Surface((size, size), py_game.SRCALPHA, 32)
    rect = py_game.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return py_game.transform.scale2x(surface)


class Object(py_game.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = py_game.Rect(x, y, width, height)
        self.image = py_game.Surface((width, height), py_game.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = py_game.mask.from_surface(self.image)
