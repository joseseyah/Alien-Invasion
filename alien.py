from matplotlib import image
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        super().__init__()
        
        self.image = pygame.image.load(image)