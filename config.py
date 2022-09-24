import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'


class DevelopConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app_dir, 'app.db')
    DB = 'sqlite:///' + os.path.join(app_dir, 'app.db')


class TestConfig(BaseConfig):
    DEBUG = True


class ProductConfig(BaseConfig):
    DEBUG = False
