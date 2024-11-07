from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__, template_folder= 'templates')
app.secret_key = "21oe12jd1dn923jd2nqxucnq0324rf"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tofig:Sefterli0506@localhost/rtpaz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from prj import routes