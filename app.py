from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from models import db, students

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
Migrate(app, db)

api = Api(app)
api.add_resource(students.StudentApi, '/<int:student_id>/')
api.add_resource(students.StudentListApi, '/')
