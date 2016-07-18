"""
Name of event : Treasure Map
Location : in the bottom of the screen ,map icon.
Image Recognition Used : True

"""

import logging
from time import sleep

from Framework import Util, Imging, Clicking, UI
from Framework.Logic import FarmAction

TREASURE_MAP_POS = (812, 566)
THROW_POS = (763, 561)


class TreasureMap(FarmAction):
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def is_available(self):
        self.log.debug('Checking for free throws')
        free_throw = free_throws()
        self.log.debug('Free throws found : %r', free_throw)

        return free_throw

    def run(self):
        self.log.debug('Checking for free throws')
        while free_throws():
            self.log.info('Free throw is available - throwing')
            Clicking.click_in_game_region_point(THROW_POS)
            UI.move_mouse_out_of_game_screen()
            sleep(10)
            if complete_quest():
                self.log.info('Landed one quest, exiting')
                break

        sleep(1)
        # TODO add support for beast gem
        # TODO add support for completing level

    def get_to_event(self):
        self.log.debug('Clicking on treasure map')
        Clicking.click_in_game_region_point(TREASURE_MAP_POS)
        UI.move_mouse_out_of_game_screen()
        sleep(6)

    def exit_event(self):
        UI.click_back_button()
        sleep(1)

    def after_run(self):
        pass


def free_throws():
    return Imging.locate_in_game_screen(Util.image_path_module('FreeThrow', 'TreasureMap')) is not None    


def complete_quest():
    return Imging.locate_in_game_screen(Util.image_path_module('CompleteNow', 'TreasureMap')) is None    