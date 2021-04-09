import pygame
from pygame.sprite import Sprite

class Alien(Sprite):        #When you use sprites, you can group related elements in your game and act on all the grouped elements at once. 
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/jethalal.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):       #To make the alien appear onscreen, we call its blitme() method in update_screen()
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor *
                    self.ai_settings.fleet_direction)      #We track the alien’s exact position with the self.x attribute
        self.rect.x = self.x
            
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
