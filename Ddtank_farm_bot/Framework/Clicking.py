from Framework import Globals
import pyautogui
import logging

log = logging.getLogger(__name__)


def click(x, y):
    """
    Clicks left click one time

    Args:
        x (int): x to click
        y (int): y to click
    """
    log.debug("Clicking at (%d,%d)", x, y)
    pyautogui.click(x, y)


def click_point(point):
    """
    Clicks left click one time

    Args:
        point (Tuple): (x,y) to click
    """
    click(point[0], point[1])


def click_in_game_region(x, y):
    """
    Clicks in game region

    Args:
        x (int): x to click , relative to game region
        y (int): y to click , relative to game region
    """
    click(x + Globals.X_GAME, y + Globals.Y_GAME)


def click_in_game_region_point(point):
    """
    Clicks in game region

    Args:
        point (Tuple): (x,y) to click in
    """
    click_in_game_region(point[0], point[1])





