import pygame
import random

class Walls():
    def __init__(self, wall_color, screen_width, screen_height):
        self.wall_color = wall_color
        self.wall_size = 10
        self.wall_height = 60
        self.wall_pos = [random.randrange(1, screen_width / self.wall_size) * self.wall_size,
                         random.randrange(1, screen_height / self.wall_size) * self.wall_size]

    def draw_wall(self, play_surface):
        pygame.draw.rect(play_surface, self.wall_color,
                         pygame.Rect(self.wall_pos[0], self.wall_pos[1], self.wall_size, self.wall_height))