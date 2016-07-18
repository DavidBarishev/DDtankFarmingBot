"""Varise function used to interact with items"""
from time import sleep

import Clicking
import Imging
import Inventory
import Util


class ItemFunctions(object):
    """Function that can be used on items
    Note:
        - Used like an enum

    Attributes:
        Batch_Accept (int): Opens in batch the maximum amount , with rewards
        Batch_Empty (int): Opens in batch the maximum amount , without rewards
        Batch_Empty_Preferred (int): Opens in batch the maximum amount, if the amount is 1, it will do Open_Empty instead
        Open_Accept (int): Open 1 with rewards
        Open_Empty (int): Open 1 without rewards
    """
    Open_Empty = 1
    Open_Accept = 2
    Batch_Empty = 3
    Batch_Accept = 4
    Batch_Empty_Preferred = 5


def locate(img_file):
    """locates item in inventory 

    Args:
        img_file (str): full path to the image

    Returns:
        Tuple: Position of the item (x,y), None if not found
    """
    items = Imging.locate_with_region(
        img_file, region=(982, 342, 331, 321), locate_all=True)
    if len(items) > 1:
        Inventory.organize_inventory()
        return Util.center(Imging.locate_with_region(img_file, region=(982, 342, 331, 321), locate_all=False))
    if len(items) > 0:
        return Util.center(items[0])
    else:
        return None


def run_function_on_item(item_img, function, index_of_function, section=0):
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

    run_function(
        item_img=item_img,
        function=function,
        index_of_function=index_of_function
    )

    Inventory.exit_inventory()
    sleep(1)


def run_function(item_img, function, index_of_function):
    """Runs function on item 

    Note:
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
    x, y = Util.center(pos)
    x, y = x + 982, y + 342
    Clicking.click(x, y)
    sleep(5)

    if function == ItemFunctions.Batch_Empty_Preferred:
        if Imging.locate_with_region(Util.image_path_main('Batch'), region=(982, 342, 407, 389)) is not None:
            function = ItemFunctions.Batch_Accept
            index_of_function = 2
        else:
            function = ItemFunctions.Open_Accept
            index_of_function = 1
    sleep(1)

    click_on_function((x, y), index_of_function)
    sleep(5)

    if function == ItemFunctions.Batch_Empty:
        Clicking.click_in_game_region_point((638, 299))  # Max
        sleep(1)
        Clicking.click_in_game_region_point((409, 356))  # Confirm
        sleep(1)

    if function == ItemFunctions.Open_Accept or function == ItemFunctions.Batch_Accept:
        Clicking.click_in_game_region_point((502, 449))  # Submit

    # TODO add support when no inventory place left
    sleep(2)


def run_function_on_multiple_items(items):
    """Runs function per item , for multiple items 

    Args:
        items (dict): Item dict , that represent the item , and the function to execute on that item.

    Note:
        - The proper form is::
        {
            "item_img": Path to image, (Use Util.image_path_main or Util.image_path_module),
            "function": Items.ItemFunctions, Function to execute,
            "index_of_function": index of function in the context menu,
            "section": Inventory.InventorySections, Section of the inventory the item is in
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

    Note:
        - Internal function 
        - The item should be already clicked once 

    Args:
        pos (tuple): (x,y) the position of the item
        index (int): the index of the function in the context menu

    """
    Clicking.click(pos[0] + 47,
                   pos[1] + (index * 30 + ((index - 1) * 30)) / 2)
