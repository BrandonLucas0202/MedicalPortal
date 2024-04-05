"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal
Entrance to the frontend web server/provider.
"""
from flask import Flask, send_from_directory, send_file

# Initialize the BackendApplication
app = Flask(__name__)


"""
/portal endpoint
"""
# Instead of the URL being "/portal/index.html" we
# can provide its own route so we can just do
# "/portal" to access the index.html
@app.route("/")
def portalHome():
    return send_file("portal/login.html")

# This is required to allow access to other files
# outside of the main HTML. Such as CSS/JS files
# Images, Icons, etc...
@app.route("/<path:path>")
def portalDir(path):
    return send_from_directory("portal", path)
