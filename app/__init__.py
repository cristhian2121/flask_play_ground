from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_babel import Babel
from flask import request
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
# Email
mail = Mail(app)
# Facelift (styles)
bootstrap = Bootstrap(app)
# Babel
babel = Babel(app)

# Blueprints import above to avoid circular dependency
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

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

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    # return 'es' -> default Spanish


# Get router module
from app import routes, models