import pygame
import random
from Game import Game
from Food import Food
from Snake import Snake
from Walls import Walls

game = Game()
snake = Snake(game.colors_dict['purple'])
food = Food(game.colors_dict[random.choice(list(['red', 'black', 'brown']))], game.screen_width, game.screen_height)
wall = Walls(game.colors_dict['green'], game.screen_width, game.screen_height)
   
change_to = snake.direction
while True:      
    change_to = game.event_loop(change_to)

    snake.validate_direction_and_change(change_to)
    snake.change_head_position()
    game.score, food.food_pos, food.food_color, wall.wall_pos = snake.snake_body_mechanism(game.score, food.food_pos, game.screen_width, game.screen_height, food.food_color, game.colors_dict, wall.wall_pos)
    
    snake.draw_snake(game.play_surface, game.colors_dict, game.level)
    food.draw_food(game.play_surface)
    wall.draw_wall(game.play_surface)

    if snake.check_for_boundaries(game.screen_width, game.screen_height, wall.wall_pos, wall.wall_height):
        game.game_over()

    game.check_score()
    game.show_score(game.level)
    game.refresh_screen()
