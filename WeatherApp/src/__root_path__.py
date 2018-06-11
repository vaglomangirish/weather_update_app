import os


def path():
    """
    Maintain project root path, to be referred and reused in various project modules.
    """
    return os.path.dirname(__file__)