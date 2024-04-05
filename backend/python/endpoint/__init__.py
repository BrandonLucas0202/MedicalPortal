"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Dynamic module package loader.
Automatically imports all modules in the folder.
Modules must end with "_module.py" to be loaded.
"""
from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*_module.py"))

__all__ = [ basename(f)[:-3] for f in modules if isfile(f)]