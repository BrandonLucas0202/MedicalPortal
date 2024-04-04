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

@flask.errorhandler(500)
def handle_error_500(error: Exception):
    return {
        "status": 500,
        "message": str(error)
    }

# Dynamically load enpoint modules
from endpoint import *