import pygame

def load_sounds():
    jump_sound = pygame.mixer.Sound("jump.mp3")
    game_over_sound = pygame.mixer.Sound("gameover.mp3")
    return jump_sound, game_over_sound
