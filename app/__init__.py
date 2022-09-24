import os
from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevelopConfig as dCnf

import config

app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopConfig')
app.config.from_object(dCnf)

bootstrap = Bootstrap(app)

from . import views
