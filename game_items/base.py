from typing import Optional

DIMENSIONS = 2

Coordinates = lambda: [0.0, 0.0]
Velocities = lambda: [1.0, 0.0]


class GameItem(dict):
    def get(self, key, default=None) -> Optional:
        if key not in self:
            if callable(default):
                self[key] = default()
            elif default:
                self[key] = default
                return default
            else:
                raise KeyError(key)
        return self[key]
