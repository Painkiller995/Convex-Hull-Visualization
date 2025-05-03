"""Jarvis March Algorithm for Convex Hull Visualization"""

import time

import pygame
from point import Point


class JarvisMarch:
    """Jarvis March Algorithm for Convex Hull Visualization"""

    def __init__(self, points, color, screen, convex_hull, yellow, Red, Grey):
        self.points = points
        self.screen = screen
        self.color = color
        self.convex_hull = convex_hull
        self.yellow = yellow
        self.Red = Red
        self.Grey = Grey

    def left_most(self):
        """Find the leftmost point (with lowest x; tie-breaker: highest y) and highlight it."""

        def point_sort_key(p: Point) -> tuple[int, int]:
            return (p.x, -p.y)

        leftmost_point = min(
            self.points,
            key=point_sort_key,
        )

        pygame.draw.circle(
            self.screen,
            self.color,
            (leftmost_point.x, leftmost_point.y),
            10,
        )
        pygame.display.update()

        return self.points.index(leftmost_point)

    def direction(self, a, b, c):
        """Determine the orientation of the triplet (a, b, c).
        Returns:
            0 -> a, b and c are collinear
            1 -> Clockwise
            2 -> Counterclockwise
        """
        orientation = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)

        if orientation == 0:
            return 0
        elif orientation > 0:
            return 1
        else:
            return 2

    def convex(self):
        """Find the convex hull using the Jarvis March algorithm."""
        if len(self.points) < 3:
            return
        current_point = self.left_most()
        hull = []
        a = current_point
        b = 0
        while True:
            hull.append(a)
            b = (a + 1) % len(self.points)

            for i, _ in enumerate(self.points):
                pygame.draw.line(
                    self.screen,
                    self.Grey,
                    (self.points[a].x, self.points[a].y),
                    (self.points[i].x, self.points[i].y),
                    1,
                )
                time.sleep(0.1)
                pygame.display.update()
                if self.direction(self.points[a], self.points[i], self.points[b]) == 2:
                    b = i
            a = b
            if a == current_point:
                break
        for n in hull:
            pygame.draw.circle(
                self.screen, self.Red, (self.points[n].x, self.points[n].y), 10
            )
            pygame.display.update()
            self.convex_hull.append((self.points[n].x, self.points[n].y))
            time.sleep(0.1)
