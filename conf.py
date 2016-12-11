"""
server configuration files, defined at initialization and available globaly

stuff should be constant here, I don't want any surprises with runtime  constant changes
"""

DEBUG = None  # server debug mode
VERBOSE = None  # print additional commands
FILESTORE = None  # save and load chatrooms into storage

FILE_STORAGE_TYPE = 'JSON'  # speciies the type of storing technology implemented


GLOBALS_DEFINED = False
def setup_globals(debug, verbose, filestore):
    """
    setup the global variables, as constant can only be called successfuly once
    """
    global GLOBALS_DEFINED
    if GLOBALS_DEFINED:
        raise ValueError("global definitions may only be defined once!")
    global DEBUG
    global VERBOSE
    global FILESTORE
    DEBUG = debug
    VERBOSE = verbose
    FILESTORE = filestore

    GLOBALS_DEFINED = True


def v_print(out_str):
    """
    a verbose check print. Easier to type rather than if-ing every time.
    :param out_str: output to be printed
    :return: None
    """
    if VERBOSE:
        print(out_str)


