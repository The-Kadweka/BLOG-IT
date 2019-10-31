import os

class Config:
   '''
   General configuration parent class
   '''
   pass
   # simple mde  configurations
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:qwerty12@localhost/moringaz'
   #  email configurations
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
   UPLOADED_PHOTOS_DEST = "app/static/photos"
   SUBJECT_PREFIX = 'FARMERS-HOME'
   SECRET_KEY = os.environ.get('SECRET_KEY')
   SQLALCHEMY_TRACK_MODIFICATIONS=False


class ProdConfig(Config):
   '''
   Production  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   pass
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:qwerty12@localhost/moringaz'
class DevConfig(Config):
   '''
   Development  configuration child class
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:qwerty12@localhost/moringaz'
   DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
