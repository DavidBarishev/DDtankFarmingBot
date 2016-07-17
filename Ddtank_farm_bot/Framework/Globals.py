import logging

try:
    import conf
except ImportError:
    from .. import conf

import Imging
import Util

log = logging.getLogger(__name__)

"""Global variables used for the whole app

Attributes:
	event_pos (tuple): Description
	f_gameplay_pos (tuple): Description
	GAME_HEIGHT (int): Game height in pixels
	GAME_WIDTH (int): Game width in pixels
	X_GAME (int): Top left corner of game, x coordinate
	Y_GAME (int): Top left corner of game, y coordinate
	GAME_REGION (tuple): (x,y,width,height) of screen
"""
GAME_WIDTH = 999
GAME_HEIGHT = 599


def initGlobals():
    global GAME_REGION
    x, y = conf.Screen
    GAME_REGION = (x, y, GAME_WIDTH, GAME_HEIGHT)

    global X_GAME
    X_GAME = x

    global Y_GAME
    Y_GAME = y

    # F Gamplay
    global f_gameplay_pos

    log.debug("Trying to find F Game Play Position")

    tmp_f = Imging.locate_in_game_screen('Images/Fun.png')

    if tmp_f is None:
        log.critical("Could not find F Gameplay")
        raise Exceptions.GlobalNotFoundException

    else:
        f_gameplay_pos = Util.center(tmp_f)
        log.debug("Located F Gameplay at : %s", str(f_gameplay_pos))

    # Event
    global event_pos

    tmp_e = Imging.locate_in_game_screen('Images/Event.png')

    if tmp_e is None:
        log.critical("Could not find Event")
        raise Exceptions.GlobalNotFoundException
    else:
        event_pos = Util.center(tmp_e)
        log.debug("Located Event at : %s", event_pos)
