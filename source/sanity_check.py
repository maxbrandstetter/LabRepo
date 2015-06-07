import sys
import os

import logging
import inspect


"""
Methods to exclude from calls
"""
to_exclude = {'__class__', '__delattr__', '__dict__', '__doc__', '__format__',
            '__getattribute__', '__hash__', '__init__', '__module__', '__new__',
            '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
            '__str__', '__subclasshook__', '__weakref__', '_Thread__bootstrap',
            '_Thread__bootstrap_inner', '_Thread__delete', '_Thread__exc_clear',
            '_Thread__exc_info', '_Thread__stop', '_note', '_reset_internal_locks',
            '_set_daemon', '_set_ident', 'getName', 'isAlive', 'isDaemon',
            'is_alive', 'join', 'run', 'setDaemon', 'setName', 'start'}

"""
class_names holds expected class names as a key with its corresponding accepted parameters as a list
"""
class_names = {'FibSeqFinder': [],
               'Interface': [],
               'QA': ['question', 'answer']}

"""
func_names holds expected class names and their corresponding accepted parameters as a list
"""
func_names = {'feet_to_miles': [5280],
              'hal_20': [],
              'get_git_branch': [],
              'get_git_url': [],
              'get_other_users': [],
              'get_fibonacci_seq': [1]}

"""
method_names holds expected method names along with a list of accepted parameters
"""
method_names = {'ask': ['Who invented Python'],
                'teach': [''],
                'correct': [''],
                '_Interface__add_answer': [''],
                'stop': []}


class SanityCheck(object):
    """
    Performs a sanity check on all modules of a given directory.

    :param directory: The directory to check
    :type directory: str
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(handler)

    def __init__(self, directory):
        self.to_check = directory
        sys.path.append(os.path.abspath(self.to_check))
        self.module_list = []
        self.class_list = []

    def import_all_modules(self):
        """
        Imports, or attempts to import, the modules from the given directory

        :return: None
        :rtype: None
        """
        for python_file in os.listdir(self.to_check):
            if python_file.endswith('.py') and '__init__.py' not in python_file:
                curr_module = python_file[:-3]
                try:
                    globals()[curr_module] = __import__(curr_module)
                    self.module_list.append(curr_module)
                    self.logger.info('The following module was successfully imported: ' + curr_module)
                except ImportError as error:
                    self.logger.error('\nError encountered while importing {}'.format(curr_module))
                    self.logger.error(error.message + '\n')

    def create_all_classes(self):
        """
        Creates an instantiation of each class from each module int the given directory

        :return: None
        :rtype: None
        """
        for module in self.module_list:
            for mod_name, obj in inspect.getmembers(sys.modules[module]):
                if inspect.isclass(obj):
                    try:
                        self.class_list.append(obj(*class_names[mod_name]))
                        self.logger.info('The following class was successfully instantiated: ' + mod_name)
                    except Exception as error:
                        self.logger.error('\nError encountered while instantiating ' + mod_name)
                        self.logger.error('Exception: {}'.format(type(error)))
                        self.logger.error(error.message + '\n')

    def call_all_methods(self):
        """
        Calls, or attempts to call, the methods from classes found in the directory

        :return: None
        :rtype: None
        """
        for curr_class in self.class_list:
            for name, obj in inspect.getmembers(curr_class):
                if callable(obj) and name not in to_exclude:
                    try:
                        obj(*method_names[name])
                        self.logger.info('The following method was successfully called: ' + name)
                    except Exception as error:
                        self.logger.error('\nError encountered while calling ' + name + ' from class ' + curr_class.__class__.__name__)
                        self.logger.error('Exception: {}'.format(type(error)))
                        self.logger.error(error.message + '\n')

    def call_all_functions(self):
        """
        Calls, or attempts to call, all module level functions

        :return: None
        :rtype: None
        """
        for module in self.module_list:
            for func, obj in inspect.getmembers(sys.modules[module]):
                if inspect.isfunction(obj):
                    try:
                        obj(*func_names[func])
                        self.logger.info('The following function was successfully called: ' + func)
                    except Exception as error:
                        self.logger.error('\nError encountered while calling ' + func + ' from module ' + module)
                        self.logger.error('Exception: {}'.format(type(error)))
                        self.logger.error(error.message + '\n')


"""
How to utilize the SanityCheck class
"""
if __name__ == '__main__':
    filepath = '.\pyTona'

    test = SanityCheck(directory=filepath)
    test.import_all_modules()
    test.create_all_classes()
    test.call_all_functions()
    test.call_all_methods()
