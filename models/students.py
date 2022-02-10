from flask_restful import Resource, fields, marshal_with, reqparse
from models import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50))
    number = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        res = self.last_name + ' ' + self.first_name[0] + '.'
        if self.second_name:
            res += ' ' + self.second_name[0] + '.'
        return res


fields = {
    'id': fields.Integer,
    'last_name': fields.String,
    'first_name': fields.String,
    'second_name': fields.String,
    'number': fields.String,
}


parser = reqparse.RequestParser()
parser.add_argument('last_name', type=str, required=True)
parser.add_argument('first_name', type=str, required=True)
parser.add_argument('second_name', type=str)
parser.add_argument('number', type=str, required=True)

class StudentApi(Resource):
    @marshal_with(fields)
    def get(self, student_id):
        return Student.query.get_or_404(student_id)


class StudentListApi(Resource):
    @marshal_with(fields)
    def get(self):
        return Student.query.all()

    @marshal_with(fields)
    def post(self):
        args = parser.parse_args()
        s = Student(**args)
        db.session.add(s)
        db.session.commit()
        return s
