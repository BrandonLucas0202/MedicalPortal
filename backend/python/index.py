"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Entrance to the backend API server.
"""
from flask_provider import instance
# Will dynamically load the entire module folder
from module import *

app = instance()

def main():
    # Would initialize the database connection here
    # and anything else we will need on startup.
    pass


    
if __name__ == "index":
    main()
