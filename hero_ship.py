"""
Program Name: hero_ship.py

Author: Shrrayash Srinivasan

Purpose: I added the alien ship file and installed a ship class for the ALien Invasion game. This file hands the ship initialization,
movement, drawing, and the firing processors. It also integrates with the TYPE_CHECKING and the Arsenal class.

!!!!THIS IS A TUTORIAL CODE!!!!


Date: November 16, 2025
"""


import pygame
from typing import TYPE_CHECKING
from arsenal import Arsenal 


if TYPE_CHECKING:
     from lab12_ssrinivasan3 import AlienInvasion



class Ship:

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.hero_ship_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.hero_ship_w, self.settings.hero_ship_h)
            )
        
        self.rect = self.image.get_rect()


        if self.settings.ship_side == "left":                 
            self.rect.midleft = self.boundaries.midleft       
        elif self.settings.ship_side == "right":              
            self.rect.midright = self.boundaries.midright    
            self.image = pygame.transform.flip(self.image, True, False)
        

        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y) 
        self.arsenal = arsenal
    

    def update(self):

        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        temp_speed = self.settings.hero_ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed
        
        self.rect.x = self.x

        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed  
            
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed 

        self.rect.y = self.y      

    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)
    
    def fire(self):
        return self.arsenal.fire_bullet()