"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

A provider for the Flask Applcation instance.
Global instance with singleton pattern.
"""
from flask import Flask

__app: Flask = None

def instance() -> Flask:
    """
    Provides the Flask Application
    instance, if not created yet,
    will be.
    """
    global __app
    
    if __app is None:
        __app = Flask(__name__)

    return __app
    