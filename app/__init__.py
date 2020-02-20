# from flask import Flask
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from config import Config
# from flask_mail import Mail
# from flask_mail import Message
#
# app = Flask(__name__)
# app.config.from_object(Config)
#
# # app.config['MAIL SERVER'] = 'localhost'
# # app.config['MAIL_PORT'] = 2525
#
from flask_mail import Mail

# mail = Mail(app)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# app.debug = True
#
# from app import routes, models

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('/home/yash_gaur/HUPROJECTS/microblog/config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app


app = create_app(config_name="testing")

app.debug = True
db = SQLAlchemy(app)
db.init_app(app)
mail = Mail(app)
migrate = Migrate(app, db)
from app import routes, models