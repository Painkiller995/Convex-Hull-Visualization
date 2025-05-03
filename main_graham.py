"""Convex Hull Visualization using Graham's Scan Algorithm"""

import os
import random
import pygame
from graham_scan import GrahamScan
from point import Point

# === Configuration ===
FPS = 30
POINT_NUMBER = 50
OFFSET = 50
WINDOW_SCALE = 0.75  # 75% of screen size

# Center the Pygame window
os.environ["SDL_VIDEO_CENTERED"] = "1"

# === Pygame Initialization ===
pygame.init()
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
WIDTH = int(SCREEN_WIDTH * WINDOW_SCALE)
HEIGHT = int(SCREEN_HEIGHT * WINDOW_SCALE)
SCREEN_SIZE = (WIDTH, HEIGHT)

win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Convex Hull (Graham's Scan)")
clock = pygame.time.Clock()

# === Colors ===
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
BLUE = (0, 183, 255)
RED = (255, 15, 79)

# === Generate Random Points ===
points = []
for _ in range(POINT_NUMBER):
    x = random.randint(OFFSET, WIDTH - OFFSET)
    y = random.randint(OFFSET, HEIGHT - OFFSET)
    points.append(Point(x, y))

# === Graham's Scan Convex Hull ===
graham = GrahamScan(points, win, RED, WHITE, BLUE)
convex_hull = graham.convex_hull()

# === Draw Final Hull ===
for i in range(len(convex_hull)):
    pygame.draw.line(
        win,
        RED,
        (convex_hull[i - 1].x, convex_hull[i - 1].y),
        (convex_hull[i].x, convex_hull[i].y),
        4,
    )
pygame.display.update()

# === Main Loop ===
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
