#Glowing Rectangles
import pygame
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))
rectList = []
rects = 0

def rectangle():
	rectangle = pygame.Rect((random.randint(0,640), random.randint(0,1320)), (random.randint(4,256), random.randint(4,256)))
	return rectangle


while True:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()
		elif ev.type == pygame.MOUSEBUTTONDOWN:
			rectList.append(rectangle())
			
	rects = len(rectList)
	
	for i in range(0, rects-1):
		screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255), 255), rectList[i])
		
	pygame.display.flip()
	
	
	
	
	
	
	
	
	
	
	
	