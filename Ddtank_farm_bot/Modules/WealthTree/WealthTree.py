import logging
import time

from Framework import Util, Imging, Clicking, Items, UI
from Framework.Logic import FarmAction

MODULE_NAME = 'WealthTree'
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
        self.wealth_tree_pos = Imging.locate_in_game_screen(Util.image_path_module('Tree',MODULE_NAME))

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
        return
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

    def get_to_event(self):
        self.log.debug("Clicking on F Gameplay")
        UI.click_f_gamplay()
        time.sleep(1)

    def exit_event(self):
        UI.click_exit_button()
        time.sleep(3)

    def after_run(self):
        Items.run_function_on_item(
            item_img=Util.image_path_module('LuckyFruit', MODULE_NAME),
            function=Items.ItemFunctions.Batch_Empty_Preferred,
            index_of_function=-1,
        )

