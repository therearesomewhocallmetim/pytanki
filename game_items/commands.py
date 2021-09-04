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
            item.clear()
            for k, v in previous_state.items():
                item[k] = v
            raise
    return fn


def move(item: GameItem):
    new_coords = []
    for coord, velocity in zip(item['coordinates'], item['velocities']):
        new_coords.append(coord + velocity)
    item['coordinates'] = new_coords


def make_movable(
        item: GameItem,
        coordinates: Coordinates = None, velocities: Velocities = None):
    if not coordinates:
        coordinates = [0.0, 0.0]
    if not velocities:
        velocities = [1.0, 0.0]
    item['coordinates'] = coordinates
    item['velocities'] = velocities


def rotate(item: GameItem):
    item['direction'] = (
            (item['direction'] + item['angular_velocity'])
            % item['max_directions'])


def make_rotatable(
        item: GameItem,
        direction: int = 0, angular_velocity: int = 1, max_directions: int = 4):
    item['direction'] = direction
    item['angular_velocity'] = angular_velocity
    item['max_directions'] = max_directions
