"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Entrance to the backend API server.
"""
from app_provider import app_instance

# Initialize the BackendApplication
app = app_instance()
flask = app.getFlask()

# Dynamically load enpoint modules
from endpoint import *
