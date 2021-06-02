import pygame
import random

class Snake():
    def __init__(self, snake_color):
        # позиция головы змеи и её тела
        self.snake_head_pos = [100, 50]
        
        # начальное тело змеи состоит из трех сегментов
        # голова змеи - первый элемент, хвост - последний
        self.snake_size = 10
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        
        # цвет змеи
        self.snake_color = snake_color
        
        # направление движения змеи (вправо)
        self.direction = "RIGHT"
        
    
    def draw_snake(self, play_surface, surface_color):
        """Отображаем все сегменты змеи"""
        
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(
                play_surface,
                self.snake_color,
                pygame.Rect(pos[0], pos[1], self.snake_size, self.snake_size))
  
    def validate_direction_and_change(self, change_to):
        """Меняем направление движения змеи, если нет противоречия с механикой игры"""
        
        if any((change_to == "RIGHT" and self.direction != "LEFT",
                change_to == "LEFT"  and self.direction != "RIGHT",
                change_to == "UP"    and self.direction != "DOWN",
                change_to == "DOWN"  and self.direction != "UP")):
            self.direction = change_to
    
    def change_head_position(self):
        """Изменяем положение головы змеи"""
        
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += self.snake_size
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= self.snake_size
        elif self.direction == "UP":
            self.snake_head_pos[1] -= self.snake_size
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += self.snake_size

    def snake_body_mechanism(self, score, food_pos, screen_width, screen_height, food_color, colors_food_dict, wall_pos):
    
        # Имитируем движение хвоста змеи,
        self.snake_body.insert(0, list(self.snake_head_pos))
        
        # если съели еду
        if (self.snake_head_pos[0] == food_pos[0] and
            self.snake_head_pos[1] == food_pos[1]):

            food_pos = [random.randrange(1, screen_width  / self.snake_size) * self.snake_size,
                        random.randrange(1, screen_height / self.snake_size) * self.snake_size]

            wall_pos = [random.randrange(1, screen_width / self.snake_size) * self.snake_size,
                    random.randrange(1, screen_height / self.snake_size) * self.snake_size]

            if food_color == 'brown':
                score += 1
            elif food_color == 'black':
                score += 2
            elif food_color == 'red':
                score += 3

            food_color = random.choice(list(colors_food_dict.keys()))
        else:
            # если не нашли еду, то убираем последний сегмент,
            # если этого не сделать, то змея будет постоянно расти
            self.snake_body.pop()
        return score, food_pos, food_color, wall_pos
   
    def check_for_boundaries(self, screen_width, screen_height, wall_pos, wall_height):
        """Проверка, что столкунлись с концами экрана или сами с собой
        (змея закольцевалась)"""
        
        # проверка границ
        if any(( self.snake_head_pos[0] > screen_width - self.snake_size  or self.snake_head_pos[0] < 0,
                 self.snake_head_pos[1] > screen_height - self.snake_size or self.snake_head_pos[1] < 0 )):
            return True

        if(self.snake_head_pos[0] == wall_pos[0] and (self.snake_head_pos[1] >= wall_pos[1] and self.snake_head_pos[1] <= wall_pos[1]+wall_height-10)):
            return True
        
        for block in self.snake_body[1:]:
            # проверяем, что не врезались в хвост
            if (block[0] == self.snake_head_pos[0] and
                block[1] == self.snake_head_pos[1]):
                return True
        
        return False
                