import logging
from time import sleep

from Framework import Util, Imging, Clicking
from Framework.Logic import FarmAction

TREASURE_MAP_POS = (812, 566)
THROW_POS = (763, 561)
PATH = 'Modules/TreasureMap/Images/'


class TreasureMap(FarmAction):
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def is_available(self):
        # Enter the menu
        self.log.debug('Clicking on treasure map')
        Clicking.click_in_game_region_point(TREASURE_MAP_POS)
        sleep(1)

        self.log.debug('Checking for free throws')
        free_throw = free_throws()
        self.log.debug('Free throws found : %r', free_throw)

        Util.click_back_button()
        sleep(1)
        return free_throw

    def run(self):
        # Enter the menu
        self.log.debug('Clicking on treasure map')
        Clicking.click_in_game_region_point(TREASURE_MAP_POS)

        self.log.debug('Checking for free throws')
        while free_throws():
            self.log.info('Free throw is available - throwing')
            sleep(6)
            Clicking.click_in_game_region_point(THROW_POS)

        sleep(1)
        Util.click_back_button()
        # TODO add support for quests
        # TODO add support for completing level


def free_throws():
    return Imging.locate_in_game_screen(PATH + 'FreeThrow.png') is not None
