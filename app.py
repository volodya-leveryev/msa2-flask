from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate

from models import api, db, course, students, task


def get_secret_key():
    try:
        f = open('secret_key')
        return f.readline()
    except FileNotFoundError as e:
        print('Secret key file not found!')
    return 'secret'


app = Flask(__name__)
app.config['SECRET_KEY'] = get_secret_key()
app.config['SERVER_NAME'] = 'localhost:5000'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
Migrate(app, db)

admin = Admin(app)
admin.add_view(ModelView(students.Student, db.session))
admin.add_view(ModelView(course.Course, db.session))
admin.add_view(ModelView(task.Task, db.session))

api.init_app(app)
api.add_resource(students.StudentApi, '/students/<int:obj_id>/')
api.add_resource(students.StudentListApi, '/students/')
api.add_resource(course.CourseApi, '/course/<int:obj_id>/')
api.add_resource(course.CourseListApi, '/course/')
api.add_resource(task.TaskApi, '/task/<int:obj_id>/')
api.add_resource(task.TaskListApi, '/task/')
