from time import sleep

from Framework import Clicking


class InventorySections(object):
    Equipment = 0
    Items = 1


def go_to_inventory(section):
    # Goto inventory
    Clicking.click_in_game_region_point((641, 572))
    sleep(1)
    go_to_section(section=section)


def go_to_section(section):
    if section == InventorySections.Items:
        Clicking.click_in_game_region_point((891, 315))
        sleep(1)
    elif section == InventorySections.Equipment:
        Clicking.click_in_game_region_point((885, 200))
        sleep(1)
    else:
        raise NotImplementedError


def organize_inventory():
    Clicking.move(812, 483)
    sleep(1)
    Clicking.click_in_game_region_point((785, 453))
    sleep(1)
    Clicking.click_in_game_region_point((812, 483))


def exit_inventory():
    Clicking.click_in_game_region_point((909, 43))


