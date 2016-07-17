import logging
from time import sleep
import os

from Framework import Imging
from Framework import Exceptions
from Framework import Util

log = logging.getLogger(__name__)


def quick_start():
    print 'DDtank Farming Bot - QuickStart program'
    print 'Make sure the game is running when the program exceutes'
    print 'You have 5 seconds to switch windows'

    sleep(5)

    config = {}
    for module_name in os.listdir('./Modules'):
        if '.py' in module_name:
            continue
        else:
            config[module_name] = 'True'

    # Game pos
    pos = Imging.locate_on_screen(Util.image_path_main('LockChat'))
    i = 0
    while pos is None and i < 3:
        log.info('Couldnt find game screen , retrying... ')
        pos = Imging.locate_on_screen(Util.image_path_main('LockChat'))
        i += 1
        sleep(0.5)

    if pos is None:
        log.critical('Couldnt find game screen , exiting')
        raise Exceptions.GlobalNotFoundException

    game_point_pos = (pos[0] - 16, pos[1] - 453)

    with open('conf.py', 'w') as outputfile:
        _write_vars_to_file(outputfile, Modules=config)
        _write_vars_to_file(outputfile, Screen=game_point_pos)


def _write_vars_to_file(_f, **vars):
    for (name, val) in vars.items():
        if isinstance(val, dict):
            _f.write("%s = %s\n" % (name, _pprint(val)))
        else:
            _f.write("%s = %s\n" % (name, repr(val)))


def _pprint(dict):
    stra = '{' + '\n'
    for item, value in dict.items():
        stra += '\t"' + str(item) + '": ' + str(value) + ',\n'
    stra = stra[:-2]
    stra += '\n}\n'
    return stra


def main():
    quick_start()

if __name__ == '__main__':
    main()
