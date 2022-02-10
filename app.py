from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from flask_restful import Api

from models import db, students


def get_secret_key():
    try:
        f = open('secret_key')
        return f.readline()
    except FileNotFoundError as e:
        print('Secret key file not found!')
    return 'secret'


app = Flask(__name__)
app.config['SECRET_KEY'] = get_secret_key()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
Migrate(app, db)

admin = Admin(app)
admin.add_view(ModelView(students.Student, db.session))

api = Api(app)
api.add_resource(students.StudentApi, '/students/<int:student_id>/')
api.add_resource(students.StudentListApi, '/students/')
