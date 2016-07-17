import logging
import os
import sys
import time

from datetime import datetime
from importlib import import_module

from Framework.Globals import initGlobals


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

        if config[module_name] == 'False':
            log.debug('Not importing %s, disabled in the config', module_name)
            continue

        log.info('Importing module : %s', module_name)
        try:
            module_imported = import_module(
                'Modules.' + module_name + '.' + module_name)
            modules.append(getattr(module_imported, module_name)())
        except ImportError:
            log.error('Module %s cannot be imported, check the docs for the proper format', module_name)
        except TypeError:
            log.error('Module %s cannot be instantiated, check the docs for the proper format', module_name)
    return modules


def get_configuration():
    log.debug('Loading Configuration')
    try:
        import conf
        return conf.Modules

    except (ImportError, AttributeError):
        log.critical('Config file not found or corrupted, please run the quick-start')
        sys.exit(0)


def run_modules(modules):
    """
    Run all the farming actions as interface from the imported modules
    Args:
        modules (List): List of all properly imported and instantiate modules

    """
    for module in modules:
        module_name = _get_module_name(str(module))
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
    initGlobals()
    config = get_configuration()
    run_modules(import_modules(config))

    log.info('Done')


def make_directories():
    if not os.path.exists('Logs'):
        os.makedirs('Logs')

    if not os.path.exists('Captures'):
        os.makedirs('Captures')


def setup_logger():
    # File
    logging.basicConfig(
        filename='./Logs/' + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '.log',
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


def _get_module_name(str_o):
    return str_o.replace('<', '') \
        .replace('>', '') \
        .replace(' ', '.') \
        .split('.')[1]


if __name__ == '__main__':
    make_directories()
    setup_logger()
    time.sleep(5)
    run_bot()
