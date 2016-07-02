def center(area):
    """
    Returns center of area

    Args:
        area (Tuple): (x,y,width,height) rectangle

    Returns:
        Tuple : Center of area
    """
    return ((area[0] + area[0] + area[2]) / 2.0), ((area[1] + area[1] + area[3]) / 2.0)


def get_module_name(str_o):
    return str_o.replace('<', '') \
        .replace('>', '') \
        .replace(' ', '.') \
        .split('.')[1]


def image_path_main(img_name):
    return 'Images/' + img_name + '.png'


def image_path_module(img_name, module_name):
    return 'Modules/' + module_name + '/Images/' + img_name + '.png'
