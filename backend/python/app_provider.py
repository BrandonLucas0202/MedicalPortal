"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

A provider for the BackendApplication instance.
Global instance with singleton pattern.
"""
from flask import Flask
from auth.authenticator import Authenticator
from database.sqlconnection import SQLConnection
import json


class __BackendApplication():

    def __init__(self) -> None:
        self.__flask = Flask(__name__)
        self.__database = SQLConnection(json.load(open("database.json")))
        self.__authenticator = Authenticator(self.__database)


    def getFlask(self) -> Flask:
        """Returns the Flask Application instance."""
        return self.__flask
    
    def getAuthenticator(self) -> Authenticator:
        """Returns the Authenticator instance."""
        return self.__authenticator
    
    def getDatabase(self) -> SQLConnection:
        """Returns the SQL Connection instance."""
        return self.__database



__app: __BackendApplication = None

def app_instance() -> __BackendApplication:
    """
    Provides the Flask Application
    instance, if not created yet,
    will be.
    """
    global __app
    
    if __app is None:
        __app = __BackendApplication()

    return __app
    