"""
Generic functions that are broadly useful in this
or most any programming context
"""
from os import path
import sys



def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    