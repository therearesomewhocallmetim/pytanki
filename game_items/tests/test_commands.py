import pytest

from ..base import GameItem
from ..commands import move, rotate, combine_commands, make_movable, make_rotatable


@pytest.fixture
def game_item():
    item = GameItem()
    make_movable(item)
    make_rotatable(item)
    return item


def test_move(game_item):
    move(game_item)
    assert [1.0, 0.0] == game_item['coordinates']
    assert [1.0, 0.0] == game_item['velocities']


@pytest.mark.parametrize('item', [
    GameItem(velocities=[1.0, 0.0]),
    GameItem(coordinates=[1.0, 0.0]),
])
def test_move__immovable(item):
    with pytest.raises(KeyError):
        move(item)


def test_make_movable():
    item = GameItem()
    make_movable(item, coordinates=[12, 5], velocities=[-7, 3])
    assert [12, 5] == item['coordinates']
    assert [-7, 3] == item['velocities']


def test_move_from_point_with_speed():
    item = GameItem()
    make_movable(item, coordinates=[12, 5], velocities=[-7, 3])
    move(item)
    assert [5, 8] == item['coordinates']


def test_make_rotatable():
    item = GameItem()
    make_rotatable(item, direction=1, angular_velocity=2, max_directions=7)
    assert 1 == item['direction']
    assert 2 == item['angular_velocity']
    assert 7 == item['max_directions']


@pytest.mark.parametrize('num_rotations, expected_direction', [
    (1, 1),
    (2, 2),
    (4, 0)
])
def test_rotate(game_item, num_rotations, expected_direction):
    for _ in range(num_rotations):
        rotate(game_item)
    assert expected_direction == game_item['direction']


def test_combine_commands(game_item):
    rotate_and_move = combine_commands(rotate, move)
    rotate_and_move(game_item)
    assert [1.0, 0.0] == game_item['coordinates']
    assert 1 == game_item['direction']


def bad_command(item):
    raise RuntimeError('I am a bad command')


def test_combine_commands__rollback_with_state(game_item):
    move(game_item)
    rotate(game_item)

    rotate_and_bad = combine_commands(rotate, bad_command)
    with pytest.raises(RuntimeError) as exc_info:
        rotate_and_bad(game_item)
    assert ('I am a bad command', ) ==  exc_info.value.args
    assert [1.0, 0.0] == game_item['coordinates']
    assert 1 == game_item['direction']
