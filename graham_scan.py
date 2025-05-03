"""Graham's Scan Algorithm for Convex Hull Visualization"""

import pygame
import random
import time
from point import Point


class GrahamScan:
    """Graham's Scan Algorithm for Convex Hull Visualization"""

    def __init__(self, points, screen, hull_color, point_color, line_color):
        self.points = points
        self.screen = screen
        self.hull_color = hull_color
        self.point_color = point_color
        self.line_color = line_color

    def orientation(self, p, q, r):
        """Determine the orientation of the triplet (p, q, r).
        Returns:
            0 -> p, q, and r are collinear
            1 -> Clockwise
            2 -> Counterclockwise
        """
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        return 2 if val > 0 else 1

    def convex_hull(self):
        """Compute the convex hull using Graham's Scan Algorithm."""
        # Step 1: Find the point with the lowest y-coordinate (and leftmost if tie)
        start = min(self.points, key=lambda p: (p.y, p.x))
        self.points.remove(start)

        # Step 2: Sort points by polar angle with respect to the start point
        self.points.sort(key=lambda p: (self.polar_angle(start, p), -p.y, p.x))

        # Add the start point back to the beginning
        self.points.insert(0, start)

        # Step 3: Use a stack to determine the convex hull
        hull = [self.points[0], self.points[1]]

        for i in range(2, len(self.points)):
            while (
                len(hull) > 1
                and self.orientation(hull[-2], hull[-1], self.points[i]) != 2
            ):
                hull.pop()
            hull.append(self.points[i])

            # Visualize the current hull
            self.visualize_hull(hull)

        return hull

    def polar_angle(self, p0, p1):
        """Calculate the polar angle between two points."""
        return (p1.x - p0.x) / ((p1.y - p0.y) + 1e-9)

    def visualize_hull(self, hull):
        """Visualize the current state of the convex hull."""
        self.screen.fill((30, 30, 30))  # Clear the screen

        # Draw all points
        for point in self.points:
            pygame.draw.circle(self.screen, self.point_color, (point.x, point.y), 4)

        # Draw the hull
        for i in range(len(hull)):
            pygame.draw.line(
                self.screen,
                self.line_color,
                (hull[i - 1].x, hull[i - 1].y),
                (hull[i].x, hull[i].y),
                2,
            )

        pygame.display.update()
        time.sleep(0.5)
