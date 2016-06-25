import Imging
import logging
import Clicking
import Globals

log = logging.getLogger(__name__)


def click_exit_button():
    log.debug('Trying to find exit button')
    pos = Imging.locate_in_game_screen('Images/x.png')

    if pos is None:
        logging.error("Could not find x button")

    else:
        logging.debug("Located x button at at : %s", str(pos))
        Clicking.click_in_game_region_point(center(pos))


def center(area):
    """
    Returns center of area

    Args:
        area (Tuple): (x,y,width,height) rectangle

    Returns:
        Tuple : Center of area
    """
    return ((area[0] + area[0] + area[2]) / 2.0), ((area[1] + area[1] + area[3]) / 2.0)


def click_f_gamplay():
    Clicking.click_in_game_region_point(Globals.f_gameplay_pos)


def click_event():
    Clicking.click_in_game_region_point(Globals.event_pos)


def reset_menus():
    Clicking.click_in_game_region_point((5, 5))


def click_back_button():
    log.debug('Trying to locate back button')
    pos = Imging.locate_in_game_screen('Images/BackButton.png')

    if pos is None:
        log.error("Couldn't locate back button")
    else:
        logging.debug("Located back button button at at : %s", str(pos))
        Clicking.click_in_game_region_point(center(pos))


def get_module_name(str_o):
    return str_o.replace('<', '')\
            .replace('>', '')\
            .replace(' ', '.')\
            .split('.')[1]
