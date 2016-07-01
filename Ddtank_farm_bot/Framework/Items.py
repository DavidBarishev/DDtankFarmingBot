from time import sleep

from Framework import Clicking
from Framework import Imging
from Framework import Inventory
from Framework import Util


class ItemFunctions(object):
    Open_Empty = 1
    Open_Accept = 2
    Batch_Empty = 3
    Batch_Accept = 4
    Batch_Empty_Preferred = 5
    Move = 6


def locate(img_file):
        items = Imging.locate_with_region(img_file, region=(982, 342, 331, 321), locate_all=True)
        if len(items) > 1:
            Inventory.organize_inventory()
            return Imging.locate_with_region(img_file, region=(982, 342, 331, 321), locate_all=False)
        if len(items) > 0:
            return items[0]
        else:
            return None


def run_function_on_item(item_img, function, index_of_function, section=Inventory.InventorySections.Items):
    Inventory.go_to_inventory(section)
    pos = locate(item_img)
    if pos is None:
        return
    x, y = Util.center(pos)
    x, y = x + 982, y+342
    Clicking.click(x, y)
    sleep(5)

    if function == ItemFunctions.Batch_Empty_Preferred:
        if Imging.locate_with_region(Util.image_path('Batch'), region=(982, 342, 407, 389)) is not None:
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


def click_on_function(pos, index):
    Clicking.click(pos[0] + 47,
                   pos[1] + (index * 30 + ((index - 1) * 30))/2)


