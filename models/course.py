from flask_restx import fields, reqparse
from models import db, ObjectApi, ObjectListApi


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    # task_set = db.relationship('Task', backref='course', lazy=True)

    def __repr__(self):
        return self.code + ' ' + self.name


fields = {
    'id': fields.Integer,
    'code': fields.String,
    'name': fields.String,
}


parser = reqparse.RequestParser()
parser.add_argument('code', type=str, required=True)
parser.add_argument('name', type=str, required=True)

class CourseApi(ObjectApi):
    model_cls = Course
    fields = fields
    parser = parser


class CourseListApi(ObjectListApi):
    model_cls = Course
    fields = fields
    parser = parser
