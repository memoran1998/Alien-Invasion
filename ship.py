# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 09:51:46 2023

@author: memor
"""

import pygame

class Ship:
    """A class to mange the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting potition."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #Load the ship imnage and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        