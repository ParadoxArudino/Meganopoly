from __future__ import annotations
from collections import deque
import pygame
import time

from modules import *

cardLocations = {
    6: (0.0375,0.05),
    4: (0.125,0.1),
    2: (0.2125,0.15),
    1: (0.3,0.2),
    3: (0.3875,0.15),
    5: (0.475,0.1),
    7: (0.5625,0.05),
}

cardTextures = {
    6: pygame.Color(255,0,0),
    4: pygame.Color(0,255,0),
    2: pygame.Color(0,0,255),
    1: pygame.Color(255,255,0),
    3: pygame.Color(255,0,255),
    5: pygame.Color(0,255,255),
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
    def __init__(self,maxFPS):
        
        #init colours
        self.background_colour = (0, 0, 0)
        
        #init window
        self.surface = pygame.display.set_mode((800,600), pygame.RESIZABLE)
        pygame.display.set_caption('Default Layout Test')
        self.exited = False
        self.maxFPS = maxFPS
        self.clock = pygame.time.Clock()

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
        for i in range(7,0,-1):
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

    def run(self):
        self.init_cards()
        while not self.exited:

            self.clock.tick(self.maxFPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
                elif event.type == pygame.VIDEORESIZE:
                    self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    for obj in self.objects:
                        obj.updateSize()
                        obj.updateBox()
                
            self.execute_render()
        pygame.quit()



scene = DefaultLayout(60)
scene.run()