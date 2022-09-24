from sqlalchemy import create_engine, MetaData, Table
from app import app
from config import DevelopConfig as dCnf


engine = create_engine(dCnf.DB, convert_unicode=True)
metadata = MetaData(bind=engine)
users = Table('users', metadata, autoload=True)


def add_user(user):
    cnn = engine.connect()
    cnn.execute(users.insert(), login=user.login.data, email=user.email.data, password=user.password.data)
    cnn.close()


def check_login(user):
    cnn = engine.connect()
    r = cnn.execute(users.select(users.c.login == user.login.data)).first()
    cnn.close()
    if r:
        return False
    return True


def select_user(filter=None):
    cnn = engine.connect()
    if filter is None:
        r = cnn.execute(users.select()).fetchall()
    else:
        r = cnn.execute(users.select(users.c.login == 'admin'))
    cnn.close()
    return r



