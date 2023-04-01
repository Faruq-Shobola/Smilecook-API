from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False