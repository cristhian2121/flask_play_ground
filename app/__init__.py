from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
# Configs
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# Database config
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Login
login = LoginManager(app)
login.login_view = 'login' # Redirect to login by defauld

# Logs
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

# Get router module
from app import routes, models, errors