import pygame
import random
import time

pygame.init()

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
yellow=(255,255,0)
green=(0,255,0)
cyan=(0,255,255)
blue=(0,0,255)
magenta=(255,0,255)

size=[600,600]
screen=pygame.display.set_mode(size)
lfont=pygame.font.SysFont('AppleSDGothicB00',20)
sfont=pygame.font.SysFont('AppleSDGothicR00',10)

pygame.display.set_caption("숫자야구 게임")

done=False
clock=pygame.time.Clock()

class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x+width>mouse[0]>x and y+height>mouse[1]>y:
          screen.blit(img_act,(x_act, y_act))
          if click[0] and action!=None:
            time.sleep(1)
            action()
        else:
            screen.blit(img_in,(x,y))

def difficulty():
  diff=True
  while diff:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
  screen.fill(black)

while not done:
