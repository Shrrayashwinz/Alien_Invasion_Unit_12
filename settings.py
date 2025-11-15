from pathlib import Path
class Settings:

    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        self.alien_ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.alien_ship_w = 40
        self.alien_ship_h = 60
        self.alien_ship_speed = 5

        