import pytest

from game_items.base import GameItem


@pytest.mark.parametrize(    'default, expected', [
    (1, 1),
    (int, 0),
    (list, []),
    (lambda: 3, 3)
])
def test_game_item__w_default(default, expected):
    item = GameItem()
    value = item.get('some_key', default)
    assert expected == value

def test_game_item__empty_no_default():
    item = GameItem()
    with pytest.raises(KeyError) as exc_info:
        item.get('some_key')
    assert exc_info.value.args == ('some_key', )

def test_game_item__nonempty_no_default():
    item = GameItem(some_key='value')
    assert 'value' == item['some_key']

