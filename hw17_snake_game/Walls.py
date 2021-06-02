import pygame
import random

class Walls():
    def __init__(self, wall_color, screen_width, screen_height):
        self.wall_color = wall_color
        self.wall_width = 10
        self.wall_height = 100
        self.wall_pos = [random.randrange(1, screen_width / self.wall_width) * self.wall_width,
                         random.randrange(1, screen_height / self.wall_width) * self.wall_width]

    def draw_wall(self, play_surface):
        pygame.draw.rect(play_surface, self.wall_color,
                         pygame.Rect(self.wall_pos[0], self.wall_pos[1], self.wall_width, self.wall_height))