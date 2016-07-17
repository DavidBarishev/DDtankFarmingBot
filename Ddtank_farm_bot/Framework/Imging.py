"""This module handles Imaging related function used to find images on screen"""

import pyautogui

import Capture
import Globals


def locate(needle, haystack, locate_all=False, grayscale=False):
    """
    Locates one image in another

    Args:
        locate_all (Optional[bool]): Locate All ?
        needle (Image): The image to find
        haystack (Image): The image to search in
        grayscale (Optional[bool]): Use grayscale in matching

    Returns:
        Tuple: if found (x, y, width, height) of matching region , otherwise None
    """
    if locate_all:
        return list(pyautogui.locateAll(needle, haystack, grayscale=grayscale))
    else:
        return pyautogui.locate(needle, haystack, grayscale=grayscale)


def locate_on_screen(needle, locate_all=False, grayscale=False):
    """
    Locate image on the screen

    Args:
        needle (Image): The image to find
        grayscale (Optional[bool]): Use grayscale in matching
        locate_all (Optional[bool]): Locate All ?

    Returns:
        Tuple: if found (x, y, width, height) of matching region , otherwise None
    """
    if locate_all:
        return pyautogui.locateAllOnScreen(needle, grayscale=grayscale)
    else:
        return pyautogui.locateOnScreen(needle, grayscale=grayscale)


def locate_with_region(needle, region, locate_all=False, grayscale=False):
    """
    Locate image on the screen with a region

    Args:
        needle (Image): The image to find
        region (Tuple): (x, y, width, height) of the region to match in
        grayscale (Optional[bool]): Use grayscale in matching
        locate_all (Optional[bool]): Locate All ?

    Returns:
        Tuple: if found (x, y, width, height) of matching region , otherwise None
    """
    return locate(needle, Capture.capture_area(area=region), grayscale=grayscale, locate_all=locate_all)


def locate_in_game_screen(needle, locate_all=False, grayscale=False):
    """
    Continent wrapper to locate with region , locates an image in the game area

    Args:
        needle (Image): The image to find
        locate_all (Optional[bool]): Locate All ?
        grayscale (Optional[bool]): Use grayscale in matching
    Returns:
        Tuple: if found (x, y, width, height) of matching region , otherwise None

    """
    return locate_with_region(needle=needle, region=Globals.GAME_REGION, locate_all=locate_all, grayscale=grayscale)
