"""Global variables used for the whole app

Attributes:
    event_pos (tuple): Description
    f_gameplay_pos (tuple): Description
    GAME_HEIGHT (int): Game height in pixels
    GAME_WIDTH (int): Game width in pixels
    X_GAME (int): Top left corner of game, x coordinate 
    Y_GAME (int): Top left corner of game, y coordinate 
    GAME_REGION (tuple): (x,y,width,height) of screen 
    GameRegionV2 (tuple): ((x,y),(width,height)) of screen 
"""
f_gameplay_pos = None
event_pos = None

X_GAME = -1
Y_GAME = -1

GAME_WIDTH = 999
GAME_HEIGHT = 599

GAME_REGION = (X_GAME, Y_GAME, GAME_WIDTH, GAME_HEIGHT)
GameRegionV2 = ((X_GAME, Y_GAME), (GAME_WIDTH, GAME_HEIGHT))
