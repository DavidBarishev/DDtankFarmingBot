"""Misc functions"""


def center(area):
    """
    Returns center of area

    Args:
        area (Tuple): (x,y,width,height) rectangle

    Returns:
        Tuple: Center of area
    """
    return ((area[0] + area[0] + area[2]) / 2.0), ((area[1] + area[1] + area[3]) / 2.0)


def image_path_main(img_name):
    """Added path to image name from the main images folder

    Args:
        img_name (str): the image name without .something (.png is used)  

    Returns:
        str: Path with the image name and .png
    """
    return 'Images/' + img_name + '.png'


def image_path_module(img_name, module_name):
    """Added path to image name from the one of the modules images folder

    Args:
        img_name (TYPE): the image name without .something (.png is used)  
        module_name (TYPE): module folder name 

    Returns:
        str: Path with the image name and .png
    """
    return 'Modules/' + module_name + '/Images/' + img_name + '.png'
