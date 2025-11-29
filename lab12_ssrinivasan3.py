"""
Program Name: Lab12_ssrinivasan3.py

Author: Shrrayash Srinivasan

Purpose: This serves as the main module for the game Alien Invasion. It has all the neccessary functions from the other files to 
ensure the game is operational. 

!!!!THIS IS A TUTORIAL CODE!!!!

Date: November 16, 2025     
"""

import sys
import pygame
from settings import Settings
from game_stats import GameStats
from hero_ship import Ship
from arsenal import Arsenal 
from alien_fleet import AlienFleet
from time import sleep
from button import Button

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.settings.initialize_dynamic_settings()

        self.game_stats = GameStats(self.settings.starting_hero_ship_count)


        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(1.7)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact)
        self.impact_sound.set_volume(0.7)
    
        self.hero_ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        self.play_button = Button(self, "Play")
        self.game_active = False
    
    def run_game(self):
        while self.running:
            self._check_events()
            if self.game_active:
               self.hero_ship.update()
               self.alien_fleet.update_fleet()
               self._check_collisions()
               self._check_events()
            self._update_screen() 
            self.clock.tick(self.settings.FPS)
  
    def _check_collisions(self):
        if self.hero_ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()

        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()


        collisions = self.alien_fleet.check_collisions(self.hero_ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(1000)
        
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()



            sleep(1.5)

    def _check_game_status(self):
        if self.game_stats.hero_ships_left > 0:
            self.game_stats.hero_ships_left -= 1
            self._reset_level()

            print(self.game_stats.hero_ships_left)
        
        else:
          self.game_active = False


    def _reset_level(self):
        self.hero_ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
    
    def restart_game(self):
        self.settings.initialize_dynamic_settings()
        self._reset_level()
        self.hero_ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.hero_ship.draw()
        self.alien_fleet.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)



        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                           
            elif event.type == pygame.MOUSEBUTTONDOWN:
               self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
          self.restart_game()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.hero_ship.moving_left = False

        elif event.key == pygame.K_RIGHT:
            self.hero_ship.moving_right = False 
        
        elif event.key == pygame.K_UP:
            self.hero_ship.moving_up = False 
        
        elif event.key == pygame.K_DOWN:
            self.hero_ship.moving_down = False 


    def _check_keydown_events(self, event):
        if event.key == pygame.K_LEFT:
            self.hero_ship.moving_left = True

        elif event.key == pygame.K_RIGHT:
            self.hero_ship.moving_right = True

        elif event.key == pygame.K_UP:
            self.hero_ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.hero_ship.moving_down = True
        
        
        elif event.key == pygame.K_SPACE:
            if self.hero_ship .fire():
                self.laser_sound.play()

        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion() 
    ai.run_game()