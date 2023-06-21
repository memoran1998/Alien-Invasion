# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 12:05:44 2023

@author: memor
"""

class Setting:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialize the game's settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100, 150, 200)
        
        #Ship settings
        self.ship_speed = 1.5