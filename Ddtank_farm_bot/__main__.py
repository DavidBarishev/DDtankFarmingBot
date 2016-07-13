import json
import logging
import os
import time

from datetime import datetime
from importlib import import_module

from Framework import Exceptions
from Framework import Globals
from Framework import Imging
from Framework import Util


from Framework import Items, CommonItems

def locate_globals(config):
    """
        Located the global variables for later use
    """

    Globals.X_GAME = config['Screen']['GamePoint'][0]
    Globals.Y_GAME = config['Screen']['GamePoint'][1]

    Globals.GAME_REGION = (Globals.X_GAME,Globals.Y_GAME,Globals.GAME_WIDTH,Globals.GAME_HEIGHT)

    # F Gamplay
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


def import_modules(config):
    """
    Imports all the modules dynamicly from /Modules and checks form.
    Returns:
        List: List of all imported modules , instantiated
    """
    modules = []
    for module_name in os.listdir('./Modules'):

        if '.py' in module_name:
            continue
        if config['Modules'][module_name] == 'False':
            log.debug('Not importing %s, disabled in the config', module_name)
            continue

        log.info('Importing module : %s', module_name)
        try:
            module_imported = import_module('Modules.' + module_name + '.' + module_name)
            modules.append(getattr(module_imported, module_name)())
        except ImportError:
            log.error('Module %s cannot be imported, check the docs for the proper format', module_name)
        except TypeError:
            log.error('Module %s cannot be instantiated, check the docs for the proper format', module_name)
    return modules


def get_configuration():
    log.debug('Loading Configuration')
    if not os.path.exists('Config.json'):
        log.info('Config file not found - creating one')
        config = {}

        for module_name in os.listdir('./Modules'):
            if '.py' in module_name:
                continue
            else:
                config[module_name] = 'True'

        # Game pos
        pos = None
        i = 0
        while pos is None and i < 4:
            log.info('Couldnt find game screen , retrying... ')
            pos = Imging.locate_on_screen(Util.image_path_main('LockChat'))
            i+= 1

        if pos is None:
            log.critical('Couldnt find game screen , exiting')
            raise Exceptions.GlobalNotFoundException
   
        game_point_pos = (pos[0] - 16,pos[1] - 453) 

        json_f = {
            "Modules":config,
            "Screen":
            {
                "GamePoint":game_point_pos,
            }
        }

        with open('Config.json', 'w') as outputfile:
            json.dump(json_f, outputfile, sort_keys=True, indent=4, ensure_ascii=False)

        return json_f

    else:
        with open('Config.json') as data_file:
            config = json.load(data_file)
            return config


def run_modules(modules):
    """
    Run all the farming actions as interface from the imported modules
    Args:
        modules (List): List of all properly imported and instantiate modules

    """
    for module in modules:
        module_name = Util.get_module_name(str(module))
        # TODO change back to farm action
        if not isinstance(module, object):
            log.error('%s is not FarmAction instance, check the docs for the proper format', module_name)
        else:
            log.debug('Going to event - %s ', module_name)
            module.get_to_event()

            log.info('Checking availability - %s', module_name)
            if module.is_available():
                log.info('%s is available , executing', module_name)
                time.sleep(1)
                module.run()

            log.debug('Existing Event - %s ', module_name)
            module.exit_event()

            log.debug('After run Event - %s ', module_name)
            time.sleep(2)
            module.after_run()


def run_bot():
    log.info("Starting The Program")

    log.info("Locating Globals")
    try:
        config = get_configuration()
        locate_globals(config)
        run_modules(import_modules(config))
        
        log.info('Done')
    except Exceptions.GlobalNotFoundException:
        log.critical("Could not locate one of the globals , exiting")


def make_directories():
    if not os.path.exists('Logs'):
        os.makedirs('Logs')

    if not os.path.exists('Captures'):
        os.makedirs('Captures')


def setup_logger():
    # File
    logging.basicConfig(filename='./Logs/' + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '.log',
                        filemode='w',
                        format='%(asctime)s,%(msecs)d | %(name)s.%(funcName)s() | %(levelname)s | %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    global log
    log = logging.getLogger(__name__)

    # Add logging above info to console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)-8s | %(message)s')
    console.setFormatter(formatter)

    logging.getLogger('').addHandler(console)

if __name__ == '__main__':
    make_directories()
    setup_logger()
    time.sleep(5)
    run_bot()

