from game_items.base import GameItem
from game_items.commands import combine_commands, rotate, move

# from game_items.tank import Tank

if __name__ == '__main__':

    t = GameItem()
    print(t)


    t1 = GameItem()
    move(t1)
    rotate(t1)

    rotate_and_move = combine_commands(rotate, move)
    try:
        rotate_and_move(t1)
    except RuntimeError:
        pass

    print(t1)

