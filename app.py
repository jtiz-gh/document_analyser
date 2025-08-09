from flask import Flask, send_from_directory, abort
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP = Flask(__name__)

# Serve the main HTML (root and explicit path)
@APP.route("/")
@APP.route("/document_analyzer.html")
def index():
    return send_from_directory(BASE_DIR, "document_analyzer.html")

# Serve images folder
@APP.route("/images/<path:filename>")
def images(filename: str):
    path = os.path.join(BASE_DIR, "images")
    if not os.path.isfile(os.path.join(path, filename)):
        abort(404)
    return send_from_directory(path, filename)

# Serve the saved_resource with proper JS mimetype (no extension)
@APP.route("/document_analyzer_files/saved_resource")
def saved_resource():
    path = os.path.join(BASE_DIR, "document_analyzer_files")
    file_path = os.path.join(path, "saved_resource")
    if not os.path.isfile(file_path):
        abort(404)
    return send_from_directory(path, "saved_resource", mimetype="application/javascript")

# Serve other files from document_analyzer_files folder
@APP.route("/document_analyzer_files/<path:filename>")
def analyzer_files(filename: str):
    path = os.path.join(BASE_DIR, "document_analyzer_files")
    if not os.path.isfile(os.path.join(path, filename)):
        abort(404)
    return send_from_directory(path, filename)

if __name__ == "__main__":
    # Bind to localhost on the default Flask port
    APP.run(host="127.0.0.1", port=5000, debug=True)
