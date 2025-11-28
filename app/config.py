import os

class Config:
    PORT = int(os.getenv("PORT", 5000))
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DATABASE = os.getenv("MONGO_DATABASE")
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS")
