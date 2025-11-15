import sys
import pygame
from settings import Settings
from alien_ship import Ship
from arsenal import Arsenal 

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()


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
    
        self.alien_ship = Ship(self, Arsenal(self))
    
    def run_game(self):
        while self.running:
            self._check_events()
            self.alien_ship.update()
            self._update_screen() 
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.alien_ship.draw()
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
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.alien_ship.moving_left = False

        elif event.key == pygame.K_RIGHT:
            self.alien_ship.moving_right = False 


    def _check_keydown_events(self, event):
        if event.key == pygame.K_LEFT:
            self.alien_ship.moving_left = True

        elif event.key == pygame.K_RIGHT:
            self.alien_ship.moving_right = True
        
        elif event.key == pygame.K_SPACE:
            if self.alien_ship.fire():
                self.laser_sound.play()

        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion() 
    ai.run_game()