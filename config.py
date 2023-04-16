import os


class DevelopmentConfig:
    DEBUG = True
    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_NAME = 'bse'
    DB_USER = 'root'
    DB_PASSWORD = 'root'


class ProductionConfig:
    DEBUG = False
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')


if os.getenv('ENV') == 'production':
    config = ProductionConfig
else:
    config = DevelopmentConfig
