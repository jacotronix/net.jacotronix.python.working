'''
Created on 17 Nov 2012

@author: Jamie
'''

from datetime import datetime
from time import sleep
from LCDLib import *

# Main program block

# Initialise display
lcd_init()

try:
    while True:
        lcd_byte(LCD_LINE_1, LCD_CMD)
        lcd_string(datetime.now().strftime('%H:%M:%S'))
        lcd_byte(LCD_LINE_2, LCD_CMD)
        lcd_string(datetime.now().strftime('%a %d %b %y'))
        sleep(1)
except KeyboardInterrupt:
    lcd_clear()