import pygame
import sys
import random
import time

class Game():
    def __init__(self):
        
        pygame.init()
        
        # размеры экрана
        self.screen_width = 720
        self.screen_height = 460

        # необходимые цвета
        self.colors_dict = {
            'red'   :pygame.Color(255, 0, 0),
            'green' :pygame.Color(0, 255, 0),
            'black' :pygame.Color(0, 0, 0),
            'white' :pygame.Color(255, 255, 255),
            'brown' :pygame.Color(165, 42, 42)
        }

        # количество кадров в секунду
        self.fps_controller = pygame.time.Clock()

        # переменная для оторбражения результата
        # (сколько еды съели)
        self.score = 0

        self.set_surface_and_title()
 
    def set_surface_and_title(self):
        """Задаем игровое поле + заголовок окна"""              
        
        self.play_surface = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake Game')
 
    def refresh_screen(self):
        """обновляем экран и задаем фпс"""
               
        pygame.display.flip()
        self.fps_controller.tick(10)
   
    def show_score(self, choice=1):
        """Отображение результата"""

        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render('Score: {0}'.format(self.score), True, self.colors_dict['black'])
        s_rect = s_surf.get_rect()
        # дефолтный случай отображаем результат слева сверху
        if choice == 1:
            s_rect.midtop = (80, 10)
        # при game_overe отображаем результат по центру
        # под надписью game over
        else:
            s_rect.midtop = (360, 120)
        # рисуем прямоугольник поверх surface
        self.play_surface.blit(s_surf, s_rect)

    def event_loop(self, change_to):
        """Функция для отслеживания нажатий клавиш игроком"""

        for event in pygame.event.get():
            # если нажали клавишу
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT  or event.key == ord('d'):
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = "LEFT"
                elif event.key == pygame.K_UP   or event.key == ord('w'):
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = "DOWN"
                # нажали escape
                elif event.key == pygame.K_ESCAPE:
                    Game.exit_()
            # закрыли окно
            if event.type == pygame.QUIT:
                Game.exit_()
        return change_to
       
    def game_over(self):
        """Функция для вывода надписи Game Over и результатов
            в случае завершения игры и выход из игры
        """
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Game over', True, self.colors_dict['red'])
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.play_surface.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        
        time.sleep(3)
        Game.exit_()

    @staticmethod
    def exit_():
        pygame.quit()
        sys.exit()
