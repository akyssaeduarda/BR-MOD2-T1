import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SMALL_CACTUS_Y_POS, LARGE_CACTUS_Y_POS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
       
        
    def update(self, game): 
        if len(self.obstacles) == 0:
            obst = random.randint(1,3)
            if obst == 1:
                obstacle = Cactus(LARGE_CACTUS, LARGE_CACTUS_Y_POS)
            elif obst == 2:
                obstacle = Cactus(SMALL_CACTUS, SMALL_CACTUS_Y_POS)
            else:
                obstacle = Bird(BIRD) 
            self.obstacles.append(obstacle)  

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
               if not game.player.has_power_up: #se o dino colidir com o obstaculo e  o power up tiver desligado, o dino morre
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
               else:
                   self.obstacles.remove(obstacle) #senao, o obstaculo é removido

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles.clear()