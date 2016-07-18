"""Has presets for common items, use this presets in Items.run_function_on_multiple_items()

Attributes:
    card (dict): Random card item
    exp_1 (dict): Exp pill lv 1
    exp_2 (dict): Exp pill lv 2
    exp_3 (dict): Exp pill lv 3
    exp_4 (dict): Exp pill lv 4
"""
import Items
import Inventory
from Util import image_path_main


exp_1 = {
    "item_img": image_path_main('EXP_1'),
    "function": Items.ItemFunctions.Open_Empty,
    "index_of_function": 1,
    "section": Inventory.InventorySections.Items
}

exp_2 = {
    "item_img": image_path_main('EXP_2'),
    "function": Items.ItemFunctions.Open_Empty,
    "index_of_function": 1,
    "section": Inventory.InventorySections.Items
}

exp_3 = {
    "item_img": image_path_main('EXP_3'),
    "function": Items.ItemFunctions.Open_Empty,
    "index_of_function": 1,
    "section": Inventory.InventorySections.Items
}

exp_4 = {
    "item_img": image_path_main('EXP_4'),
    "function": Items.ItemFunctions.Open_Empty,
    "index_of_function": 1,
    "section": Inventory.InventorySections.Items
}

card = {
    "item_img": image_path_main('Card'),
    "function": Items.ItemFunctions.Batch_Empty_Preferred,
    "index_of_function": 1,
    "section": Inventory.InventorySections.Items
}
