import pygame, sys
import time

def end_game(game_over_sound):
    pygame.time.delay(3000)
    game_over_sound.play()
    pygame.time.delay(int(game_over_sound.get_length() * 1000))
    pygame.quit()
    sys.exit()
