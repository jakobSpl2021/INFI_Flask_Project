from flask import Flask
from controllers.index import index_blueprint
from controllers.workers import workers_blueprint
from controllers.compartments import compartments_blueprint
from controllers.workgroups import workgroups_blueprint
from models import db
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/businessapp"

csrf = CSRFProtect()

csrf.init_app(app)
db.init_app(app)

app.register_blueprint(index_blueprint)

app.register_blueprint(workers_blueprint)

app.register_blueprint(compartments_blueprint)

app.register_blueprint(workgroups_blueprint)

app.run()
