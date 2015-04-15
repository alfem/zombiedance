#!/usr/bin/python
# -*- coding: utf8 -*-

# Joystick Tests

import pygame
from pygame.locals import *

JOYSTICK=0

pygame.init()

if pygame.joystick.get_count() > 0:        
  print "Joystick OK!", pygame.joystick.get_count();
  js=pygame.joystick.Joystick(JOYSTICK)
  js.init()
  print "Using joystick:",js.get_name()," with",js.get_numbuttons()," buttons and ",js.get_numaxes()," axes."       

  pygame.event.set_blocked(JOYAXISMOTION)

while True:  
  
  for e in pygame.event.get(): 

    if e.type == JOYBUTTONDOWN:   
      print "JOYSTICK"
      key=e.button
#      for key in range(0,8):    
#        if self.js.get_button(key):
      print "Button pressed", key

    if e.type == KEYDOWN:   
      print "KEY"
      if e.key == pygame.K_SPACE:
        break


