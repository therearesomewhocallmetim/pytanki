from copy import deepcopy
from typing import Any

from game_items.base import GameItem, Coordinates, Velocities


def combine_commands(*commands):
    def fn(item: Any):
        previous_state = deepcopy(item)
        try:
            for command in commands:
                command(item)
        except:
            for k, v in previous_state.items():
                item[k] = v
            raise
    return fn


def move(item: GameItem):
    new_coords = []
    for coord, velocity in zip(
            item.get('coordinates', Coordinates),
            item.get('velocities', Velocities)):
        new_coords.append(coord + velocity)
    item['coordinates'] = new_coords


def rotate(item: GameItem):
    item['direction'] = (
            (item.get('direction', int) + item.get('angular_velocity', 1))
            % item.get('max_directions', 4))
