from Framework import Items,Inventory
from Util import image_path_main


def run_exp_1():
    Items.run_function_on_item(
        item_img=image_path_main('EXP_1'),
        function=Items.ItemFunctions.Open_Empty,
        index_of_function=1,
    )


exp_1 = {
        "item_img" : image_path_main('EXP_1'),
        "function" : Items.ItemFunctions.Open_Empty,
        "index_of_function" : 1,
        "section" : Inventory.InventorySections.Items
    }
    

def exp_2():
    Items.run_function_on_item(
        item_img=image_path_main('EXP_2'),
        function=Items.ItemFunctions.Open_Empty,
        index_of_function=1,
    )


def exp_3():
    Items.run_function_on_item(
        item_img=image_path_main('EXP_3'),
        function=Items.ItemFunctions.Open_Empty,
        index_of_function=1,
    )


def exp_4():
    Items.run_function_on_item(
        item_img=image_path_main('EXP_4'),
        function=Items.ItemFunctions.Open_Empty,
        index_of_function=1,
    )


def card():
    Items.run_function_on_item(
        item_img=image_path_main('Card'),
        function=Items.ItemFunctions.Open_Empty,
        index_of_function=1,
    )