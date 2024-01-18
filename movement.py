from utilities import py_game
from collisions import handle_vertical_collision, collide
from utilities import PLAYER_VEL

def handle_move(player, objects):
    keys = py_game.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)

    if keys[py_game.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[py_game.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()