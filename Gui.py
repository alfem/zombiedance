# -*- coding: utf8 -*-

import sys
import pygame
from pygame.locals import *
import Tools
import Zombies

JOYSTICK=0

class Gui:
  '''
  Screen graphics and sounds are embedded in this class
  '''
  def __init__(self,width,height): 
    resolution=width,height

    pygame.init()
    pygame.mouse.set_visible(0)
    pygame.key.set_repeat(10,10)


    self.screen=pygame.display.set_mode(resolution,pygame.FULLSCREEN)
#    self.screen=pygame.display.set_mode(resolution)
  
    self.snd_intro=Tools.load_sound("intro.wav")
    self.snd_hit=Tools.load_sound("hit.wav")
    self.snd_miss=Tools.load_sound("miss.wav")
    self.snd_bite=Tools.load_sound("bite.wav")

    self.fnt_titles = pygame.font.Font("fonts/Ghoulish.ttf", 40)
    self.fnt_score = pygame.font.Font("fonts/Ghoulish.ttf", 80)
    self.fnt_end = pygame.font.Font(None, 50)

    self.intro,rect = Tools.load_image("zombie-dance-intro.png")
    self.ground,rect = Tools.load_image("zombie-dance-ground-01.png")
    self.end,rect = Tools.load_image("zombie-dance-end.png")

    self.step,self.step_rect = Tools.load_image("cell-orange.png",-1)
    
# many zombie types with many states (coming up from the depths)
    self.zombie_types=[]
    for t in range(1):
      self.zombie_types.append([])
      for s in range(4):
        img,rect=Tools.load_image("zombie%i-%i.png" % (t,s),-1)
        self.zombie_types[t].append(img)             
    
    self.scoreboard=pygame.Rect(30,70,100,100)

# JOYSTICK (DANCE MAT) INITIALIZATION
    if pygame.joystick.get_count() > 0:        
       print "Joystick OK!", pygame.joystick.get_count();
       self.js=pygame.joystick.Joystick(JOYSTICK)
       self.js.init()
       print "Using joystick:",self.js.get_name()," with",self.js.get_numbuttons()," buttons and ",self.js.get_numaxes()," axes."       
       pygame.event.set_blocked(JOYAXISMOTION)


# CELLS
# 0  1  2
# 3  4  5
# 6  7  8

# Map por DanceMat
#    self.keymap=(3,7,1,5,6,8,0,2)
# Map for joystick testing
    self.keymap=(7,5,3,1,0,2,6,8)

# SHOW INTRO
  def show_intro(self):

    self.screen.blit(self.intro, (0, 0))
   
    pygame.display.flip()
#    self.snd_intro.play()
    pygame.time.delay(1000)

# SHOW GROUND
  def show_ground(self):

#    self.ground.fill((255,255,255),self.scoreboard)
    self.screen.blit(self.ground, (0, 0))
    self.screen.fill((25,50,25),(20,20,165,700))
    text = self.fnt_titles.render("zombies", 1, (200,0,0))
    self.screen.blit(text, (30,45))
    
    text = self.fnt_titles.render("damage", 1, (200,0,0))
    self.screen.blit(text, (30,340))

    pygame.display.flip()
    pygame.time.delay(1000)

# SHOW SCORE
  def show_score(self,p):

    self.screen.fill((150,150,150),(50,100,100,100))
    text = self.fnt_score.render(str(p.kills), 1, (0,0,0))
    width,height=text.get_size()
    x=100-width/2
    y=150-height/2
    self.screen.blit(text, (x,y))
    
    for n in range(5):  
      self.screen.fill((10,10,10),(50,400+n*50,100,30))
    for n in range(p.lives):  
      self.screen.fill((0,100,0),(50,400+n*50,100,30))

    pygame.display.flip();



# MOVE ZOMBIE UP
  def show_zombie(self,z): 

    self.screen.blit(self.ground,(206+z.x,56+z.y),(206+z.x,56+z.y,210,210))
    self.screen.blit(self.zombie_types[z.type][z.depth],(206+z.x,56+z.y))
    pygame.display.flip()


# KILL ZOMBIE 
  def zombie_killed(self,z): 
    self.snd_hit.play()
    self.screen.blit(self.ground,(206+z.x,56+z.y),(206+z.x,56+z.y,210,210))
    pygame.display.flip()

# ZOMBIE BITES! 
  def zombie_bites(self,z): 
    self.snd_bite.play()
    self.screen.blit(self.ground,(206+z.x,56+z.y),(206+z.x,56+z.y,210,210))
    pygame.display.flip()

 
# MOVE PLAYER
  def move_player(self,p):

# JOYSTICK SECTION

    p.cell=4
    self.screen.blit(self.ground,(200+p.x,50+p.y),(200+p.x,50+p.y,self.step_rect.width,self.step_rect.height))

    for key in range(0,8):    
      if self.js.get_button(key):
        p.cell=self.keymap[key]
        print "Button pressed", key, p.cell
  
    p.move()
  
    self.screen.blit(self.step,(200+p.x,50+p.y))
    pygame.display.flip()

    pygame.event.pump()


# KEYS SECTION
    keys_state=pygame.key.get_pressed()
    if keys_state[K_ESCAPE]:
      sys.exit(0)


# SHOW_END
  def show_end(self,p):

    self.screen.blit(self.end,(0,0))

    text = self.fnt_end.render(unicode("%i ZOMBIES KILLED" % (p.kills),'utf-8'), 1, (250,200, 0))
    width,height=text.get_size()
    x=(self.ground.get_width()-width)/2
    self.screen.blit(text, (x,300))

    text = self.fnt_end.render(unicode("Press SPACEBAR to play again",'utf-8'), 1, (250,200, 0))
    width,height=text.get_size()
    x=(self.ground.get_width()-width)/2
    self.screen.blit(text, (x,550))

    pygame.display.flip()

    pygame.event.clear()

    while 1:
      event=pygame.event.wait()
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          sys.exit(0)
        if event.key == K_SPACE: 
          break               
   
   
