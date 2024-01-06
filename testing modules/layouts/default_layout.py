from __future__ import annotations
from collections import deque
import pygame
import time

from modules import *

cardLocations = {
    1: (0.0375,0.05),
    2: (0.125,0.1),
    3: (0.225,0.15),
    4: (0.3375,0.2),
    5: (0.45,0.15),
    6: (0.55,0.1),
    7: (0.6375,0.05),
}

cardTextures = {
    1: pygame.Color(255,0,0),
    2: pygame.Color(0,255,0),
    3: pygame.Color(0,0,255),
    4: pygame.Color(255,255,0),
    5: pygame.Color(255,0,255),
    6: pygame.Color(0,255,255),
    7: pygame.Color(255,255,255),
}

#class objects:



class card:
    def __init__(self, position: int, cardID, window: DefaultLayout):
        self.position = position
        self.cardID = cardID
        self.window = window
        self.size = ((self.window.width()*0.125),(self.window.height()*0.3))
        self.box = Box(0,0,0,0)

        self.updateBox()

    def updateSize(self):
        self.size = ((self.window.width()*0.125),(self.window.height()*0.3))
    
    def updateBox(self):
        x1 = int(self.window.width()*cardLocations[self.position][0])
        y1 = int(self.window.height()*cardLocations[self.position][1])
        x2 = int(self.size[0])
        y2 = int(self.size[1])
        print(x2-x1,y2-y1)
        self.box = pygame.Rect(x1,y1,x2,y2)
    
    def render(self):
        pygame.draw.rect(self.window.surface, cardTextures[self.cardID], self.box)
    

                 
class DefaultLayout:
    def __init__(self):
        
        #init colours
        self.background_colour = (0, 0, 0)
        
        #init window
        self.surface = pygame.display.set_mode((800,600), pygame.RESIZABLE)
        pygame.display.set_caption('Default Layout Test')

        #init objects
        self.objects: list[card] = [] #List of mage gamemode game objects

    #Window properties
    def width(self) -> int:
        return self.surface.get_width()
    def height(self) -> int:
        return self.surface.get_height()
    def box(self) -> Box:
        return self.surface.get_rect()
    def surface(self) -> pygame.Surface:
        return self.surface

    def init_cards(self):
        for i in range(1,8):
            self.objects.append(card(i,i,self))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.exited = True

    def execute_render(self):
        #Draws all game objects to the screen. Called once per frame
        self.surface.fill(self.background_colour)
        
        for obj in self.objects:
            obj.render()
        pygame.display.flip()

        time.sleep(10)
    

    


scene = DefaultLayout()
scene.init_cards()
scene.execute_render()