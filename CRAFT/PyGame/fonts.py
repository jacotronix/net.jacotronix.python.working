'''
Created on 8 Jun 2014

@author: Jamie
'''
import os
import pygame
import time
import string

class pitft :
    screen = None;
    
    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print "I'm running under X display = {0}".format(disp_no)

        os.putenv('SDL_FBDEV', '/dev/fb1')
        
        # Select frame buffer driver
        # Make sure that SDL_VIDEODRIVER is set
        driver = 'fbcon'
        if not os.getenv('SDL_VIDEODRIVER'):
            os.putenv('SDL_VIDEODRIVER', driver)
        try:
            pygame.display.init()
        except pygame.error:
            print 'Driver: {0} failed.'.format(driver)
            exit(0)
        
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print "Framebuffer size: %d x %d" % (size[0], size[1])
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))        
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

# create instance of frame buffer screen
mytft = pitft()

# hide the pointer
pygame.mouse.set_visible(False)

# set font size; large enough to see but still get a few lines
fontsize = 20
# set screen origin
text_base_x = 0
text_base_y = 0
# set pixels per text line; depends on font size
text_y_offset = 20
# .. erm, a counter
count = 1
# lines per screen; depends on font size
lines = 12

# loop through the font names
for f in pygame.font.get_fonts():
    
    # get the path to the font name
    fontpath = pygame.font.match_font(f)
    
    #print to local console; I run this over a SSH connection
    print '{:02d}:\t{}\t{}'.format(count, f, fontpath)

    # initialise the font and size
    font = pygame.font.Font(fontpath, fontsize)
    
    # create text to display
    alphabet = "{:02d} abcdefghijklmnopqrstuvwxyz".format(count)
    
    # place text on framebuffer screen
    text_surface = font.render(alphabet, True, (255, 255, 255))  # White text
    mytft.screen.blit(text_surface, (text_base_x, text_base_y))
    
    # move down a line
    text_base_y+=text_y_offset
    
    # if enough lines are on screen
    if ((count%lines) == 0):
        # print a line break on the console; SSH
        print
        # display the text so far on screen
        pygame.display.update()
        # wait 10 seconds
        time.sleep(10)
        # blank the screen
        mytft.screen.fill((0,0,0))
        # reset to top of screen
        text_base_y = 0
    
    # increment the counter
    count+=1

# run out of fonts
# display what's left on screen
pygame.display.update()
# wait 10 seconds
time.sleep(10)
