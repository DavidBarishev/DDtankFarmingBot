import logging
import time
import os
from datetime import datetime

from importlib import import_module

import Globals
import Util
import Imging
import Logic
import Exceptions
import Capture


def locate_globals():
    # F Gamplay
    """
        Located the global variables for later use
    """
    log.debug("Trying to find F Game Play Position")

    tmp_f = Imging.locate_in_game_screen('Images/Fun.png')

    if tmp_f is None:
        log.critical("Could not find F Gameplay")
        raise Exceptions.GlobalNotFoundException

    else:
        Globals.f_gameplay_pos = Util.center(tmp_f)
        log.debug("Located F Gameplay at : %s", str(Globals.f_gameplay_pos))

    # Event
    tmp_e = Imging.locate_in_game_screen('Images/Event.png')

    if tmp_e is None:
        log.critical("Could not find Event")
        raise Exceptions.GlobalNotFoundException
    else:
        Globals.event_pos = Util.center(tmp_e)
        log.debug("Located Event at : %s", Globals.event_pos)


def import_modules():
    """
    Imports all the modules dynamicly from /Modules and checks form.
    Returns:
        List: List of all imported modules , instantiated
    """
    modules = []
    for module_name in os.listdir('./Modules'):

        if '.py' in module_name:
            continue

        log.info('Importing module : %s', module_name)
        print 'Importing module : %s' % module_name
        try:
            if input('Import this ?'):
                module_imported = import_module('Modules.' + module_name + '.' + module_name)
                modules.append(getattr(module_imported, module_name)())
        except ImportError:
            log.error('Module %s cannot be imported, check the docs for the proper format', module_name)
        except TypeError:
            log.error('Module %s cannot be instantiated, check the docs for the proper format', module_name)
    # TODO Remove this
    '''
    ---------------------------------------------------------------
    '''
    time.sleep(3)
    return modules


def run_modules(modules):
    """
    Run all the farming actions as interface from the imported modules
    Args:
        modules (List): List of all properly imported and instantiate modules

    """
    for module in modules:
        module_name = Util.get_module_name(str(module))
        if not isinstance(module, Logic.FarmAction):
            log.error('%s is not FarmAction instance, check the docs for the proper format', module_name)
        else:
            log.info('Checking availability - %s', module_name)
            if module.is_available():
                log.info('%s is available , executing', module_name)
                time.sleep(1)
                module.run()


def main():
    logging.basicConfig(filename='./Logs/'+datetime.now().strftime('%Y-%m-%d %H-%M-%S')+'.log',
                        filemode='w',
                        format='%(asctime)s,%(msecs)d - %(name)s.%(funcName)s() - %(levelname)s - %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    global log
    log = logging.getLogger(__name__)

    log.info("Starting The Program")

    log.info("Locating Globals")
    try:
        locate_globals()
        run_modules(import_modules())

        log.info('Done')
    except Exceptions.GlobalNotFoundException:
        log.critical("Could not locate one of the globals , exiting")


if __name__ == '__main__':
    time.sleep(5)
    main()
    #Capture.save_game_screen()
