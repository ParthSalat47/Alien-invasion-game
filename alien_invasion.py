# ~ Alien invasion game - A ship that fires bullets

# ~ Planning your Project

'''
In Alien Invasion, the player controls a ship that appears at
the bottom center of the screen. The player can move the ship
right and left using the arrow keys and shoot bullets using the
spacebar. When the game begins, a fleet of aliens fills the sky
and moves across and down the screen. The player shoots and
destroys the aliens. If the player shoots all the aliens, a new fleet
appears that moves faster than the previous fleet. If any alien hits
the player’s ship or reaches the bottom of the screen, the player
loses a ship. If the player loses three ships, the game ends.
'''

# ~ Creating a Pygame Window and Responding to User Input

#import sys      #for sys.exit()        #used directly in game_functions
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
#from alien import Alien        #not needed coz aliens are made in gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard




def run_game():

    # Initialize pygame, settings, and screen object.
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.init()       # initializes background settings that Pygame needs to work properly.
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship.
    ship = Ship(screen, ai_settings)

    # Make an alien.
    #alien = Alien(ai_settings, screen)
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Make a group to store bullets in.
    bullets = Group()       #(2)
    
    # Set the background color.     #not needed coz done by ai_settings
    #bg_color = (230, 230, 230)      #it's a tuple

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Start the main loop for the game.
    while True:
        
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)       #We update the aliens’ positions after the bullets have been updated, because we’ll soon be checking to see whether any bullets hit any aliens.
           
        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button)

run_game()



'''
- The pygame module contains the functionality needed to make a game. We’ll 
use the sys module to exit the game when the player quits. 
- A surface in Pygame is a part of the screen where you display a game 
element.
- (1) We draw the ship onscreen by calling ship.blitme() after filling the 
background, so the ship appears on top of the background
- (2) If you make a group like this inside the loop, you’ll be creating 
thousands of groups of bullets and your game will probably slow to a crawl. If 
your game freezes up, look carefully at what’s happening in your main while 
loop.
- we’ll use the method sprite.groupcollide() to look for collisions between 
members of two groups.



'''

































