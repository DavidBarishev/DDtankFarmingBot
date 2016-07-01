import logging
from time import sleep

from Framework import Util, Imging, Clicking
from Framework.Logic import FarmAction


EXPLORE_POS = (577, 542)
RIGHT = (958, 534)
FARM_POS = (500, 190)
TREASURE_POS = (34, 133)
BACK_POS = (959, 566)
PATH = 'Modules/TreasureFarm/Images/'
TILES = [(492, 186), (579, 233), (428, 238)]


class TreasureFarm(FarmAction):
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.stars = None

    def is_available(self):
        self.log.debug('Checking amount of times left to seek treasure ')
        stars = Imging.locate_in_game_screen(PATH + 'Smiley.png', locate_all=True)
        self.log.info('Treasure available to seek : %d times', len(stars))
        self.stars = stars

        return len(self.stars) > 0

    def run(self):
        self.log.debug('Staring exploring')
        Clicking.click_in_game_region_point(EXPLORE_POS)
        sleep(7)

        for i, star in enumerate(self.stars):
            self.log.info('Exploring Tile')
            Clicking.click_in_game_region_point(TILES[i])
            sleep(10)

    def get_to_event(self):
        self.log.debug('Moving Right')
        for i in xrange(3):
            Clicking.click_in_game_region_point(RIGHT)
            sleep(5)

        self.log.debug('Entering Farm')
        Clicking.click_in_game_region_point(FARM_POS)
        sleep(7)

        self.log.debug('Entering farm treasure')
        Clicking.click_in_game_region_point(TREASURE_POS)
        sleep(7)

    def exit_event(self):
        Util.click_back_button()
        sleep(7)

        self.log.debug('Clicking door')
        Clicking.click_in_game_region_point(BACK_POS)
        sleep(7)
