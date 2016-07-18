"""Varise function used to interact with items"""
from time import sleep
import logging

import Clicking
import Imging
import Inventory
import Util

log = logging.getLogger(__name__)


class ItemFunctions(object):
    """Function that can be used on items 
    - Used like an enum

    Attributes:
        Batch_Accept (int): Batch open max, with rewards
        Batch_Empty (int): Batch open max, without rewards
        Batch_Empty_Preferred (int): Batch open max, without rewards , if amount is 1 , will do Open_Empty instead
        Open_Accept (int): Open 1 with rewards
        Open_Empty (int): Open 1 without rewards
        Batch_Accept_Preferred (int): Batch open max, with rewards , if amount is 1 , will do Open_Empty instead
    """
    Open_Empty = 1
    Open_Accept = 2
    Batch_Empty = 3
    Batch_Accept = 4
    Batch_Empty_Preferred = 5
    Batch_Accept_Preferred = 6


def convert(x):
    return {
        1: 'Open_Empty',
        2: 'Open_Accept',
        3: 'Batch_Empty',
        4: 'Batch_Accept',
        5: 'Batch_Empty_Preferred',
        6: 'Batch_Accept_Preferred'
    }[x]


def locate(img_file):
    """locates item in inventory 

    Args:
        img_file (str): Description

    Returns:
        Tuple: Position of the item (x,y), None if not found
    """
    img_name = img_file.split('/')[-1]
    log.debug('Trying to locate %s in inventory', img_name)

    items = Imging.locate_with_region(
        img_file, region=(982, 342, 331, 321), locate_all=True)

    if len(items) > 1:
        log.debug('Found multiple instances of the item, organizing to stack them')
        Inventory.organize_inventory()
        return Util.center(Imging.locate_with_region(img_file, region=(982, 342, 331, 321), locate_all=False))

    if len(items) > 0:
        pos = Util.center(items[0])
        log.debug('Found %s at %s', img_name, str(pos))
        return pos
    else:
        log.error('Could not locate %s in inventory', img_name)
        return None


def run_function_on_item(item_img, function, index_of_function, section):
    """Uses function on item

    Args:
        item_img (str): file name of item's image
        function (ItemFunctions): function to execute 
        index_of_function (int): index of function in the item's context menu
        - When using batch_empty_prefered , leave it at -1
        section (InventorySections, optional): Section of inventory the item is at

    """
    Inventory.go_to_inventory(section)
    sleep(1)

    log.debug('Running %s on %s', item_img.split('/')[-1], convert(function))
    run_function(
        item_img=item_img,
        function=function,
        index_of_function=index_of_function
    )

    Inventory.exit_inventory()
    sleep(1)


def run_function(item_img, function, index_of_function):
    """Runs function on item 
    - Inventory should be open
    - Internal function, use run_function_on_item instead 

    Args:
        item_img (str): file name of item's image
        function (ItemFunctions): function to execute 
        index_of_function (int): index of function in the item's context menu
        - When using batch_empty_prefered , leave it at -1

    """
    pos = locate(item_img)
    if pos is None:
        return
    x, y = pos
    x, y = x + 982, y + 342

    log.debug('Clicking on the item')
    Clicking.click(x, y)
    sleep(5)

    if function == ItemFunctions.Batch_Empty_Preferred or function == ItemFunctions.Batch_Accept_Preferred:
        log.debug('Checking if batch available')

        if Imging.locate_with_region(Util.image_path_main('Batch'), region=(982, 342, 407, 389)) is not None:
            log.debug('Batch found, using Batch')
            if function == ItemFunctions.Batch_Empty_Preferred:
                function = ItemFunctions.Batch_Empty
                index_of_function = 2
            else:
                function = ItemFunctions.Batch_Accept
                index_of_function = 2
        else:
            log.debug('Batch not found, using regular open')
            if function == ItemFunctions.Batch_Empty_Preferred:
                function = ItemFunctions.Open_Empty
                index_of_function = 1
            else:
                function = ItemFunctions.Open_Accept
                index_of_function = 1

    log.debug('Clicking the %s icon in context menu', convert(function))
    click_on_function((x, y), index_of_function)
    sleep(5)

    if function == ItemFunctions.Batch_Empty:
        log.debug('Clicking max button')
        Clicking.click_in_game_region_point((638, 299))  # Max
        sleep(1)
        log.debug('Clicking confirm')
        Clicking.click_in_game_region_point((409, 356))  # Confirm
        sleep(1)

    if function == ItemFunctions.Open_Accept or function == ItemFunctions.Batch_Accept:
        log.debug('Clicking accept')
        Clicking.click_in_game_region_point((502, 449))  # Submit

    # TODO add support when no inventory place left
    sleep(2)


def run_function_on_multiple_items(items):
    """Runs function per item , for multiple items 

    Args:
        items (dict): Item dict , that represent the item , and the function.
        The proper form is :
        {
            "item_img": Path to image , (Use Util.image_path_main or Util.image_path_module),
            "function": Items.ItemFunctions.* Function to execute,
            "index_of_function": index of function in the context menu ,
            "section": Inventory.InventorySections.* Section of the inventory the item is in
        }
    """
    current_section = items[0]['section']
    Inventory.go_to_inventory(current_section)
    for item in items:
        if item['section'] != current_section:
            current_section = items['section']
            Inventory.go_to_section(current_section)

        run_function(
            item_img=item['item_img'],
            function=item['function'],
            index_of_function=item['index_of_function']
        )
    Inventory.exit_inventory()
    sleep(1)


def click_on_function(pos, index):
    """Clicks on function when the position of item is known 
    - Internal function 
    - The item should be clicked once 

    Args:
        pos (tuple): (x,y) the position of the item
        index (int): the index of the function in the context menu

    """
    Clicking.click(pos[0] + 47,
                   pos[1] + (index * 30 + ((index - 1) * 30)) / 2)
