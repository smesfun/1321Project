import pygame

class Player:
    def __init__(self, size):
        self.rect = pygame.Rect(50, 400, size[0], size[1])
        self.velocity_y = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = -20
            self.is_jumping = True

    def update(self):
        self.velocity_y += 1
        self.rect.y += self.velocity_y

        if self.rect.y >= 400:
            self.rect.y = 400
            self.is_jumping = False

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def check_collision(self, obstacles):
        for obs in obstacles:
            if self.rect.colliderect(obs["rect"]):
                return True
        return False
