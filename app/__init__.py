from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
app.config.from_object(Config)

# app.config['MAIL SERVER'] = 'localhost'
# app.config['MAIL_PORT'] = 2525

mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.debug = True

from app import routes, models
