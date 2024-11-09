import pygame
import random

def initialize_obstacles():
    obstacles = []
    for i in range(3):
        rect = pygame.Rect(800 + i * 300, 400, 50, 50)
        obstacles.append({"rect": rect, "speed": 5})
    return obstacles

def update_obstacles(obstacles):
    for obs in obstacles:
        obs["rect"].x -= obs["speed"]
        if obs["rect"].x < -50:
            obs["rect"].x = 800
            obs["speed"] = max(obs["speed"], 5)
    return obstacles

def draw_obstacles(screen, obstacles):
    for obs in obstacles:
        pygame.draw.rect(screen, (0, 0, 0), obs["rect"])
