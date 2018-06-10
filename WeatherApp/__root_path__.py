"""
Class to maintain project root path, to be referred and reused in various project modules.
"""
import os


def path():
    return os.path.dirname(__file__)