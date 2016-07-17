"""This modules is used to capture the screen
"""
#import pyautogui
import time

import Globals

PATH = './Captures/'


def capture_area(area):
    """
    Captures area of the screen

    Args:
        area (Tuple (x,y,width,height)): Area to capture

    Returns:
        Image : Image of the area captured
    """
    img = pyautogui.screenshot(region=area)
    return img


def save_area(area, filename=None):
    """
    Saves area of the screen to file

    Args:
        area (Tuple (x,y,width,height)): Area to capture save
        filename (String): File name to save
    """
    if filename is None:
        filename = ('area_snap_' + str(area).replace('(', ' ').replace(')', ' '))

    save_img(capture_area(area=area), filename)


def get_game_screen():
    """
    Get game screen image

    Returns:
         Image : Image of screen area
    """
    return capture_area(area=Globals.GAME_REGION)


def save_game_screen(filename=('full_snap_' + str(time.time()))):
    """
    Saves game area screen shot to file

    Args:
        filename (String): Name of file to save to
    """
    save_img(get_game_screen(), filename)


def save_img(img, filename):
    """
    Saves image to file

    Args:
        img (Image): Image to save
        filename (String): Image save name
    """
    img.save(PATH + filename + '.png')
