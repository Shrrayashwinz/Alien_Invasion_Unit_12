"""
Program Name: arsenal.py

Author: Shrrayash Srinivasan

Purpose: Defined the Arsenal class so that it can manage the bullet creating, aswell as the updating and the elimination of
bullets that go offscreen.

Date: November 16, 2025
"""


import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
     from lab12_ssrinivasan3 import AlienInvasion



class Arsenal:
    def __init__(self, game: 'AlienInvasion'):
         self.game = game
         self.settings = game.settings
         self.arsenal = pygame.sprite.Group()
    
    def update_arsenal(self):
         self.arsenal.update()
         self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
         for bullet in self.arsenal.copy():
              if bullet.rect.bottom <= 0:
                   self.arsenal.remove(bullet)
    
    def draw(self):
         for bullet in self.arsenal:
              bullet.draw_bullet()
    
    def fire_bullet(self):
         if len(self.arsenal) < self.settings.bullet_amount:
              new_bullet = Bullet(self.game)
              self.arsenal.add(new_bullet)
              return True
         return False