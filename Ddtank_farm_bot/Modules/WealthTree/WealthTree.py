import logging
import time

from Framework import Util, Imging, Clicking
from Framework.Logic import FarmAction

PATH = 'Modules/WealthTree/Images/'
MAGIC_FRUIT = (352, 204)
WEALTH_FRUIT = (296, 257)
HEALTH_FRUIT = (391, 306)
LUCKY_FRUIT = (322, 357)


class WealthTree(FarmAction):
    def __init__(self):
        self.wealth_tree_pos = None
        self.log = logging.getLogger(__name__)

    def is_available(self):
        # Wealth Tree
        self.log.debug("Trying to find Wealth Tree Position")
        self.wealth_tree_pos = Imging.locate_in_game_screen(PATH + 'Tree.png')

        if self.wealth_tree_pos is None:
            self.log.info("Couldn't find wealth tree event , considering it as not live")
            Util.reset_menus()
            return False
        else:
            self.log.debug("Found Wealth Tree at : %s", str(self.wealth_tree_pos))
            Clicking.click_in_game_region_point(self.wealth_tree_pos)
            time.sleep(2)

        return True

    def run(self):
        self.log.debug("Clicking on Magic Fruit")
        Clicking.click_in_game_region_point(MAGIC_FRUIT)
        time.sleep(1)

        self.log.debug("Clicking on Wealth Fruit")
        Clicking.click_in_game_region_point(WEALTH_FRUIT)
        time.sleep(1)

        self.log.debug("Clicking on Health Fruit")
        Clicking.click_in_game_region_point(HEALTH_FRUIT)
        time.sleep(1)

        self.log.debug("Clicking on Lucky Fruit")
        Clicking.click_in_game_region_point(LUCKY_FRUIT)
        time.sleep(2)

        # TODO Open the fruits

    def get_to_event(self):
        self.log.debug("Clicking on F Gameplay")
        Util.click_f_gamplay()
        time.sleep(1)

    def exit_event(self):
        Util.click_exit_button()
        time.sleep(3)
