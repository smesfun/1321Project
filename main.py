import pygame, sys
from Scripts import Player
from Scripts import endGame
from Scripts import obstacleBehavior
from Scripts import accelerateGame
from Scripts import gameSound

pygame.init()

resolution = (800, 600)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("CSE Project")
clock = pygame.time.Clock()

jump_sound, game_over_sound = gameSound.load_sounds()

player = Player.Player((50, 50))
obstacles = obstacleBehavior.initialize_obstacles()


running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.jump()
                jump_sound.play()

    player.update()
    obstacles = obstacleBehavior.update_obstacles(obstacles)
    accelerateGame.increase_difficulty(obstacles)


    if player.check_collision(obstacles):
        endGame.end_game(game_over_sound)
        running = False


    player.draw(screen)
    obstacleBehavior.draw_obstacles(screen, obstacles)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
