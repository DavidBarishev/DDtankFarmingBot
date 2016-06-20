import logging
from time import sleep

import Util
from Ddtank_farm_bot import Imging
import Clicking
from Logic import FarmAction


EXPLORE_POS = (577, 542)
RIGHT = (958, 534)
FARM_POS = (680, 190)
TREASURE_POS = (34, 133)
BACK_POS = (959, 566)
PATH = 'Modules/TreasureFarm/Images/'
TILES = [(492, 186),(579, 233),(428, 238)]


class TreasureFarm(FarmAction):
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def is_available(self):
        return True
        walk_to_farm(self.log)

        self.log.debug('Checking amount of times left to seek treasure ')
        is_left = Imging.locate_in_game_screen(PATH + 'Explore.png')
        self.log.debug('Treasure available to seek : %s', is_left is not None)
        sleep(1)

        exit_farm(self.log)

        return is_left is not None

    def run(self):

        walk_to_farm(self.log)

        self.log.debug('Checking amount of times left to seek treasure ')
        stars = Imging.locate_in_game_screen(PATH + 'Smiley.png', locate_all=True)
        stars = list(stars)
        self.log.info('Treasure available to seek : %d times', len(stars))

        self.log.debug('Staring exploring')
        Clicking.click_in_game_region_point(EXPLORE_POS)
        sleep(3)

        for i, star in enumerate(stars):
            self.log.info('Exploring Tile')
            Clicking.click_in_game_region_point(TILES[i])
            sleep(5.5)

        exit_farm(self.log)


def walk_to_farm(log):
    # Get to the farm
        log.debug('Moving Right')
        for i in xrange(3):
            Clicking.click_in_game_region_point(RIGHT)
            sleep(3)

        log.debug('Entering Farm')
        Clicking.click_in_game_region_point(FARM_POS)
        sleep(3)

        log.debug('Entering farm treasure')
        Clicking.click_in_game_region_point(TREASURE_POS)
        sleep(3)


def exit_farm(log):
    log.debug('Exiting')
    Util.click_back_button()
    sleep(2)

    log.debug('Clicking door')
    Clicking.click_in_game_region_point(BACK_POS)
    sleep(2)

if __name__ == '__main__':
    sleep(5)
    TreasureFarm().is_available()
