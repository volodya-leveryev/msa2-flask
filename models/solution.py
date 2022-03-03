"""
Постановка решений задач в очередь (POST)
Получение списка решений в очереди (GET)
Получение оценки по решению в очереди (GET id)
"""
from flask import request
from flask_restx import Resource, marshal, reqparse, fields
from redis import Redis

from . import api_key_required

fields = {
    'id': fields.Integer,
    'task_id': fields.Integer,
    'student_id': fields.Integer,
    'status': fields.String,  # IN_QUEUE - Q, PROCESSED - P, FAILED - F
    'text': fields.String,
    'mark': fields.Integer,
    'enqueued_at': fields.DateTime,
    'processed_at': fields.DateTime,
}

parser = reqparse.RequestParser()
parser.add_argument('task_id', type=int, required=True)
parser.add_argument('student_id', type=int, required=True)
parser.add_argument('text', type=str, required=True)
parser.add_argument('status', type=str, required=True)


class SolutionApi(Resource):
    parser = reqparse.RequestParser()

    @api_key_required
    def get(self, obj_id):
        # Запросить из Redis решение
        res = {}
        return marshal(res, self.fields)


class SolutionListApi(Resource):
    parser = reqparse.RequestParser()

    @api_key_required
    def get(self):
        """
        Список решений
        Фильтры:
        - номер страницы
        - по студенту
        """
        size, page = 20, int(request.args.get('p', 0))
        task_id = int(request.args.get('t', 0))
        # Запросить из Redis список решений
        res = []
        return marshal(res, self.fields)

    @api_key_required
    def post(self):
        args = self.parser.parse_args()
        # Создать решение в Redis
        r = Redis(host='localhost', port=6379, db=0)
        r.publish('solutions')
        res = {}
        return marshal(res, self.fields)
