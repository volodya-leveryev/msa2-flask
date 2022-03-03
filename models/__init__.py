from flask import abort, request
from flask_restx import Api, Resource, marshal, reqparse
from flask_sqlalchemy import SQLAlchemy

authorizations = {
    'ApiKeyAuth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-Key',
    }
}
api = Api(authorizations=authorizations)
db = SQLAlchemy()


def api_key_required(func):
    def wrapper(*args, **kwargs):
        # api_key = request.headers.get('X-API-Key')
        # if not api_key:
        #     abort(403)
        # elif api_key != '12345':
        #     abort(403)
        return func(*args, **kwargs)
    return wrapper


class ObjectApi(Resource):
    model_cls = db.Model
    fields = {}
    parser = reqparse.RequestParser()

    @api_key_required
    def get(self, obj_id):
        s = self.model_cls.query.get_or_404(obj_id)
        return marshal(s, self.fields)

    @api_key_required
    def delete(self, obj_id):
        s = self.model_cls.query.get_or_404(obj_id)
        db.session.delete(s)
        db.session.commit()
        return {'success': True}

    @api_key_required
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

    @api.doc(params={'p': {
        'description': 'Page number, positive integer number',
        'type': 'int',
    }})
    @api_key_required
    def get(self):
        size, page = 20, int(request.args.get('p', 0))
        res = self.model_cls.query.offset(size * page).limit(size).all()
        return marshal(res, self.fields)

    @api_key_required
    def post(self):
        args = self.parser.parse_args()
        s = self.model_cls(**args)
        db.session.add(s)
        db.session.commit()
        return marshal(s, self.fields)
