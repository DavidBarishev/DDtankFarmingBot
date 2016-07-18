"""This module handles Inventory actions 
"""
from time import sleep
import logging

import Clicking

log = logging.getLogger(__name__)


class InventorySections(object):
    """This class used to describe which category of the inventory

    Attributes:
        Equipment (int): First section, player's equipment
        Items (int): Second section, player's items
    """
    Equipment = 0
    Items = 1


def convert(x):
    return {
        0: 'Equipment',
        1: 'Items'
    }[x]


def go_to_inventory(section):
    """Enters inventory which the given section 

    Args:
        section (InventorySections): section to enter

    """
    # Goto inventory
    log.debug('Goint to inventory')
    Clicking.click_in_game_region_point((641, 572))
    sleep(2)
    go_to_section(section=section)


def go_to_section(section):
    """Go to specific section of the inventory
    - Inventory should be open 

    Args:
        section (InventorySections): section to enter

    Raises:
        NotImplementedError: If inventory section isn't part of InventorySections class 
    """
    log.debug('Go to inventory section %s', convert(section))
    if section == InventorySections.Items:
        Clicking.click_in_game_region_point((891, 315))
        sleep(1)
    elif section == InventorySections.Equipment:
        Clicking.click_in_game_region_point((885, 200))
        sleep(1)
    else:
        raise NotImplementedError


def organize_inventory():
    """Organized the inventory, using the in-game button
    - Inventory should be open before the operation  
    """
    log.debug('Organizing the inventory')
    Clicking.move(812, 483)
    sleep(1)
    Clicking.click_in_game_region_point((785, 453))
    sleep(1)
    Clicking.click_in_game_region_point((812, 483))


def exit_inventory():
    """Exists inventory
    - Inventory should be open before the operation  
    """
    log.debug('Exiting inventory')
    Clicking.click_in_game_region_point((909, 43))
