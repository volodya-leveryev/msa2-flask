from flask import request
from flask_restx import Resource, marshal, reqparse
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ObjectApi(Resource):
    model_cls = db.Model
    fields = {}
    parser = reqparse.RequestParser()

    def get(self, obj_id):
        s = self.model_cls.query.get_or_404(obj_id)
        return marshal(s, self.fields)

    def delete(self, obj_id):
        s = self.model_cls.query.get_or_404(obj_id)
        db.session.delete(s)
        db.session.commit()
        return {'success': True}

    def put(self, obj_id):
        s = self.model_cls.query.get_or_404(obj_id)
        args = self.parser.parse_args()
        for k, v in args.items():
            s.__setattr__(k, v)
        db.session.merge(s)
        db.session.commit()
        return marshal(s, self.fields)


class ObjectListApi(Resource):
    model_cls = db.Model
    fields = {}
    parser = reqparse.RequestParser()

    def get(self):
        size, page = 20, int(request.args.get('p', 0))
        print(size * page)
        res = self.model_cls.query.offset(size * page).limit(size).all()
        return marshal(res, self.fields)

    def post(self):
        args = self.parser.parse_args()
        s = self.model_cls(**args)
        db.session.add(s)
        db.session.commit()
        return marshal(s, self.fields)
