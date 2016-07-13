import logging

import pyautogui

from Framework import Imging, Util
from Framework import Globals

log = logging.getLogger(__name__)

def click_exit_button():
    from Framework import Clicking
    log.debug('Trying to find exit button')
    pos = Imging.locate_in_game_screen('Images/x.png')

    if pos is None:
        logging.error("Could not find x button")

    else:
        logging.debug("Located x button at at : %s", str(pos))
        Clicking.click_in_game_region_point(Util.center(pos))


def click_f_gamplay():
    from Framework import Clicking
    Clicking.click_in_game_region_point(Globals.f_gameplay_pos)


def click_event():
    from Framework import Clicking
    Clicking.click_in_game_region_point(Globals.event_pos)


def reset_menus():
    from Framework import Clicking
    Clicking.click_in_game_region_point((5, 5))


def click_back_button():
    from Framework import Clicking
    log.debug('Trying to locate back button')
    pos = Imging.locate_in_game_screen('Images/BackButton.png')

    if pos is None:
        log.error("Couldn't locate back button")
    else:
        logging.debug("Located back button button at at : %s", str(pos))
        Clicking.click_in_game_region_point(Util.center(pos))


def move_mouse_out_of_game_screen():
    pyautogui.moveTo(Globals.X_GAME - 10, Globals.Y_GAME - 10)
