from datetime import datetime

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

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(dict):
        obj = Solution(dict)
        obj.id = dict['id']
        obj.status = dict['status']
        obj.mark = dict['mark']
        obj.enqueued_at = dict['enqueued_at']
        obj.processed_at = dict['processed_at']
        return obj
