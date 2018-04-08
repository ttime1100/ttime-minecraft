#Import the pygame module
#System module for exiting window we create
import pygame, sys

#import some useful constants
from pygame.locals import *

#Initilize som pygame module
pygame.init()

#Game dimension in constants and will be passed to display
tilesize = 40
mapwidth = 3
mapheight = 5


#Create new drawing surface -- Good for regular game
#displaySurf = pygame.display.set_mode((300,300)) #width,height

#New with game dimension properties
#Needed for correct tile disturbution
displaySurf = pygame.display.set_mode((mapwidth*tilesize,mapheight*tilesize))

#give window a caption
pygame.display.set_caption('T-Time MineCraft')

#constants for resources
dirt = 0
grass = 1
water = 2
coal = 3

#Color constants for resources
black = (0, 0, 0)
brown = (153, 76, 0)
green = (0,255, 0)
blue = (0, 0, 255)

#A dictionary(key term) linking the constants resources
colours = {
            dirt: brown,
            grass: green,
            water: blue,
            coal: black
         }

#list representing tile map for game enviornment
#tilemap = [[1,3,0],[2,2,1],[3,1,2],[0,2,3],[1,2,0]]
#uses 2-dimensional arrays(5 rows)


#New and improved tile map with constants
tilemap = [
            [grass, coal, dirt],
            [water, water, grass],
            [coal, grass, water],
            [dirt, grass, coal],
            [grass, water, dirt]

          ]



#Game Loop (repeat) forever
while True:

    #get all the user events
    for event in pygame.event.get():
        #if user wants to quit game
        if event.type == QUIT:
            #end the game
            pygame.quit()
            sys.exit()

    #loop through each row
    for row in range(mapheight):
        #loop through each column in the row
        for column in range(mapwidth):
            #draw the resource at that position in the tilemap, using correct colour
            pygame.draw.rect(displaySurf,colours[tilemap[row][column]], (column*tilesize,row*tilesize,tilesize,tilesize))


    #Update the display
    pygame.display.update()

    #Draw Ellipse on Screen
    #pygame.draw.ellipse(displaySurf, (0,255,0), (100,50,20,20))
    #three parameters
    #(where to draw, RGB color of Rectangle, Where to draw Coordinates(x,y,width,height))
