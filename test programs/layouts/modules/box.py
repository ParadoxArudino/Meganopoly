from __future__ import annotations
from typing import Tuple

class Box:
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.width = x2 - x1
        self.height = y2 - y1

    @property
    def top(self) -> float:
        return self.y1

    @property
    def bottom(self) -> float:
        return self.y2

    @property
    def left(self) -> float:
        return self.x1

    @property
    def right(self) -> float:
        return self.x2

    def center(self) -> Tuple[float, float]:
        """Calculates the coordinates of the center of the box"""
        center_x = self.left + self.width / 2
        center_y = self.top + self.height / 2

        return (center_x, center_y)

    def is_inside(self, outer_box: Box, allowed_margin=0.0) -> bool:
        is_within_x = (
            outer_box.left - self.left <= allowed_margin
            and self.right - outer_box.right <= allowed_margin
        )

        is_within_y = (
            outer_box.top - self.top <= allowed_margin
            and self.bottom - outer_box.bottom <= allowed_margin
        )

        return is_within_x and is_within_y

    def intersects_with_point(self, coordinates: Tuple[float, float]):
        other_x, other_y = coordinates
        is_within_x = self.x1 <= other_x <= self.x2
        is_within_y = self.y1 <= other_y <= self.y2
        return is_within_x and is_within_y

    def is_outside(self, other_box: Box) -> bool:
        is_outside_x = self.right < other_box.left or self.left > other_box.right

        is_outside_y = self.bottom < other_box.top or self.top > other_box.bottom

        return is_outside_x or is_outside_y