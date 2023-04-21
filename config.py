import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://test_u0mr_user:ZyLn19unbYJEQTXm7Zl5yNdtw5vddohR@dpg-ch10rm0rddl13a4m3rpg-a/test_u0mr'

class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')