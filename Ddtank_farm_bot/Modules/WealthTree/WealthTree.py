import Clicking
from Logic import FarmAction
import logging
import time
import Imging
import Util

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
        logging.debug("Clicking on F Gameplay")
        Util.click_f_gamplay()
        time.sleep(1)

        # Wealth Tree
        self.log.debug("Trying to find Wealth Tree Position")
        self.wealth_tree_pos = Imging.locate_in_game_screen(PATH + 'Tree.png')

        Util.reset_menus()

        if self.wealth_tree_pos is None:
            self.log.info("Couldn't find wealth tree event , considering it as not live")
            return False
        else:
            self.log.debug("Found Wealth Tree at : %s", str(self.wealth_tree_pos))

        return True

    def run(self):
        self.log.debug("Clicking on F Gameplay")
        Util.click_f_gamplay()
        time.sleep(1)

        self.log.debug("Clicking on Wealth Tree")
        Clicking.click_in_game_region(self.wealth_tree_pos[0], self.wealth_tree_pos[1])
        time.sleep(1)

        self.log.debug("Clicking on Magic Fruit")
        Clicking.click_in_game_region_point(MAGIC_FRUIT)
        time.sleep(0.1)

        self.log.debug("Clicking on Wealth Fruit")
        Clicking.click_in_game_region_point(WEALTH_FRUIT)
        time.sleep(0.1)

        self.log.debug("Clicking on Health Fruit")
        Clicking.click_in_game_region_point(HEALTH_FRUIT)
        time.sleep(0.1)

        self.log.debug("Clicking on Lucky Fruit")
        Clicking.click_in_game_region_point(LUCKY_FRUIT)
        time.sleep(1)

        Util.click_exit_button()

        # TODO Open the fruits

