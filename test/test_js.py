import pygame
from pygame.locals import *

JOYSTICK=0

pygame.init()

# JOYSTICK (DANCE MAT) INITIALIZATION
if pygame.joystick.get_count() > 0:        
 print "Joystick OK!", pygame.joystick.get_count();
 js=pygame.joystick.Joystick(JOYSTICK)
 js.init()
 print js.get_name()," axis:",js.get_numaxes()," buttons:",js.get_numbuttons()
          
          
while 1:                 

 event=pygame.event.pump() 
 print "Test:  ",

 if js.get_button(7):
  print " Button!"

                                                   