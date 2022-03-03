"""
Постановка решений задач в очередь (POST)
Получение списка решений в очереди (GET)
Получение оценки по решению в очереди (GET id)
"""
from datetime import datetime

from flask import request
from flask_restx import Resource, marshal, reqparse, fields
from redis import Redis

from tasks import process_solution

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


class Solution:
    # TODO: Написать сериализацию в JSON
    def __init__(self, args):
        print(args)
        self.id = 0,
        self.task_id = args['task_id']
        self.student_id = args['student_id']
        self.status = 'Q'
        self.text = args['text']
        self.mark = 0
        self.enqueued_at = datetime.now()
        self.processed_at = None


class SolutionApi(Resource):
    parser = reqparse.RequestParser()

    @api_key_required
    def get(self, obj_id):
        # Запросить из Celery решение
        res = {}
        return marshal(res, self.fields)


class SolutionListApi(Resource):
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
        # Запросить из Celery список решений
        res = []
        return marshal(res, self.fields)

    @api_key_required
    def post(self):
        args = parser.parse_args()
        # Создать решение в Celery
        solution = Solution(args)
        res = process_solution.delay(solution)
        return marshal({'ok': True}, self.fields)
