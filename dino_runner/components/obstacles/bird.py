
import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, images):
        self.type = random.randint(0, 1)
        super().__init__(images, self.type)

        self.rect.y = random.randint(200,300)
        
    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 1

        if self.step_index >= 10: 
            self.step_index = 0 
        
   


        
           

        