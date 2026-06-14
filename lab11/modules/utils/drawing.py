"""
Author: Liz Matthews
"""

import pygame, math, os


# Color definition
EDGE_COLOR =  (200,200,200)
PATH_COLOR =  (50,50,50)
GRID_COLOR = (0,0,0)
VERTEX_COLOR = (150,0,0)
START_COLOR = (0,255,0)
GOAL_COLOR = (0,0,255)
CURRENT_COLOR = (0,100,100)
LOOK_COLOR = (0,100,0)
BACKGROUND = (255,255,255)


COLORS = {"edge" : EDGE_COLOR,
          "path" : PATH_COLOR,
          "grid" : GRID_COLOR,
          "vertex" : VERTEX_COLOR,
          "start" : START_COLOR,
          "goal" : GOAL_COLOR,
          "look" : LOOK_COLOR,
          "background" : BACKGROUND,
          "current" : CURRENT_COLOR}


if not pygame.font.get_init():
   pygame.font.init()


# Drawing sizes
SCALE = 1
VERT_SIZE = 8 * SCALE
EDGE_SIZE = 2 * SCALE
GRID_SIZE = 25 * SCALE
SCREEN_SIZE = (500 * SCALE,300 * SCALE)

FONT = pygame.font.Font(os.path.join("modules", "utils", "PressStart2P.ttf"), 8 * SCALE)

def renderText(surface, text, position):
   textSurf = FONT.render(text, False, COLORS["grid"])
   surface.blit(textSurf, position)

def makeBackground(surface):
   """A simple function to fill a pygame surface with the BACKGROUND color."""
   surface.fill(BACKGROUND)   

def drawVertex(surface, vertexType, position):
   """A simple function to draw a circle at a vertex's position."""
   pygame.draw.circle(surface, COLORS[vertexType], position, VERT_SIZE)
   
def drawEdge(surface, edge, edgeType, directed=True):
   """A simple function to draw an edge. If directed is true then the
       edge is drawn as an arrow."""
       
   pygame.draw.line(surface, COLORS[edgeType],
                    edge.getConnectedFrom().coords,
                    edge.getConnectedTo().coords,
                    EDGE_SIZE)
   
   if directed:
      drawArrowPoint(surface, COLORS[edgeType], edge.getConnectedFrom().coords, edge.getConnectedTo().coords)
   
def drawArrowPoint(surface, color, start, end):
   """Draws an arrow point at the end, angled to have come from the start"""
   
   diffX = end[0] - start[0]
   diffY = end[1] - start[1]
   size = math.sqrt(math.pow(diffX, 2) + math.pow(diffY, 2))
   slopeX = diffX / size
   slopeY = diffY / size
   moveBack = VERT_SIZE * 1.75
   
   newEnd = [int(end[0] - moveBack * slopeX), int(end[1] - moveBack * slopeY)]
   pygame.draw.line(surface, color, start, newEnd, EDGE_SIZE)
   
   
   
   rotation = math.degrees(math.atan2(start[1]-newEnd[1], newEnd[0]-start[0]))+90
   pygame.draw.polygon(surface, color, ((newEnd[0]+EDGE_SIZE * 3 *math.sin(math.radians(rotation)),
                                                    newEnd[1]+EDGE_SIZE * 3 *math.cos(math.radians(rotation))),
                                                   (newEnd[0]+EDGE_SIZE * 3 *math.sin(math.radians(rotation-120)),
                                                    newEnd[1]+EDGE_SIZE * 3 *math.cos(math.radians(rotation-120))),
                                                   (newEnd[0]+EDGE_SIZE * 3 *math.sin(math.radians(rotation+120)),
                                                    newEnd[1]+EDGE_SIZE * 3 *math.cos(math.radians(rotation+120)))))
        
        