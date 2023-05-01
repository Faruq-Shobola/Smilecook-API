from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'super-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    UPLOADED_IMAGES_DEST = 'static/images'
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 10 * 60