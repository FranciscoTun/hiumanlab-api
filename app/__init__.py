import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask_cors import CORS
from .config import Config
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    allowed_origins = app.config["ALLOWED_ORIGINS"]
    if "," in allowed_origins:
        allowed_origins = [o.strip() for o in allowed_origins.split(",")]
    CORS(app, resources={r"/*": {"origins": allowed_origins}})
    register_routes(app)
    return app
