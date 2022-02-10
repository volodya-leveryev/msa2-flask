from flask_restful import Resource, fields, marshal_with
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


student_fields = {
    'last_name': fields.String,
    'first_name': fields.String,
    'second_name': fields.String,
    'number': fields.String,
}


class StudentApi(Resource):
    @marshal_with(student_fields)
    def get(self):
        return Student.query.all()
