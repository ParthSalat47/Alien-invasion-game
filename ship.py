import pygame
from pygame.sprite import Sprite        #to make a grp of ships - to show no. of ships left


class Ship(Sprite):
    
    def __init__(self, screen, ai_settings):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx        #(1)
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Update rect object from self.center.
        self.rect.centerx = self.center     #only integer part will be saved
    
    def blitme(self):       #blitme() method, which will draw the image to the
                            #screen at the position specified by self.rect.
        """Draw the ship at its current location."""
    
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx




'''
- When you’re centering a game element, work with the center, centerx, or
centery attributes of a rect. When you’re working at an edge of the screen,
work with the top, bottom, left, or right attributes. When you’re adjusting
the horizontal or vertical placement of the rect, you can just use the x and
y attributes, which are the x- and y-coordinates of its top-left corner.
- In Pygame, the origin (0, 0) is at the top-left corner of the screen, and 
coordinates increase as you go down and to the right. On a 1200 by 800 screen, 
the origin is at the top-left corner, and the bottom-right corner has the 
coordinates (1200, 800)
- (1) first store the screen’s rect in self.screen_rect w, and then make the 
value of self.rect.centerx (the x-coordinate of the ship’s center) match the 
centerx attribute of the screen’s rect
'''

















