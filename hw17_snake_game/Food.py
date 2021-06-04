import random
import pygame

class Food():
    def __init__(self, food_color, screen_width, screen_height):
        """Еда"""
        
        self.food_color = food_color
        self.food_size = 10
        self.food_pos = [random.randrange(1, screen_width  / self.food_size) * self.food_size,
                         random.randrange(1, screen_height / self.food_size) * self.food_size]
  
    def draw_food(self, play_surface):
        """Отображение еды"""
        
        pygame.draw.rect(
            play_surface,
            self.food_color,
            pygame.Rect(self.food_pos[0], self.food_pos[1], self.food_size, self.food_size))