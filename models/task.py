from flask_restx import fields, reqparse
from models import db, ObjectApi, ObjectListApi


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return self.name


fields = {
    'id': fields.Integer,
    'course_id': fields.Integer,
    'name': fields.String,
    'text': fields.String,
}


parser = reqparse.RequestParser()
parser.add_argument('course_id', type=int, required=True)
parser.add_argument('name', type=str, required=True)
parser.add_argument('text', type=str, required=True)

class TaskApi(ObjectApi):
    model_cls = Task
    fields = fields
    parser = parser


class TaskListApi(ObjectListApi):
    model_cls = Task
    fields = fields
    parser = parser
