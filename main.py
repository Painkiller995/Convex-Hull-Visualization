"""Convex Hull Visualization using Jarvis March Algorithm"""

import os
import random
import time

import pygame

from jarvis_march import JarvisMarch
from point import Point

# === Configuration ===
FPS = 30
POINT_NUMBER = 5
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
pygame.display.set_caption("Convex Hull (Gift Wrapper)")
clock = pygame.time.Clock()

# === Colors ===
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GREY = (180, 180, 180)
BLUE = (0, 183, 255)
YELLOW = (255, 230, 0)
RED = (255, 15, 79)
GREEN = (41, 255, 123)

# === Background ===
win.fill(BLACK)

# === Generate Random Points ===
points = []
for _ in range(POINT_NUMBER):
    x = random.randint(OFFSET, WIDTH - OFFSET)
    y = random.randint(OFFSET, HEIGHT - OFFSET)
    point = Point(x, y)
    points.append(point)
    pygame.draw.circle(win, WHITE, (point.x, point.y), 4)
pygame.display.update()

# === Jarvis March Convex Hull ===
convex_hull = []
jarvis = JarvisMarch(points, GREEN, win, convex_hull, YELLOW, RED, GREY)
jarvis.left_most()
jarvis.convex()

# === Draw Hull Lines ===
for i, start in enumerate(convex_hull):
    end = convex_hull[(i + 1) % len(convex_hull)]
    time.sleep(0.5)
    pygame.draw.line(win, BLUE, start, end, 4)
    pygame.display.update()

# === Main Loop ===
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
