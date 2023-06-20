# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 20:06:48 2023

@author: memor

Alien invasion project practice.
"""
import sys
import pygame

from settings import Setting
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """initialize the game, create game resources."""
        pygame.init()
        
        self.settings = Setting()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Allien Invasion")
        
        self.ship = Ship(self)
        
        #set background color
        self.bg_color = (230,230,230)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #Make the most recently drawn screen visible.
            pygame.display.flip()
            
if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()