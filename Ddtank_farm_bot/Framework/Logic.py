"""Provides the abstract classes for the program """

from abc import abstractmethod, ABCMeta


class FarmAction(object):
    """
    This abstract class represents the 'farming' actions.
    Each farming module has to inherent from this class.

    Notes:
        -Used like an interface
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self):
        """
        Runs the farming action
        """
        pass

    @abstractmethod
    def is_available(self):
        """
        Can you execute the event

        Returns:
            bool: Can you execute the event
        """
        pass

    @abstractmethod
    def get_to_event(self):
        """
        Get in game to the event screen
        """
        pass

    @abstractmethod
    def exit_event(self):
        """
        Exists the event , back to main yard
        """
        pass

    @abstractmethod
    def after_run(self):
        """
        Runs it after exit_event
        """
        pass
